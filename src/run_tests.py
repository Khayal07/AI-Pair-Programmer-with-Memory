import sys
import os
import pytest

# Əsas qovluğu və xüsusilə 'src' qovluğunu Python-un axtarış yoluna əlavə edirik
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, "src")

# Hər iki yolu sistemə tanıdırıq
sys.path.insert(0, src_dir)
sys.path.insert(0, current_dir)

if __name__ == "__main__":
    print(f"Testlər bu qovluqdan işə salınır: {current_dir}")
    print("-" * 50)
    # Pytest-i çağırırıq
    sys.exit(pytest.main(["tests/"]))