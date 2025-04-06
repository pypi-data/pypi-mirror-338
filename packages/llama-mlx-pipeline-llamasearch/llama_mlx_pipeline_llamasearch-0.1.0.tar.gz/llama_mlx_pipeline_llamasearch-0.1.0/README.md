# MLXPipeline

A Local-First Data Extraction Pipeline powered by Apple MLX

![MLXPipeline Banner](https://via.placeholder.com/800x200?text=MLXPipeline)

## Overview

**MLXPipeline** is a Python package for extracting, chunking, and analyzing data from various sources, optimized specifically for Apple Silicon. Unlike cloud-based solutions, MLXPipeline performs all processing, including machine learning inference tasks, locally on your machine.

Built on Apple's MLX framework, it efficiently leverages Apple's M-series chips to provide:

- 🔒 **Enhanced Privacy**: All data stays on your device
- 💰 **Cost Efficiency**: No API fees or usage limits
- ⚡ **Speed**: Optimized for Apple Silicon (M1/M2/M3 chips)
- 🔄 **Versatility**: Handles text, PDFs, webpages, images, audio, video, and more

## Features

### Content Extraction
- **Document Parsing**: Extract text from PDFs, DOCX, PPTX, HTML, Markdown, JSON, CSV
- **Web Scraping**: Extract content from websites with clean-up of navigation, ads, etc.
- **OCR**: Extract text from images using Optical Character Recognition
- **Audio Transcription**: Convert audio files to text using MLX-powered Whisper
- **Video Transcription**: Extract and transcribe audio from video files

### Content Processing
- **Text Chunking**: Split large documents into manageable chunks based on size
- **Semantic Chunking**: Create chunks based on semantic similarity using embeddings
- **Structured Information Extraction**: Extract specific information using local LLMs

### Local-First Machine Learning
- **MLX-Powered**: Uses Apple's MLX framework for ML tasks
- **Embeddings**: Generate text embeddings for semantic processing
- **Transcription**: Local audio transcription using MLX Whisper models
- **LLM Integration**: Use local Large Language Models for content extraction and analysis

## Requirements

- macOS on Apple Silicon (M1/M2/M3 or newer)
- Python 3.9+
- MLX compatible models (not included in the package)

## Installation

```bash
pip install mlxpipeline
```

### Model Setup

MLXPipeline requires pre-downloaded MLX-compatible models to function. You should download:

1. **MLX LLM Model**: For extraction and analysis (e.g., Llama-3-8B-MLX)
2. **MLX Whisper Model**: For audio transcription
3. **MLX Embedding Model**: For semantic chunking (e.g., all-MiniLM-L6-v2)

These models should be placed in the default model directory `~/.mlxpipeline/models` or specified using the appropriate arguments.

You can find MLX-compatible models at:
- [MLX Community Models](https://mlx.readthedocs.io/en/latest/usage/examples.html)
- [Hugging Face](https://huggingface.co/) (models with MLX support)

## Usage

MLXPipeline can be used both as a command-line tool and as a Python library.

### Command Line Usage

**Scraping a webpage:**
```bash
mlxpipeline --source https://example.com --output result.txt
```

**Chunking a document:**
```bash
mlxpipeline --source document.pdf --chunk-type text --chunk-size 1000 --output chunks.txt
```

**Extracting structured information:**
```bash
mlxpipeline --source article.txt --extract --schema schema.json --output result.json
```

**Audio transcription:**
```bash
mlxpipeline --source recording.mp3 --whisper-model-path ~/.mlxpipeline/models/whisper-small-mlx --output transcription.txt
```

**Using a custom LLM for extraction:**
```bash
mlxpipeline --source document.pdf --extract --schema schema.json --llm-model-path ~/models/llama-3-8b-mlx --output result.json
```

### Python Library Usage

**Basic document processing:**
```python
from mlxpipeline.scraper import scrape_pdf
from mlxpipeline.chunker import chunk_text
from mlxpipeline.extract import extract_from_chunk

# Extract text from PDF
text = scrape_pdf("document.pdf")

# Split into chunks
chunks = chunk_text(text, chunk_size=1000, chunk_overlap=100)

# Extract structured information
schema = {
    "title": "string",
    "author": "string",
    "key_points": "array"
}

for i, chunk in enumerate(chunks):
    result = extract_from_chunk(
        chunk, 
        schema=schema,
        llm_model_path="~/.mlxpipeline/models/llm/llama-3-8b-mlx"
    )
    print(f"Chunk {i+1} extraction: {result}")
```

**Webpage scraping and analysis:**
```python
from mlxpipeline.scraper import scrape_webpage, ai_extract_webpage_content

# Simple webpage scraping
content = scrape_webpage("https://example.com/article")

# AI-powered extraction (focuses on main content)
main_content = ai_extract_webpage_content(
    "https://example.com/article",
    llm_model_path="~/.mlxpipeline/models/llm/llama-3-8b-mlx"
)
```

**Audio transcription:**
```python
from mlxpipeline.scraper import scrape_audio

# Transcribe audio
transcription = scrape_audio(
    "interview.mp3",
    whisper_model_path="~/.mlxpipeline/models/whisper/whisper-small-mlx"
)
```

## Differences from thepipe_api

MLXPipeline is a fork of thepipe_api that has been completely redesigned to be local-first and Apple Silicon optimized. Key differences include:

1. **Local-Only Processing**: All ML tasks run locally with no cloud API dependencies
2. **MLX Integration**: Uses Apple's MLX framework for optimized performance on Apple Silicon
3. **Model Management**: Users must download and provide MLX-compatible models
4. **Simplified Architecture**: Removed all API interactions and authentication requirements
5. **Performance Focus**: Optimized for M-series chips with unified memory architecture

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - See LICENSE file for details