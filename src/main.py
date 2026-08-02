import typer
from pathlib import Path
from typing import Optional

from src.git_miner import GitMiner
from src.extractor.pattern_extractor import PatternExtractor
from src.memory.store import MemoryStore
from src.engine.suggestion_engine import SuggestionEngine

app = typer.Typer(help="AI Pair-Programmer with Memory CLI")

@app.command("scan")
def scan(limit: int = typer.Option(5, help="Neçə son commit analiz edilsin?")):
    """Git tarixçəsini oxuyur və yeni kodlama vərdişlərini çıxarır."""
    typer.echo(f"Son {limit} commit analiz edilir...")
    
    miner = GitMiner()
    extractor = PatternExtractor()
    store = MemoryStore()
    
    commits = miner.get_recent_commits(limit=limit)
    if not commits:
        typer.echo("Git repozitoriyası tapılmadı və ya commit yoxdur.")
        raise typer.Exit()
        
    total_extracted = 0
    
    for commit in commits:
        diff_text = miner.get_diff_from_commit(commit)
        if diff_text:
            patterns = extractor.extract_from_diff(diff_text)
            for p in patterns:
                store.add_or_update_pattern(p)
                typer.echo(f"Tapıldı/Yeniləndi: [{p.category}] {p.title}")
                total_extracted += 1
                
    typer.echo(f"\nSkan bitdi! Cəmi {total_extracted} pattern emal edildi.")

@app.command("suggest")
def suggest(
    prompt: str = typer.Argument(..., help="Nə etmək istəyirsiniz?"),
    filepath: Optional[Path] = typer.Option(None, help="Üzərində işlədiyiniz faylın yolu")
):
    """Kontekst və yaddaş əsasında kod təklifi verir."""
    current_code = ""
    if filepath and filepath.exists():
        current_code = filepath.read_text(encoding="utf-8")
        
    typer.echo("Yaddaş yoxlanılır və AI-dan təklif alınır...\n")
    
    engine = SuggestionEngine()
    suggestion = engine.generate_suggestion(current_code=current_code, user_prompt=prompt)
    
    typer.echo("-" * 40)
    typer.echo(suggestion)
    typer.echo("-" * 40)

@app.command("memory-list")
def memory_list(threshold: float = typer.Option(0.25, help="Minimum aktuallıq balı (decay threshold)")):
    """Aktiv yaddaş vərdişlərini siyahıya alır."""
    store = MemoryStore()
    active = store.get_active_patterns(threshold=threshold)
    
    if not active:
        typer.echo("Hələ ki aktiv vərdiş tapılmadı və ya hamısının balı kritik həddən aşağıdır.")
        raise typer.Exit()
        
    typer.echo(f"Cəmi {len(active)} aktiv vərdiş:\n")
    for item in active:
        p = item["pattern"]
        score = item["relevance_score"]
        typer.echo(f"- [{score:.2f}] {p.title} (Tezlik: {p.frequency_count})")

if __name__ == "__main__":
    app()