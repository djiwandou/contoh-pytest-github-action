from src.uppercase import convert_uppercase
# not parameterized
def test_convert_uppercase_empty_string():
    assert convert_uppercase("") == ""

def test_convert_uppercase_string():
    assert convert_uppercase("ini") == "INI"

def test_convert_uppercase_single_character():
    assert convert_uppercase("a") == "A"

def test_convert_uppercase_mixed_casing():
    assert convert_uppercase("Bob") == "BOB"

def test_convert_uppercase_with_spaces():
    assert convert_uppercase("never give up") == "NEVER GIVE UP"

def test_convert_uppercase_with_punctuation():
    assert convert_uppercase("Do you see God?") == "DO YOU SEE GOD?"

def test_convert_abnormal_characters():
    assert convert_uppercase("?#%") == "?#%"