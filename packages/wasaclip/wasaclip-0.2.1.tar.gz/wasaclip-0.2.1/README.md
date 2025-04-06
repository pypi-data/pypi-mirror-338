# WasaClip 🌶️✂️

WasaClip takes your clipboard entries and gives them a spicy refresh! Trim, replace, reformat, or clean up text with lightning speed. Just copy, let WasaClip process it, and paste the perfect result—sharp, clean, and ready to go. Whether you're editing code, removing extra spaces, or transforming text, WasaClip makes it effortless.

![WasaClip](https://raw.githubusercontent.com/rotten77/wasaclip/main/wasaclip.png)

## Install

    pip install wasaclip

## How to Use WasaClip

Create a processor file (e.g., `my_processor.py`) with a process function.

Run WasaClip and pass the processor file as an argument:

    wasaclip my_processor.py

## Processors

The processor file should contain a process function that:

* Takes a string argument (the clipboard content).
* Returns either a string (the processed content) or None (to skip processing).
* Can import and use any Python libraries.
* May include additional helper functions if needed.

**Check the [examples](https://github.com/rotten77/wasaclip/tree/main/examples) folder🌶️**

*Example:*

    # lowercase.py
    def process(content: str) -> str:
        return f"{content.lower()}"