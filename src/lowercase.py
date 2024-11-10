def convert_lowercase(s):
    if not s: 
        return "String is empty"
    if not isinstance(s, str):
        return "Invalid input"
    return s.lower()