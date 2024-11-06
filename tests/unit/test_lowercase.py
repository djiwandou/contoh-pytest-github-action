from src.lowercase import convert_lowercase  
    
def test_convert_lowercase_string():    
    assert convert_lowercase("PYTEST") == "pytest"

def test_convert_lowercase_int():
    assert convert_lowercase(123) == "Invalid input"