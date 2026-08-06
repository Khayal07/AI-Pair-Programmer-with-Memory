# 🧠 AI Pair-Programmer with Memory

<div align="center">

### Learn from your Git history. Remember your coding habits. Generate personalized code.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge\&logo=openai\&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-CLI-009688?style=for-the-badge)
![GitPython](https://img.shields.io/badge/GitPython-History%20Mining-F05032?style=for-the-badge\&logo=git\&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063?style=for-the-badge)

*A personalized AI-powered CLI assistant that learns your coding style directly from your Git history.*

</div>

---

# 📖 Overview

Traditional AI coding assistants generate generic code suggestions.

**AI Pair-Programmer with Memory** takes a different approach.

Instead of only relying on the current prompt, the assistant analyzes your Git commit history, discovers recurring programming habits, stores them inside a local memory system, and generates suggestions that match **your own coding style**.

As your coding habits evolve, the memory adapts through a built-in decay mechanism, allowing outdated patterns to fade while strengthening frequently used ones.

---

# ✨ Features

## 🔍 Git History Mining

Automatically scans your local Git repository to learn your coding habits.

* Variable naming conventions
* Preferred libraries
* Architectural decisions
* Error handling style
* Frequently used coding patterns

---

## 🧠 AI Pattern Extraction

Uses Large Language Models (LLMs) to identify meaningful programming habits rather than simple keyword matching.

---

## 💾 Persistent Memory

Stores learned coding patterns inside a local memory database.

Features include:

* Persistent storage
* Memory scoring
* Automatic updates
* Long-term learning

---

## ⏳ Memory Decay

Older habits naturally become less important over time.

Frequently repeated patterns become stronger while outdated ones gradually disappear.

---

## 🎯 Personalized Code Suggestions

Instead of generating generic solutions, the assistant combines:

* Current prompt
* Active memory
* File context

to generate code that feels like **you wrote it yourself**.

---

## 💻 CLI Interface

Everything can be controlled directly from the terminal using simple commands.

---

# 🏛️ Architecture

```text
                    Git Repository
                           │
                           ▼
                     git_miner.py
                           │
                           ▼
                  code_scanner.py
                           │
                           ▼
               pattern_extractor.py
                           │
                           ▼
                 Memory Store
            (store.py + schemas.py)
                           │
                           ▼
                 Memory Decay
                  (decay.py)
                           │
                           ▼
              suggestion_engine.py
                           │
                           ▼
             Personalized Code Output
```

---

# 🛠 Tech Stack

| Technology               | Purpose                              |
| ------------------------ | ------------------------------------ |
| Python 3.12+             | Core programming language            |
| Typer                    | CLI framework                        |
| OpenAI API (gpt-4o-mini) | Pattern extraction & code generation |
| Pydantic                 | Data validation                      |
| GitPython                | Git history mining                   |
| python-dotenv            | Environment configuration            |

---

# 📂 Project Structure

```text
AI Pair-Programmer with Memory/
│
├── src/
│   │
│   ├── engine/
│   │   ├── __init__.py
│   │   └── suggestion_engine.py
│   │
│   ├── eval/
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   └── scenarios.py
│   │
│   ├── extractor/
│   │   ├── __init__.py
│   │   └── pattern_extractor.py
│   │
│   ├── memory/
│   │   ├── __init__.py
│   │   ├── decay.py
│   │   ├── schemas.py
│   │   └── store.py
│   │
│   ├── __init__.py
│   ├── code_scanner.py
│   ├── config.py
│   ├── conftest.py
│   ├── git_miner.py
│   ├── main.py
│   └── run_tests.py
│
├── tests/
│   ├── integration/
│   │   └── test_memory_store.py
│   │
│   └── unit/
│       ├── test_decay.py
│       └── test_pattern_extractor.py
│
├── .ai-memory-example/
│   ├── conventions.json
│   ├── mistakes.json
│   └── patterns.json
│
├── .env.example
├── .gitignore
├── poetry.lock
├── pyproject.toml
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Khayal07/AI-Pair-Programmer-with-Memory
cd "AI Pair-Programmer with Memory"
```

Install dependencies using Poetry:

```bash
poetry install
```

Or using pip:

```bash
pip install -r requirements.txt
```

---

# ⚙️ Environment Variables

Copy the example environment file.

```bash
cp .env.example .env
```

Configure your API key.

```env
OPENAI_API_KEY=your_api_key
MODEL_NAME=gpt-4o-mini
```

> **Note:** Never commit your `.env` file or API keys to GitHub.

---

# 💻 CLI Usage

## Learn from Git History

Analyze your latest commits and extract coding patterns.

```bash
python src/main.py scan --limit 5
```

---

## Show Active Memory

Display the habits currently remembered by the AI.

```bash
python src/main.py memory-list
```

---

## Generate Personalized Code

Generate code based on your personal coding style.

```bash
python src/main.py suggest "Create a function to calculate memory decay" --filepath src/memory/decay.py
```

---

# 🔄 Workflow

```text
User Command
      │
      ▼
Read Git History
      │
      ▼
Extract Coding Patterns
      │
      ▼
Store Memory
      │
      ▼
Apply Memory Decay
      │
      ▼
Retrieve Active Memory
      │
      ▼
Generate Personalized Code
```

---

# 🧪 Running Tests

Run the complete test suite.

```bash
python src/run_tests.py
```

The project includes tests for:

* ✅ Memory persistence
* ✅ Memory decay
* ✅ Pattern extraction
* ✅ Suggestion engine
* ✅ Integration tests

---

# 🎯 Future Improvements

* Semantic vector memory
* VS Code Extension
* Local LLM support
* Multi-language support
* RAG-enhanced memory retrieval
* Memory visualization dashboard
* Advanced memory scoring

---

# 👨‍💻 Author

Built as an **AI Engineering** project demonstrating:

* Git History Mining
* Long-Term Memory
* Memory Decay
* LLM-based Pattern Extraction
* Personalized AI Code Generation
* Context-Aware Developer Assistance
