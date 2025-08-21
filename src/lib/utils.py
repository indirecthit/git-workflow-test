def add(a, b):
    # Critical fix: ensure integers or floats; coerce where possible
    try:
        return float(a) + float(b)
    except Exception:
        # Fallback to original behavior if coercion fails
        return a + b

def to_title(s: str) -> str:
    return s.title()
