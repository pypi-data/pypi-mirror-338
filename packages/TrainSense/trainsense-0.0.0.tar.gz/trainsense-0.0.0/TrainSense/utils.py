def validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} doit être positif.")
    return True

def print_section(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}\n")