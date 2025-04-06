import argparse
import base64
import json
import os
import sys
from typing import Any, Dict, List, Optional

# Default paths to look for models
DEFAULT_MODEL_DIR = os.path.expanduser("~/.mlxpipeline/models")

# Ensure model directories exist
os.makedirs(os.path.join(DEFAULT_MODEL_DIR, "llm"), exist_ok=True)
os.makedirs(os.path.join(DEFAULT_MODEL_DIR, "whisper"), exist_ok=True)
os.makedirs(os.path.join(DEFAULT_MODEL_DIR, "embeddings"), exist_ok=True)

# Default model paths
DEFAULT_LLM_MODEL_PATH = os.path.join(DEFAULT_MODEL_DIR, "llm/llama-3-8b-mlx-quantized")
DEFAULT_WHISPER_MODEL_PATH = os.path.join(DEFAULT_MODEL_DIR, "whisper/whisper-small-mlx")
DEFAULT_EMBEDDING_MODEL_PATH = os.path.join(DEFAULT_MODEL_DIR, "embeddings/all-minilm-l6-v2-mlx")

# Default extraction prompt
DEFAULT_EXTRACTION_PROMPT = """
I need to extract specific information from the following text into JSON format.
Please focus only on facts and information explicitly mentioned in the text.
Don't make assumptions or add information not present in the text.

When extracting information, follow these guidelines:
1. If a piece of information is not mentioned, use null for that field.
2. Use exact quotes from the source when appropriate.
3. For dates, use ISO format (YYYY-MM-DD) when possible.
4. Extract all relevant information according to the schema.

Here's the text to analyze:
{text}

Extract the information according to this schema:
{schema}

Respond ONLY with the JSON object containing the extracted information.
"""


def make_image_url(image_path: str) -> str:
    """
    Encode image as base64 for local model consumption.

    Args:
        image_path: Path to the image

    Returns:
        str: Base64 encoded image
    """
    with open(image_path, "rb") as f:
        return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"


def calculate_tokens(text: str, tokenizer=None) -> int:
    """
    Calculate the number of tokens in the text using MLX tokenizer if provided,
    otherwise use a rough estimate.

    Args:
        text: Text to calculate tokens for
        tokenizer: MLX tokenizer instance

    Returns:
        int: Approximate number of tokens
    """
    if tokenizer:
        # Use the MLX tokenizer to get accurate token count
        tokens = tokenizer.encode(text)
        return len(tokens)
    else:
        # Fallback to rough approximation (4 chars ~= 1 token)
        return len(text) // 4


def parse_arguments(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command line arguments.

    Args:
        args: Command line arguments

    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="MLXPipeline: Local-First Data Extraction Pipeline powered by Apple MLX"
    )

    # Input/Output arguments
    parser.add_argument("--source", type=str, help="Source file or URL to scrape")
    parser.add_argument(
        "--source-type",
        type=str,
        choices=[
            "url",
            "pdf",
            "docx",
            "pptx",
            "image",
            "audio",
            "video",
            "text",
            "markdown",
            "json",
            "csv",
            "html",
        ],
        help="Type of source (autodetected if not specified)",
    )
    parser.add_argument(
        "--chunk",
        type=str,
        help="Path to file containing a chunk for extraction (alternative to --source)",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path (outputs to stdout if not specified)",
    )

    # Chunking arguments
    parser.add_argument(
        "--chunk-type",
        type=str,
        choices=["text", "semantic"],
        default="text",
        help="Chunking method to use",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=1000,
        help="Maximum size of chunks (in characters for text, in semantic units for semantic)",
    )
    parser.add_argument(
        "--chunk-overlap",
        type=int,
        default=100,
        help="Overlap between chunks (in characters for text, in semantic units for semantic)",
    )

    # Extraction arguments
    parser.add_argument(
        "--extract",
        action="store_true",
        help="Extract structured information from the content",
    )
    parser.add_argument(
        "--schema",
        type=str,
        help="JSON schema for extraction (required if --extract is specified)",
    )
    parser.add_argument(
        "--extraction-prompt",
        type=str,
        help="Custom prompt for extraction (uses default if not specified)",
    )
    parser.add_argument(
        "--ai-extract",
        action="store_true",
        help="Use AI to extract relevant content before processing (for webpages and PDFs)",
    )

    # Model path arguments
    parser.add_argument(
        "--llm-model-path",
        type=str,
        default=DEFAULT_LLM_MODEL_PATH,
        help=f"Path to the MLX LLM model for extraction (default: {DEFAULT_LLM_MODEL_PATH})",
    )
    parser.add_argument(
        "--whisper-model-path",
        type=str,
        default=DEFAULT_WHISPER_MODEL_PATH,
        help=f"Path to the MLX Whisper model for audio transcription (default: {DEFAULT_WHISPER_MODEL_PATH})",
    )
    parser.add_argument(
        "--embedding-model-path",
        type=str,
        default=DEFAULT_EMBEDDING_MODEL_PATH,
        help=f"Path to the MLX embedding model for semantic chunking (default: {DEFAULT_EMBEDDING_MODEL_PATH})",
    )

    # Parse arguments
    parsed_args = parser.parse_args(args)

    # Validate arguments
    if parsed_args.extract and not parsed_args.schema:
        parser.error("--schema is required when --extract is specified")

    if not parsed_args.source and not parsed_args.chunk:
        parser.error("Either --source or --chunk must be specified")

    return parsed_args


def load_json_schema(schema_path: str) -> Dict[str, Any]:
    """
    Load a JSON schema from a file.

    Args:
        schema_path: Path to the schema file

    Returns:
        Dict[str, Any]: Loaded schema
    """
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON schema: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading schema file: {e}")
        sys.exit(1)
