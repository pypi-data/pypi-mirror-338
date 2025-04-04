import os
import logging
import chardet
import typer
import json
from datetime import datetime
from pathlib import Path
from typing import List
from rich import print
from rich.console import Console
from collections import defaultdict

DEFAULT_EXCLUDES = {"vcpkg_installed", ".git", ".vs"}

def is_excluded_dir(path: Path, base: Path, exclude_dirs: List[str]) -> bool:
    rel = path.relative_to(base).as_posix()
    if any(rel == e or rel.startswith(e + "/") for e in exclude_dirs):
        return True
    if path.name.startswith("."):
        return True
    return False

app = typer.Typer()
console = Console()

log_filename = f"encoding_conversion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Summary:
    def __init__(self):
        self.total_files = 0
        self.already_utf8 = 0
        self.converted = 0
        self.skipped = 0
        self.details = []
        self.errors = 0
        self.encoding_counts = defaultdict(int)

    def to_dict(self):
        return {
            "total_files": self.total_files,
            "already_utf8": self.already_utf8,
            "converted": self.converted,
            "skipped": self.skipped,
            "errors": self.errors,
            "encoding_counts": dict(self.encoding_counts),
            "details": self.details
        }

def detect_encoding(filepath: Path) -> str:
    with open(filepath, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def convert_to_utf8(filepath: Path, dry_run: bool, summary: Summary, skip_ascii: bool = False):
    summary.total_files += 1
    encoding = detect_encoding(filepath)
    if encoding:
        summary.encoding_counts[encoding] += 1

    if encoding is None:
        summary.skipped += 1
        summary.details.append({"file": str(filepath), "status": "skipped", "reason": "undetectable"})
        logging.warning(f"Could not detect encoding for {filepath}")
        return

    if skip_ascii and encoding.lower() == 'ascii':
        summary.skipped += 1
        summary.details.append({"file": str(filepath), "status": "skipped", "reason": "ascii skipped"})
        logging.info(f"Skipped ASCII file: {filepath}")
        return

    if encoding.lower() == 'utf-8':
        summary.already_utf8 += 1
        summary.details.append({"file": str(filepath), "status": "utf-8"})
        logging.info(f"{filepath} is already UTF-8.")
        return

    if dry_run:
        summary.converted += 1
        summary.details.append({"file": str(filepath), "status": "dry-run", "original_encoding": encoding})
        logging.info(f"[Dry Run] Would convert {filepath} from {encoding} to UTF-8.")
        return

    try:
        with open(filepath, 'r', encoding=encoding, errors='replace') as f:
            content = f.read()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        summary.converted += 1
        summary.details.append({"file": str(filepath), "status": "converted", "original_encoding": encoding})
        logging.info(f"Converted {filepath} from {encoding} to UTF-8.")
    except Exception as e:
        summary.errors += 1
        summary.details.append({"file": str(filepath), "status": "error", "reason": str(e)})
        logging.error(f"Failed to convert {filepath}: {e}")

def process_directory(directory: Path, dry_run: bool, summary: Summary, extensions: List[str], exclude_dirs: List[str], skip_ascii: bool):
    for root, dirs, files in os.walk(directory):
        root_path = Path(root)
        dirs[:] = [d for d in dirs if not is_excluded_dir(root_path / d, directory, exclude_dirs)]
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                filepath = Path(root) / file
                convert_to_utf8(filepath, dry_run=dry_run, summary=summary, skip_ascii=skip_ascii)

def print_summary(summary: Summary, dry_run: bool):
    from rich.table import Table
    console.print("\n[bold underline]Summary Report[/]\n")
    console.print(f"[cyan]Total files scanned  :[/] {summary.total_files}")
    console.print(f"[green]Already UTF-8     :[/] {summary.already_utf8}")
    console.print(f"[yellow]{'Would be converted' if dry_run else 'Converted'} :[/] {summary.converted}")
    console.print(f"[red]Skipped (ignored):[/] {summary.skipped}")
    console.print(f"[bold red]Errors (exceptions):[/] {summary.errors}")

    table = Table(title="Original Encodings Summary")
    table.add_column("Encoding", style="cyan")
    table.add_column("Count", style="magenta")
    for enc, count in sorted(summary.encoding_counts.items(), key=lambda x: -x[1]):
        table.add_row(enc, str(count))
    console.print(table)

    logging.info(f"Summary: Total={summary.total_files}, UTF-8={summary.already_utf8}, "
                 f"{'WouldConvert' if dry_run else 'Converted'}={summary.converted}, "
                 f"Skipped={summary.skipped}, Errors={summary.errors}")

    logging.info("--- Summary Report ---")
    

@app.command()
def convert(
    directory: Path = typer.Argument(..., help="Directory to scan for source files"),
    dry_run: bool = typer.Option(False, help="Preview changes without modifying files"),
    json_output: Path = typer.Option(None, help="Optional path to save summary report as JSON"),
    extensions: List[str] = typer.Option([".cpp", ".h", ".hpp"], help="Additional file extensions to process"),
    exclude_dirs: List[str] = typer.Option(None, help="Relative subdirectories to exclude from processing"),
    skip_ascii: bool = typer.Option(False, help="Skip files detected as ASCII encoding")
):
    if not directory.is_dir():
        print(f"[red]Error: Provided path is not a directory: {directory}[/]")
        raise typer.Exit(code=1)

    console.print(f"{'[bold yellow]Dry-running[/]' if dry_run else '[bold green]Converting[/]'} files in: [blue]{directory}[/]")

    summary = Summary()
    process_directory(
        directory,
        dry_run=dry_run,
        summary=summary,
        extensions=extensions,
        exclude_dirs=(exclude_dirs or list(DEFAULT_EXCLUDES)),
        skip_ascii=skip_ascii
    )
    print_summary(summary, dry_run)

    if json_output:
        try:
            with open(json_output, 'w', encoding='utf-8') as f:
                json.dump(summary.to_dict(), f, indent=2, ensure_ascii=False)
            console.print(f"[blue]Summary written to[/] {json_output}")
        except Exception as e:
            console.print(f"[red]Failed to write JSON summary:[/] {e}")

def main():
    app()

if __name__ == "__main__":
    main()
