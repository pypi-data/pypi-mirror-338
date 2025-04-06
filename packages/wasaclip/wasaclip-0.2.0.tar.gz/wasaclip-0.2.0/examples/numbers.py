import re

def process(content: str) -> str:
    """
    Extracts all numbers from the text and joins them.
    
    Args:
        content: The clipboard content to process
        
    Returns:
        Extracted numbers or None if no numbers found
    """
    numbers = re.findall(r'\d+(?:\.\d+)?', content)
    if numbers:
        return ' '.join(numbers)
    return None