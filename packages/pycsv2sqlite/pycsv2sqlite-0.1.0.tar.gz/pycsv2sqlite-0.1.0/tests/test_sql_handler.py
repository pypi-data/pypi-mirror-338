import pytest
import pandas as pd
import sqlite3
from pathlib import Path
from pycsv2sqlite.utils.sqlite_handler import export_to_sqlite, get_sqlite_type
import typer

@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing"""
    return pd.DataFrame({
        'int_col': [1, 2, 3],
        'float_col': [1.1, 2.2, 3.3],
        'str_col': ['a', 'b', 'c'],
        'date_col': pd.date_range('2024-01-01', periods=3),
        'bool_col': [True, False, True]
    })

@pytest.fixture
def temp_db(tmp_path):
    """Create a temporary database file"""
    db_file = tmp_path / "test.db"
    return str(db_file)

def test_get_sqlite_type():
    """Test SQLite type mapping"""
    assert get_sqlite_type(pd.Int64Dtype()) == "INTEGER"
    assert get_sqlite_type(pd.Float64Dtype()) == "REAL"
    assert get_sqlite_type(pd.StringDtype()) == "TEXT"
    assert get_sqlite_type(pd.BooleanDtype()) == "BOOLEAN"
    assert get_sqlite_type(pd.DatetimeTZDtype(tz='UTC')) == "TIMESTAMP"

def test_export_to_sqlite_basic(sample_df, temp_db):
    """Test basic export functionality"""
    export_to_sqlite(sample_df, temp_db, "test_table")
    
    # Verify data
    conn = sqlite3.connect(temp_db)
    result = pd.read_sql("SELECT * FROM test_table", conn)
    conn.close()
    
    assert len(result) == len(sample_df)
    assert list(result.columns) == list(sample_df.columns)

def test_export_to_sqlite_schema(sample_df, temp_db):
    """Test if schema is created correctly"""
    export_to_sqlite(sample_df, temp_db, "test_table")
    
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    
    # Get table info
    schema = cursor.execute("PRAGMA table_info(test_table)").fetchall()
    conn.close()
    
    # Verify column types
    column_types = {row[1]: row[2] for row in schema}
    assert column_types['int_col'] == 'INTEGER'
    assert column_types['float_col'] == 'REAL'
    assert column_types['str_col'] == 'TEXT'
    assert column_types['date_col'] == 'TIMESTAMP'
    assert column_types['bool_col'] == 'BOOLEAN'

def test_export_to_sqlite_if_exists(sample_df, temp_db):
    """Test if_exists parameter behavior"""
    # First export
    export_to_sqlite(sample_df, temp_db, "test_table", if_exists='replace')
    
    # Second export with append
    export_to_sqlite(sample_df, temp_db, "test_table", if_exists='append')
    
    conn = sqlite3.connect(temp_db)
    count = conn.execute("SELECT COUNT(*) FROM test_table").fetchone()[0]
    conn.close()
    
    assert count == len(sample_df) * 2

def test_export_to_sqlite_invalid_path():
    """Test handling of invalid database path"""
    df = pd.DataFrame({'a': [1]})
    with pytest.raises(typer.Exit):
        export_to_sqlite(df, "/invalid/path/db.sqlite")

def test_export_to_sqlite_empty_df(temp_db):
    """Test handling of empty DataFrame"""
    df = pd.DataFrame()
    with pytest.raises(typer.Exit):
        export_to_sqlite(df, temp_db, "empty_table")