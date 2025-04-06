def process(content: str) -> str:
    """
    Example processor that converts text to uppercase and adds a prefix.
    
    Args:
        content: The clipboard content to process
        
    Returns:
        Processed string or None if processing should be skipped
    """
    # Skip empty strings
    if not content.strip():
        return None
        
    # Process the content
    result = f"{content.upper()}"
    return result