import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mlxpipeline.core import (
    calculate_tokens,
    load_json_schema,
    make_image_url,
    parse_arguments,
)


class TestCore(unittest.TestCase):
    """Test cases for core module functions."""

    def test_calculate_tokens(self):
        """Test token calculation."""
        # Test with simple text
        text = "This is a test text with approximately 10 tokens."
        # Without tokenizer, should use fallback method (~4 chars = 1 token)
        tokens = calculate_tokens(text)
        self.assertGreater(tokens, 0)
        self.assertLess(tokens, len(text))

        # Test with mock tokenizer
        mock_tokenizer = MagicMock()
        mock_tokenizer.encode.return_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        tokens = calculate_tokens(text, tokenizer=mock_tokenizer)
        self.assertEqual(tokens, 10)
        mock_tokenizer.encode.assert_called_once_with(text)

    def test_make_image_url(self):
        """Test image URL generation."""
        # Create a temporary image file
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_img:
            temp_img.write(b"test image content")
            temp_img_path = temp_img.name

        try:
            # Test making an image URL
            image_url = make_image_url(temp_img_path)

            # Check if it's a base64 data URL
            self.assertTrue(image_url.startswith("data:image/jpeg;base64,"))

            # Check if the content is encoded correctly
            content_part = image_url.split(",")[1]
            import base64

            decoded = base64.b64decode(content_part)
            self.assertEqual(decoded, b"test image content")
        finally:
            # Clean up
            os.unlink(temp_img_path)

    def test_parse_arguments(self):
        """Test argument parsing."""
        # Test with minimal arguments
        args = parse_arguments(["--source", "test.txt"])
        self.assertEqual(args.source, "test.txt")
        self.assertEqual(args.chunk_type, "text")  # Default value

        # Test with chunk argument
        args = parse_arguments(["--chunk", "chunk.txt", "--schema", "schema.json", "--extract"])
        self.assertEqual(args.chunk, "chunk.txt")
        self.assertEqual(args.schema, "schema.json")
        self.assertTrue(args.extract)

        # Test with custom model paths
        custom_llm_path = "/path/to/custom/llm"
        args = parse_arguments(["--source", "test.txt", "--llm-model-path", custom_llm_path])
        self.assertEqual(args.llm_model_path, custom_llm_path)

    def test_load_json_schema(self):
        """Test loading JSON schema."""
        # Create a temporary schema file
        schema_content = '{"type": "object", "properties": {"name": {"type": "string"}}}'
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as temp_schema:
            temp_schema.write(schema_content)
            temp_schema_path = temp_schema.name

        try:
            # Test loading the schema
            schema = load_json_schema(temp_schema_path)
            self.assertIsInstance(schema, dict)
            self.assertEqual(schema["type"], "object")
            self.assertIn("properties", schema)
            self.assertIn("name", schema["properties"])
        finally:
            # Clean up
            os.unlink(temp_schema_path)

    @patch("sys.exit")
    def test_load_json_schema_error(self, mock_exit):
        """Test error handling when loading invalid JSON schema."""
        # Create a temporary invalid schema file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as temp_schema:
            temp_schema.write('{"invalid": json')
            temp_schema_path = temp_schema.name

        try:
            # Test loading the invalid schema
            load_json_schema(temp_schema_path)
            mock_exit.assert_called_once()
        finally:
            # Clean up
            os.unlink(temp_schema_path)


if __name__ == "__main__":
    unittest.main()
