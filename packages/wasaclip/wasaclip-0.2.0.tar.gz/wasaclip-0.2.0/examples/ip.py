import re

def process(content: str) -> str:
    """
    Extracts all IP addreses from the text and joins them.
    
    Args:
        content: The clipboard content to process
        
    Returns:
        Extracted IP addreses or None if no numbers found
    """
    ips = re.findall(r'(?:(?:\d{1,3}\.){3}\d{1,3})', content)
    if ips:
        return ' '.join(ips)