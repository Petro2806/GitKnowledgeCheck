"""Text utilities."""

def normalize_spaces(s: str) -> str:
    # collapse consecutive whitespace to single spaces
    parts = s.split()
    return " ".join(parts)

def slugify(s: str) -> str:
    s = normalize_spaces(s).lower()
    out = []
    for ch in s:
        if ch.isalnum():
            out.append(ch)
        elif ch in (" ", "-", "_"):
            out.append("-")
    # remove duplicate dashes
    result = []
    prev_dash = False
    for ch in out:
        if ch == "-":
            if not prev_dash:
                result.append(ch)
            prev_dash = True
        else:
            result.append(ch)
            prev_dash = False
    return "".join(result).strip("-")
