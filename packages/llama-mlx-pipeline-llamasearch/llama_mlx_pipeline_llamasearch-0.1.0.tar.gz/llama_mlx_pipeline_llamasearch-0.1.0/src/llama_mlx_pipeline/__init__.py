import argparse
import os
import sys
from typing import Any, Dict, List, Optional

from .chunker import chunk_semantic, chunk_text
from .core import parse_arguments
from .extractor import extract_from_chunk
from .scraper import (
    ai_extract_pdf_content,
    ai_extract_webpage_content,
    extract_from_documents,
    scrape_audio,
    scrape_csv,
    scrape_docx,
    scrape_html,
    scrape_image,
    scrape_json,
    scrape_markdown,
    scrape_pdf,
    scrape_pptx,
    scrape_text,
    scrape_video,
    scrape_webpage,
    scrape_youtube,
)

__version__ = "0.1.0"


def main():
    """
    Main entry point for the mlxpipeline command line interface.
    """
    args = parse_arguments()

    # Process the input based on arguments
    result = process_input(args)

    # Output the result
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result)

    return 0


def process_input(args: argparse.Namespace) -> str:
    """
    Process the input based on the provided arguments.

    Args:
        args: Parsed command line arguments

    Returns:
        str: Processed output
    """
    # Extract from chunk if extraction was specified
    if args.extract and args.chunk:
        with open(args.chunk, "r", encoding="utf-8") as f:
            chunk = f.read()

        result = extract_from_chunk(
            chunk,
            schema=args.schema,
            extraction_prompt=args.extraction_prompt,
            llm_model_path=args.llm_model_path,
        )
        return result

    # Scrape content from source if specified
    if args.source:
        content = scrape_content(args)

        # If no chunking or extraction is needed, return the scraped content
        if not args.chunk_type:
            return content

        # Chunk the content if specified
        chunks = chunk_content(content, args)

        # Extract from chunks if specified
        if args.extract:
            results = []
            for chunk in chunks:
                result = extract_from_chunk(
                    chunk,
                    schema=args.schema,
                    extraction_prompt=args.extraction_prompt,
                    llm_model_path=args.llm_model_path,
                )
                results.append(result)
            return "\n\n".join(results)

        # If no extraction was specified, return the chunks
        return "\n\n---\n\n".join(chunks)

    # If neither chunk nor source was specified, print help
    print("Error: Either --chunk or --source must be specified.")
    parse_arguments(["--help"])
    return ""


def scrape_content(args: argparse.Namespace) -> str:
    """
    Scrape content based on the provided arguments.

    Args:
        args: Parsed command line arguments

    Returns:
        str: Scraped content
    """
    source_type = args.source_type
    source = args.source

    # Determine source type if not specified
    if not source_type:
        if source.startswith(("http://", "https://")):
            source_type = "url"
        elif source.endswith(".pdf"):
            source_type = "pdf"
        elif source.endswith(".docx"):
            source_type = "docx"
        elif source.endswith(".pptx"):
            source_type = "pptx"
        elif source.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
            source_type = "image"
        elif source.endswith((".mp3", ".wav", ".ogg", ".flac", ".m4a")):
            source_type = "audio"
        elif source.endswith((".mp4", ".mov", ".avi", ".mkv", ".webm")):
            source_type = "video"
        elif source.endswith(".md"):
            source_type = "markdown"
        elif source.endswith(".json"):
            source_type = "json"
        elif source.endswith((".csv", ".tsv")):
            source_type = "csv"
        elif source.endswith((".txt", ".text")):
            source_type = "text"
        else:
            source_type = "text"  # Default to text

    # Scrape based on source type
    if source_type == "url":
        if "youtube.com" in source or "youtu.be" in source:
            return scrape_youtube(source, whisper_model_path=args.whisper_model_path)
        elif args.ai_extract:
            return ai_extract_webpage_content(source, llm_model_path=args.llm_model_path)
        else:
            return scrape_webpage(source)
    elif source_type == "pdf":
        if args.ai_extract:
            return ai_extract_pdf_content(source, llm_model_path=args.llm_model_path)
        else:
            return scrape_pdf(source)
    elif source_type == "docx":
        return scrape_docx(source)
    elif source_type == "pptx":
        return scrape_pptx(source)
    elif source_type == "image":
        return scrape_image(source)
    elif source_type == "audio":
        return scrape_audio(source, whisper_model_path=args.whisper_model_path)
    elif source_type == "video":
        return scrape_video(source, whisper_model_path=args.whisper_model_path)
    elif source_type == "markdown":
        return scrape_markdown(source)
    elif source_type == "json":
        return scrape_json(source)
    elif source_type == "csv":
        return scrape_csv(source)
    elif source_type == "html":
        return scrape_html(source)
    else:  # Default to text
        return scrape_text(source)


def chunk_content(content: str, args: argparse.Namespace) -> List[str]:
    """
    Chunk content based on the provided arguments.

    Args:
        content: Content to chunk
        args: Parsed command line arguments

    Returns:
        List[str]: List of chunks
    """
    chunk_type = args.chunk_type
    chunk_size = args.chunk_size
    chunk_overlap = args.chunk_overlap

    if chunk_type == "semantic":
        return chunk_semantic(
            content,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            embedding_model_path=args.embedding_model_path,
        )
    else:  # Default to text
        return chunk_text(
            content,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )


if __name__ == "__main__":
    sys.exit(main())
