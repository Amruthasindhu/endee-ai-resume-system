# AI Resume + Interview Assistant

An intelligent web application that analyzes resumes against job descriptions using **RAG (Retrieval-Augmented Generation)**. Upload a PDF resume, paste a job description, and instantly get a structured evaluation powered by OpenAI GPT.

## Features

- Upload resume as a PDF
- Paste any job description
- Auto-generates a structured analysis:
  - **Eligibility Score** (0–100)
  - **Matched Skills**
  - **Missing Skills**
  - **Final Verdict**
  - **Actionable Suggestions**
- Ask custom follow-up questions about resume-job fit
- Fast semantic search using OpenAI vector embeddings
- Custom in-memory vector database (Endee Store)

## Tech Stack

| Layer        | Technology                    |
| ------------ | ----------------------------- |
| Frontend     | Streamlit                     |
| LLM          | OpenAI GPT-3.5-turbo          |
| Embeddings   | OpenAI text-embedding-ada-002 |
| Vector Store | Custom Endee Vector Database  |
| PDF Parsing  | PyPDF2                        |
| Environment  | python-dotenv                 |

## Project Structure

```
ai-resume-assistant/
│
├── app.py                  # Streamlit frontend
│
├── backend/
│   ├── rag.py              # RAG pipeline + OpenAI GPT integration
│   ├── embeddings.py       # OpenAI embedding generation
│   └── endee_store.py      # Custom vector database
│
├── utils/
│   ├── pdf_parser.py       # PDF text extraction
│   └── chunking.py         # Text chunking logic
│
├── .env                    # API keys (do NOT push to GitHub)
├── .gitignore              # Excludes .env and other sensitive files
├── requirements.txt        # Python dependencies
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-resume-assistant.git
cd ai-resume-assistant
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Create a `.env` file in the root of the project:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> Never push this file to GitHub. Make sure `.env` is listed in your `.gitignore`.

### 5. Run the application

```bash
streamlit run app.py
```

## How It Works

```
PDF Resume
    │
    ▼
Text Extraction (PyPDF2)
    │
    ▼
Text Chunking (200 words/chunk)
    │
    ▼
OpenAI Embeddings (text-embedding-ada-002)
    │
    ▼
Endee Vector Store (cosine similarity search)
    │
    ▼
Job Description + Query → Top-K Relevant Chunks Retrieved
    │
    ▼
Structured Prompt → OpenAI GPT-3.5-turbo
    │
    ▼
Eligibility Score · Matched Skills · Missing Skills · Verdict · Suggestions
```

## Example Output

```
Eligibility Score: 72

Matched Skills:
- Python
- Machine Learning
- SQL
- REST APIs

Missing Skills:
- AWS / GCP
- Docker
- Tableau / Power BI

Final Verdict:
Partially Eligible — strong core skills, but lacks cloud and visualization experience.

Suggestions:
- Earn an AWS or GCP cloud certification
- Build a portfolio project using Docker
- Complete a Tableau or Power BI course
```

## Security Notes

- Store your API key in `.env` only — never hardcode it in source files
- Add the following to your `.gitignore`:

```
.env
__pycache__/
*.pyc
venv/
```

## Future Enhancements

- PDF report download of the analysis
- Chat history tracking across sessions
- Multi-job comparison mode
- Resume rewrite suggestions

## Author

Amrutha Sindhu
AIML Engineering Student

## Acknowledgements

- [OpenAI](https://openai.com) for GPT and embedding models
- [Streamlit](https://streamlit.io) for the rapid UI framework
- [PyPDF2](https://pypdf2.readthedocs.io) for PDF parsing
