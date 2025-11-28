def normalize_data(raw_data):
    """
    normalizes a list of numbers to a range between 0 and 1 using min-max scaling.
    logic: (x - min) / (max - min)
    """
    if not raw_data:
        raise ValueError("Input list cannot be empty")
        
    # validation: ensure all inputs are numbers
    clean_data = []
    for item in raw_data:
        if not isinstance(item, (int, float)):
             raise TypeError(f"Invalid data type found: {item} ({type(item)})")
        clean_data.append(item)

    min_val = min(clean_data)
    max_val = max(clean_data)
    
    # edge case: if all numbers are the same, avoid division by zero
    if min_val == max_val:
        return [0.0] * len(clean_data)
        
    # apply min-max normalization
    normalized = [(x - min_val) / (max_val - min_val) for x in clean_data]
    return normalized