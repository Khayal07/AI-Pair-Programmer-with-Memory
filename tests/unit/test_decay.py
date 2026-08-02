from datetime import datetime, timezone, timedelta
from memory.schemas import MemoryPattern
from memory.decay import calculate_decay_score

def test_decay_score_calculation():
    # Yeni yaranmış pattern
    pattern = MemoryPattern(
        id="test_pattern",
        category="test",
        title="Test Pattern",
        description="Just for testing",
        weight=1.0,
        frequency_count=1
    )
    
    # İndiki vaxtda score yoxlanılır (0 gün keçib)
    score_now = calculate_decay_score(pattern, decay_rate=0.05, alpha=0.1)
    
    # 10 gün əvvələ qaytaraq
    pattern.last_seen = datetime.now(timezone.utc) - timedelta(days=10)
    score_10_days = calculate_decay_score(pattern, decay_rate=0.05, alpha=0.1)
    
    # Zəifləmə baş verməlidir
    assert score_10_days < score_now

def test_frequency_increases_score():
    pattern = MemoryPattern(
        id="freq_test",
        category="test",
        title="Freq Test",
        description="Just for testing",
        weight=1.0,
        frequency_count=1
    )
    score_low_freq = calculate_decay_score(pattern)
    
    pattern.frequency_count = 10
    score_high_freq = calculate_decay_score(pattern)
    
    # Çox istifadə olunanın balı daha yüksək olmalıdır
    assert score_high_freq > score_low_freq