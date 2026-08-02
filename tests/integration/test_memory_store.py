import tempfile
from memory.store import MemoryStore
from memory.schemas import MemoryPattern

def test_store_add_and_update():
    with tempfile.TemporaryDirectory() as temp_dir:
        store = MemoryStore(memory_dir=temp_dir)
        
        pattern = MemoryPattern(
            id="test_store",
            category="test",
            title="Test Store",
            description="Integration test for store"
        )
        
        # Əlavə etmə
        store.add_or_update_pattern(pattern)
        patterns = store.load_patterns()
        assert len(patterns) == 1
        assert patterns[0].frequency_count == 1
        
        # Yeniləmə (Eyni ID ilə)
        store.add_or_update_pattern(pattern)
        patterns_updated = store.load_patterns()
        assert len(patterns_updated) == 1
        assert patterns_updated[0].frequency_count == 2