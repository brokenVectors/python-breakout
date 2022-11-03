def clamp(num, min_value, max_value):
    num = max(min(num, max_value), min_value)
    return num