# accounts/utils/__init__.py

QUARTER_CHOICES = [
    ("jan-mar", "January - March"),
    ("apr-jun", "April - June"),
    ("jul-sep", "July - September"),
    ("oct-dec", "October - December"),
]

def get_month_range(quarter):
    mapping = {
        "jan-mar": (1, 3),
        "apr-jun": (4, 6),
        "jul-sep": (7, 9),
        "oct-dec": (10, 12),
    }
    if quarter not in mapping:
        raise ValueError(f"Invalid quarter key: {quarter}")
    return mapping[quarter]
def get_quarter_for_month(month: int):
    """Return the quarter key + label for a given month number (1–12)."""
    if 1 <= month <= 3:
        return "jan-mar", "January - March"
    elif 4 <= month <= 6:
        return "apr-jun", "April - June"
    elif 7 <= month <= 9:
        return "jul-sep", "July - September"
    elif 10 <= month <= 12:
        return "oct-dec", "October - December"
    else:
        raise ValueError(f"Invalid month: {month}")
