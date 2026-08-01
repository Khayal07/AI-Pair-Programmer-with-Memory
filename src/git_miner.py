import git
from pathlib import Path
from typing import List

class GitMiner:
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        try:
            self.repo = git.Repo(self.repo_path)
        except git.InvalidGitRepositoryError:
            self.repo = None

    def get_recent_commits(self, limit: int = 5) -> List[git.Commit]:
        if not self.repo:
            return []
        try:
            return list(self.repo.iter_commits(max_count=limit))
        except git.GitCommandError:
            return []

    def get_diff_from_commit(self, commit: git.Commit) -> str:
        """
        Verilmiş commit ilə onun parent-i arasındakı kod dəyişikliklərini (diff) çıxarır.
        """
        if not commit.parents:
            return ""
        
        parent = commit.parents[0]
        diffs = parent.diff(commit, create_patch=True)
        
        diff_text = ""
        for d in diffs:
            # Əsasən Python və ya konfiqurasiya fayllarına köklənirik
            if d.a_path and (d.a_path.endswith('.py') or d.a_path.endswith('.sql')):
                diff_text += f"\n--- File: {d.a_path} ---\n"
                try:
                    diff_text += d.diff.decode('utf-8') + "\n"
                except Exception:
                    continue
        return diff_text