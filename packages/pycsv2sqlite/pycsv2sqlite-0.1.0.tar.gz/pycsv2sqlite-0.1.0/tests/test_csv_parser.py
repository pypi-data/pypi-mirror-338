import pytest
import pandas as pd
from pathlib import Path
from pycsv2sqlite.utils.csv_parser import parse_csv, parse_tsv, parse_file

@pytest.fixture
def sample_csv(tmp_path):
    """Create a sample CSV file for testing"""
    csv_content = """col1,col2,col3
1,2.5,text1
2,3.5,text2
3,4.5,text3"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)
    return str(csv_file)

@pytest.fixture
def sample_tsv(tmp_path):
    """Create a sample TSV file for testing"""
    tsv_content = """col1\tcol2\tcol3
1\t2.5\ttext1
2\t3.5\ttext2
3\t4.5\ttext3"""
    tsv_file = tmp_path / "test.tsv"
    tsv_file.write_text(tsv_content)
    return str(tsv_file)

def test_parse_csv_basic(sample_csv):
    """Test basic CSV parsing"""
    df = parse_csv(sample_csv, delimiter=",", has_header=True)
    assert len(df) == 3
    assert list(df.columns) == ["col1", "col2", "col3"]
    assert df["col1"].dtype == "int64"
    assert df["col2"].dtype == "float64"
    assert df["col3"].dtype == "object"

def test_parse_csv_pandas_kwargs(sample_csv):
    """Test CSV parsing with pandas kwargs"""
    df = parse_csv(
        sample_csv,
        delimiter=",",
        has_header=True,
        dtype={"col1": "float64"},
        usecols=["col1", "col2"],
        na_values=["text1"]
    )
    assert list(df.columns) == ["col1", "col2"]
    assert df["col1"].dtype == "float64"
    assert df.isna().sum()["col1"] == 0

def test_parse_tsv_basic(sample_tsv):
    """Test basic TSV parsing"""
    df = parse_tsv(sample_tsv, has_header=True)
    assert len(df) == 3
    assert list(df.columns) == ["col1", "col2", "col3"]

def test_parse_file_detection(sample_csv, sample_tsv):
    """Test file format detection"""
    csv_df = parse_file(sample_csv, delimiter=",")
    tsv_df = parse_file(sample_tsv)
    
    assert len(csv_df) == len(tsv_df) == 3
    assert list(csv_df.columns) == list(tsv_df.columns)

def test_parse_csv_encoding(tmp_path):
    """Test CSV parsing with encoding"""
    content = "col1,col2\ná,é"
    csv_file = tmp_path / "utf8.csv"
    csv_file.write_text(content, encoding="utf-8")
    
    df = parse_csv(str(csv_file), encoding="utf-8")
    assert df.iloc[0, 0] == "á"

def test_parse_csv_skiprows(sample_csv):
    """Test CSV parsing with row skipping"""
    df = parse_csv(sample_csv, skiprows=1)
    assert len(df) == 2


def test_parse_file_invalid():
    pass