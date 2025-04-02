def parse_list_strings(input_string):
    """
    Converts a comma-separated string into a cleaned list of values.

    Args:
        input_string (str): A string of comma-separated values.

    Returns:
        list: A list of trimmed, non-empty strings.
    """
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")
    
    return [item.strip() for item in input_string.split(",") if item.strip()]