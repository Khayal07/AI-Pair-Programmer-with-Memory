from extractor.pattern_extractor import PatternExtractor

def test_extractor_initialization():
    # Extractor-un düzgün API açarı və model ilə inisializasiya olunduğunu yoxlayırıq
    extractor = PatternExtractor()
    assert extractor.client is not None
    # assert extractor.model_name == "gpt-4o-mini"  