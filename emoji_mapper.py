#!/usr/bin/env python3
"""EmojiMapper – a tiny CLI utility to replace words with emojis.

Supported mappings are defined in the EMOJI_MAP dictionary. Extend it as you like.
"""
import sys

EMOJI_MAP = {
    "love": "❤️",
    "coffee": "☕️",
    "pizza": "🍕",
    "cat": "🐱",
    "dog": "🐶",
    "happy": "😊",
    "sad": "😢",
    "fire": "🔥",
    "star": "⭐️",
}

def replace_words(text: str) -> str:
    words = text.split()
    return " ".join(EMOJI_MAP.get(w.lower(), w) for w in words)

def main():
    if len(sys.argv) < 2:
        print("Usage: python emoji_mapper.py <your text>")
        sys.exit(1)
    input_text = " ".join(sys.argv[1:])
    print(replace_words(input_text))

if __name__ == "__main__":
    main()
