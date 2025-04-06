#!/usr/bin/env python3
"""
Enhanced OCR PDF Command-Line Tool

This script converts PDF documents to images, performs OCR using the
stepfun-ai/GOT-OCR2_0 model from Hugging Face, and outputs the extracted
text in Markdown or plain text format. It now supports processing multiple
PDF files from a specified folder.

Author: Your Name
Created: 2024-09-24
"""

import os
import typer
from pathlib import Path
from typing import Optional
from pdf2image import convert_from_path
from transformers import AutoModel, AutoTokenizer
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn
from rich.markdown import Markdown
from rich.prompt import Prompt

# Initialize Typer app and Rich console
app = typer.Typer()
console = Console()

# Default model name
MODEL_NAME = 'stepfun-ai/GOT-OCR2_0'

def process_pdf(
    input_file: Path,
    output_dir: Path,
    format: str,
    ocr_type: str,
    model,
    tokenizer,
    verbose: bool
):
    """Process a single PDF file."""
    output_file = output_dir / (input_file.stem + ('.md' if format.lower() == 'md' else '.txt'))

    console.print(f"[bold blue]Processing:[/bold blue] [underline]{input_file}[/underline]")
    console.print(f"Output will be saved to [underline]{output_file}[/underline]\n")

    # Convert PDF to images
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        "•",
        TimeElapsedColumn(),
        "•",
        TimeRemainingColumn(),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("Converting PDF to images...", total=100)
        try:
            images = convert_from_path(str(input_file))
            progress.update(task, advance=100)
        except Exception as e:
            console.print(f"[bold red]Error during PDF conversion:[/bold red] {e}")
            return

    num_pages = len(images)
    console.print(f"Converted PDF into [bold]{num_pages}[/bold] image(s).\n")

    # Perform OCR on each image
    extracted_text = []
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        "•",
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Performing OCR on images...", total=num_pages)
        for idx, image in enumerate(images, start=1):
            temp_image_path = f"temp_page_{idx}.jpg"
            image.save(temp_image_path, "JPEG")

            try:
                ocr_result = model.chat(
                    tokenizer,
                    temp_image_path,
                    ocr_type=ocr_type.lower()
                )
                extracted_text.append(f"## Page {idx}\n\n{ocr_result}\n")
            except Exception as e:
                console.print(f"[bold red]Error during OCR on page {idx}:[/bold red] {e}")
                extracted_text.append(f"## Page {idx}\n\n[Error during OCR]\n")

            os.remove(temp_image_path)
            progress.advance(task)

    # Write to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            if format.lower() == 'md':
                f.write("# OCR Extraction\n\n")
            for page_text in extracted_text:
                f.write(page_text)
        console.print(f"[bold green]OCR completed for {input_file.name}![/bold green]")
        console.print(f"Extracted text saved to [underline]{output_file}[/underline]\n")
    except Exception as e:
        console.print(f"[bold red]Error writing to output file:[/bold red] {e}")

    if verbose and extracted_text:
        console.print("[bold yellow]Preview of the first page:[/bold yellow]")
        console.print(Markdown(extracted_text[0]) if format.lower() == 'md' else extracted_text[0])

@app.command()
def main(
    format: str = typer.Option("md", "--format", "-f", help="Output format: 'md' for Markdown or 'txt' for plain text.", case_sensitive=False),
    ocr_type: str = typer.Option("ocr", "--ocr-type", "-t", help="OCR type: 'ocr' for plain text or 'format' for formatted OCR.", case_sensitive=False),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose mode.")
):
    """
    An enhanced command-line tool to perform OCR on multiple PDF documents
    from a specified folder and output the extracted text in Markdown or
    plain text format.
    """
    console.print("[bold magenta]Enhanced OCR PDF Processor[/bold magenta]\n")

    # Ask for input folder
    input_folder = Prompt.ask("Enter the path to the folder containing PDF files", default=str(Path.cwd()))
    input_folder = Path(input_folder)

    if not input_folder.exists() or not input_folder.is_dir():
        console.print(f"[bold red]Error:[/bold red] The specified folder does not exist or is not a directory.")
        raise typer.Exit(code=1)

    # Set output directory
    output_dir = input_folder / "ocr_output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load OCR model
    console.print("[bold green]Loading OCR model...[/bold green]")
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
        model = AutoModel.from_pretrained(
            MODEL_NAME,
            trust_remote_code=True,
            low_cpu_mem_usage=True,
            device_map='auto',
            use_safetensors=True,
            pad_token_id=tokenizer.eos_token_id
        )
        model = model.eval()
    except Exception as e:
        console.print(f"[bold red]Error loading model:[/bold red] {e}")
        raise typer.Exit(code=1)
    console.print("[bold green]Model loaded successfully.[/bold green]\n")

    # Process PDF files
    pdf_files = list(input_folder.glob("*.pdf"))
    if not pdf_files:
        console.print("[bold yellow]No PDF files found in the specified folder.[/bold yellow]")
        raise typer.Exit(code=0)

    console.print(f"[bold green]Found {len(pdf_files)} PDF file(s) to process.[/bold green]\n")

    for pdf_file in pdf_files:
        process_pdf(pdf_file, output_dir, format, ocr_type, model, tokenizer, verbose)

    console.print("[bold green]All PDF files processed successfully![/bold green]")

if __name__ == "__main__":
    app()
