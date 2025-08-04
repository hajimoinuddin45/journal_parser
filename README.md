# 🧠 Journal Parser with OCR, PostgreSQL & Docker

A Dockerized Python project that extracts structured data from trademark journal PDFs using OCR (PaddleOCR) and stores the results in a PostgreSQL database.

---

## 🚀 Features

- 🔍 **OCR-powered parsing** using PaddleOCR
- 🐘 **PostgreSQL** for storing parsed data
- 🐳 **Docker Compose** setup for multi-container orchestration
- 📄 **PDF input** with table/field extraction
- 🔬 **Modular design** for easy extension

---

## 📦 Folder Structure

journal_parser/
├── app/
│ ├── database.py
│ ├── ocr.py
│ └── parser.py
├── data/
│ └── journal.pdf
├── migrations/
│ └── init.sql
├── parse_journal.py
├── requirements.txt
├── docker-compose.yml
└── Dockerfile

---

## 🛠️ Setup & Usage

### ✅ Prerequisites

- Docker & Docker Compose installed
- NVIDIA GPU with CUDA (for GPU OCR acceleration)
- WSL2 + NVIDIA drivers if on Windows

---

### 🔧 1️⃣ Build & Run Containers

```bash
docker-compose down -v
docker-compose up --build
```  <!-- ✅ This closes step 1's code block -->

initialize_database:
  title: "🗃️ 2️⃣ Initialize the Database"
  description: "This step sets up the required database schema."
  commands:
    - docker cp migrations/init.sql journal_parser-db-1:/init.sql
    - docker exec -it journal_parser-db-1 psql -U admin -d trademark_journals -f /init.sql

run_parser:
  title: "🧠 3️⃣ Run the OCR Parser"
  description: "This runs the parser script to extract data from the PDF and insert it into the database."
  command: docker exec -it journal_parser-app-1 python3 parse_journal.py data/journal.pdf --db-url postgresql://admin:admin@db:5432/trademark_journals --batch-size 10

verify_output:
  title: "✅ 4️⃣ Verify Parsed Output"
  description: "To check if the parsed data was successfully stored."
  steps:
    - docker exec -it journal_parser-db-1 psql -U admin -d trademark_journals
    - "Inside the PostgreSQL prompt, run:"
    - "\\dt"
    - "SELECT * FROM trademarks LIMIT 5;"

author:
  name: "✍️ Haji Moinuddin"
  profile: "GitHub Profile"

license:
  type: "📄 MIT License"

