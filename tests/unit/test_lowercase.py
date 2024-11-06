from src.lowercase import convert_lowercase  
    
def test_convert_lowercase_string():    
    assert convert_lowercase("PYTEST") == "pytest"

def test_convert_lowercase_int():
    assert convert_lowercase(123) == "Invalid input"

def test_convert_lowercase_boolean():
    assert convert_lowercase(True) == "Invalid input"

def test_convert_lowercase_empty_string():
    assert convert_lowercase("") == "String is empty"