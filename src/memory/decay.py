from datetime import datetime, timezone
import math
from .schemas import MemoryPattern

def calculate_decay_score(
    pattern: MemoryPattern,
    decay_rate: float = 0.05,
    alpha: float = 0.1
) -> float:
    """
    S(t) = w_0 * exp(-lambda * delta_t) + alpha * ln(1 + f)
    """
    now = datetime.now(timezone.utc)
    
    # Əgər datetime timezone-aware deyilsə, onu UTC edək
    last_seen = pattern.last_seen
    if last_seen.tzinfo is None:
        last_seen = last_seen.replace(tzinfo=timezone.utc)

    delta_t_days = (now - last_seen).total_seconds() / (24 * 3600)
    if delta_t_days < 0:
        delta_t_days = 0

    # Baza çəkisinin zəifləməsi (Base weight decay)
    decay_factor = math.exp(-decay_rate * delta_t_days)
    base_score = pattern.weight * decay_factor

    # Tezlik üzrə gücləndirici (Frequency reinforcement)
    frequency_bonus = alpha * math.log(1 + pattern.frequency_count)

    total_score = base_score + frequency_bonus
    return round(total_score, 4)