import time
import pyperclip
import importlib.util
import argparse
from typing import Optional, Callable
from colorama import Fore, Style
import sys
import os
from importlib.metadata import version
__version__ = version("wasaclip")

class WasaClip:
    def __init__(self, processor_function: Callable[[str], Optional[str]], interval: float = 0.5):
        """
        Initialize the clipboard monitor.
        
        Args:
            processor_function: Function that processes clipboard content
            interval: How often to check clipboard (in seconds)
        """
        self.processor_function = processor_function
        self.interval = interval
        self.previous_content: Optional[str] = None
        self.previous_processed: Optional[str] = None
        
    def process_clipboard(self, content: str) -> Optional[str]:
        """Process the clipboard content using the provided processor function."""
        try:
            result = self.processor_function(content)
            # Convert result to string if it's not None
            return str(result) if result is not None else None
        except Exception as e:
            print(Fore.RED+f"Error processing clipboard content: {e}"+Style.RESET_ALL)
            return None
    
    def run(self):
        """Start monitoring the clipboard."""
        print(Fore.YELLOW+f"┌───────────────────────────────┐")
        print(Fore.YELLOW+f"  WasaClip {__version__}")
        print(Fore.YELLOW+f"└───────────────────────────────┘")
        print("")
        print(Fore.MAGENTA+"Monitoring clipboard...")
        print(Fore.RED+"Press Ctrl+C to stop")
        print("")
        print(Fore.LIGHTWHITE_EX+"------------------------------------"+Style.RESET_ALL)

        try:
            while True:
                current_content = pyperclip.paste()
                
                # Only process if content is new (different from both previous content and previous processed)
                if (current_content != self.previous_content and 
                    current_content != self.previous_processed and 
                    current_content is not None):
                    
                    processed_content = self.process_clipboard(current_content)
                    
                    # Only update clipboard if processing was successful
                    if processed_content is not None:
                        pyperclip.copy(processed_content)
                        print(f"{Fore.CYAN+'Original:'} {Style.RESET_ALL+current_content}")
                        print(f"{Fore.GREEN+'Processed:'} {Style.RESET_ALL+processed_content}")
                        print(Fore.LIGHTWHITE_EX+"------------------------------------"+Style.RESET_ALL)
                    
                    self.previous_content = current_content
                    self.previous_processed = processed_content
                
                time.sleep(self.interval)
                
        except KeyboardInterrupt:
            print(Fore.RED+"\nStopping clipboard monitor"+Style.RESET_ALL)

def load_processor(file_path: str) -> Callable[[str], Optional[str]]:
    """
    Load the processor function from a Python file.
    
    The file should contain a function named 'process' that takes a string
    and returns either a string or None.
    """
    try:
        # Get the absolute path
        abs_path = os.path.abspath(file_path)
        
        # Load the module
        spec = importlib.util.spec_from_file_location("processor", abs_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not load processor from {file_path}")
            
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Check if process function exists
        if not hasattr(module, 'process'):
            raise AttributeError(
                f"The processor file must contain a 'process' function that takes "
                f"a string argument and returns a string or None"
            )
        
        return module.process
        
    except Exception as e:
        print(Fore.RED+f"Error loading processor file: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Monitor the clipboard and process its contents.')
    parser.add_argument('processor_file', help='Python file containing the processor function')
    parser.add_argument('--interval', type=float, default=0.5, 
                       help='Clipboard check interval in seconds (default: 0.5)')
    
    args = parser.parse_args()
    
    # Load the processor function
    processor = load_processor(args.processor_file)
    
    # Create and run the monitor
    monitor = WasaClip(
        processor_function=processor,
        interval=args.interval
    )
    monitor.run()

if __name__ == "__main__":
    main()