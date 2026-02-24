import os
import fitz  # PyMuPDF

def convert_pdf_to_png(pdf_path, dpi=300):
    """
    Converts a PDF file to PNG images (one per page) with high quality.
    """
    print(f"Processing: {pdf_path}")
    doc = fitz.open(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Calculate matrix for desired DPI (default PDF is usually 72 DPI)
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=mat)
        output_file = f"{base_name}.png"
        pix.save(output_file)
        print(f"  Saved: {output_file}")
    
    print("Done!")

def main():
    # Scan for PDF files in the current directory
    pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return

    print(f"Found {len(pdf_files)} PDF files.")
    
    for pdf_file in pdf_files:
        try:
            convert_pdf_to_png(pdf_file)
        except Exception as e:
            print(f"Error converting {pdf_file}: {e}")

if __name__ == "__main__":
    main()
