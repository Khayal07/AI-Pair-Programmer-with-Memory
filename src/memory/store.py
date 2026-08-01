import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime, timezone

from .schemas import MemoryPattern
from .decay import calculate_decay_score

class MemoryStore:
    def __init__(self, memory_dir: str = ".ai-memory"):
        self.memory_dir = Path(memory_dir)
        self.patterns_file = self.memory_dir / "patterns.json"
        self._ensure_dir()

    def _ensure_dir(self):
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        if not self.patterns_file.exists():
            self.patterns_file.write_text("[]", encoding="utf-8")

    def load_patterns(self) -> List[MemoryPattern]:
        try:
            data = json.loads(self.patterns_file.read_text(encoding="utf-8"))
            return [MemoryPattern(**item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_patterns(self, patterns: List[MemoryPattern]):
        # Pydantic model_dump ilə obyektləri JSON formatına salırıq
        data = [p.model_dump(mode="json") for p in patterns]
        self.patterns_file.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

    def get_active_patterns(self, threshold: float = 0.25) -> List[Dict]:
        """
        Kritik baldan (threshold) yuxarı olan aktiv pattern-ləri qaytarır.
        """
        patterns = self.load_patterns()
        active_patterns = []
        
        for p in patterns:
            score = calculate_decay_score(p)
            if score >= threshold:
                active_patterns.append({
                    "pattern": p,
                    "relevance_score": score
                })
        
        # Ən uyğun olanları ən üstdə tutmaq üçün (descending order)
        active_patterns.sort(key=lambda x: x["relevance_score"], reverse=True)
        return active_patterns

    def add_or_update_pattern(self, new_pattern: MemoryPattern):
        patterns = self.load_patterns()
        
        for i, p in enumerate(patterns):
            if p.id == new_pattern.id:
                # Köhnə pattern tapıldı, yeniləyirik
                p.frequency_count += 1
                p.last_seen = datetime.now(timezone.utc)
                if new_pattern.example_snippet:
                    p.example_snippet = new_pattern.example_snippet
                patterns[i] = p
                self.save_patterns(patterns)
                return
        
        # Tapılmadısa, yenisini əlavə edirik
        patterns.append(new_pattern)
        self.save_patterns(patterns)