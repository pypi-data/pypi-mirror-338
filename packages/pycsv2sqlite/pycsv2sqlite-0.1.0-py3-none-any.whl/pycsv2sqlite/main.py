import typer
import pandas as pd
from datetime import datetime
from pathlib import Path
from pycsv2sqlite.utils.csv_parser import parse_csv
from pycsv2sqlite.utils.sqlite_handler import export_to_sqlite


app = typer.Typer()

@app.command()
def import_data(
    input_path: str = typer.Argument(..., help="Path to the input CSV/TSV file or directory."),
    delimiter: str = typer.Option(",", help="Delimiter used in the input file(s)."),
    has_headers: bool = typer.Option(True, help="Whether input file(s) have headers. If False, will use col0, col1, etc."),
    db_file: str = typer.Option(f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.sqlite3", help="Output SQLite database file name.")
):
    """Import data from CSV/TSV file(s) into an SQLite database."""
    
    path = Path(input_path)
    total_records = 0
    
    # Define pandas read options
    pd_options = {
        'delimiter': delimiter,
        'header': 0 if has_headers else None,  # Use first row as headers if has_headers=True
    }
    
    if path.is_file():
        # Single file processing
        df = parse_csv(str(path), **pd_options)
        export_to_sqlite(df, db_file)
        total_records = len(df)
    
    elif path.is_dir():
        # Directory processing
        csv_files = list(path.glob("*.[ct]sv"))
        # gzipped files
        csv_files += list(path.glob("*.gz"))
        # Check if any CSV/TSV files are found
        if not csv_files:
            typer.echo("No CSV/TSV files found in the directory.")
            raise typer.Exit(1)
        
        for file in csv_files:
            typer.echo(f"Processing {file.name}...")
            df = parse_csv(str(file), **pd_options)
            export_to_sqlite(df, db_file, table_name=path.stem)
            total_records += len(df)
    
    else:
        typer.echo("The specified path does not exist.")
        raise typer.Exit(1)
    
    typer.echo(f"Successfully imported {total_records} records into {db_file}.")
    typer.echo(f"Processed {1 if path.is_file() else len(csv_files)} file(s).")

if __name__ == "__main__":
    app()