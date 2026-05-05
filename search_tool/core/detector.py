def detect_type(value):
    if "@" in value:
        return "email"
    elif value.replace("+", "").isdigit():
        return "phone"
    elif "." in value:
        return "domain"
    elif " " in value:
        return "name"
    return "unknown"