def calculate_similarity(baseline_code: str, memory_code: str) -> float:
    """
    Yaddaşsız (baseline) və yaddaşlı modelin nəticələri arasındakı Jaccard oxşarlığını hesablayır.
    """
    base_words = set(baseline_code.split())
    mem_words = set(memory_code.split())
    
    if not base_words or not mem_words:
        return 0.0
        
    intersection = base_words.intersection(mem_words)
    union = base_words.union(mem_words)
    
    return len(intersection) / len(union)