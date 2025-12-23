import os
import csv
import pandas as pd
import pytest

def test_output_exists():
    assert os.path.exists('/app/output.csv'), "Output file /app/output.csv not found"

def test_csv_content():
    df = pd.read_csv('/app/output.csv')
    
    # Check headers
    expected_headers = ['name', 'email']
    assert list(df.columns) == expected_headers, f"Expected headers {expected_headers}, got {list(df.columns)}"
    
    # Check data content
    # Based on input.json: 12 users are active.
    expected_names = ["John Doe", "Mike Ross", "Rachel Zane", "Donna Paulsen", "Jessica Pearson", "Katrina Bennett", "Samantha Wheeler", "Sheila Sazs", "Gretchen Bodinski", "Harold Gunderson", "Benjamin Sisko", "Odo Constable"]
    actual_names = df['name'].tolist()
    
    assert len(actual_names) == 12, f"Expected 12 active users, found {len(actual_names)}"
    for name in expected_names:
        assert name in actual_names, f"User {name} should be in the output"

def test_no_inactive_users():
    df = pd.read_csv('/app/output.csv')
    inactive_names = ["Jane Smith", "Harvey Specter"]
    actual_names = df['name'].tolist()
    
    for name in inactive_names:
        assert name not in actual_names, f"Inactive user {name} should NOT be in the output"
