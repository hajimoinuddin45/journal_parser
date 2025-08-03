import argparse
from app.ocr import extract_text_from_pdf
from app.parser import extract_fields
from app.database import Database
from dotenv import load_dotenv
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_path", type=str, help="Path to journal PDF")
    parser.add_argument("--db-url", type=str, required=True, help="PostgreSQL connection URL")
    parser.add_argument("--batch-size", type=int, default=10, help="Batch size for processing")
    args = parser.parse_args()

    load_dotenv()
    raw_text = extract_text_from_pdf(args.pdf_path)
    entries = extract_fields(raw_text)
    db = Database(args.db_url)
    db.insert_batch(entries, batch_size=args.batch_size)

if __name__ == '__main__':
    main()