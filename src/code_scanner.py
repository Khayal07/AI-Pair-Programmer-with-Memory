from pathlib import Path
from typing import List

class CodeScanner:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)

    def get_python_files(self) -> List[Path]:
        """Layihədəki virtual environment (venv) xaricindəki bütün Python fayllarını tapır."""
        files = []
        for path in self.root_dir.rglob("*.py"):
            if ".venv" not in str(path) and "__pycache__" not in str(path):
                files.append(path)
        return files
        
    def read_file(self, file_path: Path) -> str:
        """Faylın məzmununu oxuyub qaytarır."""
        if file_path.exists():
            return file_path.read_text(encoding="utf-8")
        return ""