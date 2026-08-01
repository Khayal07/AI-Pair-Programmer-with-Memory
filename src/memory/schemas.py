from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional

def _now_utc():
    return datetime.now(timezone.utc)

class MemoryPattern(BaseModel):
    id: str
    category: str
    title: str
    description: str
    example_snippet: Optional[str] = None
    weight: float = Field(default=1.0, ge=0.0)
    frequency_count: int = Field(default=1, ge=1)
    first_seen: datetime = Field(default_factory=_now_utc)
    last_seen: datetime = Field(default_factory=_now_utc)