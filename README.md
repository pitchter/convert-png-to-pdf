# PDF to PNG Converter

Python script to convert PDF files into PNG images using `PyMuPDF` (`fitz`) with high-quality rendering and configurable DPI.

## Features

- Automatically scans all `.pdf` files in the current directory
- High-resolution conversion (default: `300 DPI`)
- Batch processing for multiple PDF files
- Clear terminal logs for progress and errors

## Tech Stack

- Python
- [PyMuPDF](https://pymupdf.readthedocs.io/)

## Requirements

- Python 3.8+ (3.10+ recommended)
- Dependencies listed in `requirements.txt`

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Place your `.pdf` files in the same directory as `convert.py`.
2. Run:

```bash
python convert.py
```

3. The script will detect PDF files and start converting immediately.

Example terminal output:

```text
Found 2 PDF files.
Processing: sample.pdf
  Saved: sample.png
Done!
```

## Output

- Images are saved in the same directory as the script.
- Output filename format: `<original_filename>.png`

## Configuration

Default DPI is set to `300` in:

```python
convert_pdf_to_png(pdf_path, dpi=300)
```

To adjust output quality and file size, change the `dpi` value in the code.

## Current Limitation

In the current implementation, multi-page PDFs are saved repeatedly to the same filename (`<base_name>.png`). Each new page overwrites the previous one, so only the last page remains per PDF file.

## Project Structure

```text
.
├── convert.py
├── requirements.txt
└── README.md
```

## License

No license is currently specified. If you plan to use or distribute this project, add a `LICENSE` file.
