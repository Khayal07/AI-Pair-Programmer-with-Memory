import os
from dotenv import load_dotenv

# .env faylındakı dəyişənləri yükləyirik
load_dotenv()

# Əsas API Açarımız
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Yaddaş fayllarının saxlanılacağı qovluq
MEMORY_DIR = os.getenv("MEMORY_DIR", ".ai-memory")

# Günlük zəifləmə əmsalı
DECAY_RATE = float(os.getenv("DECAY_RATE", "0.05"))