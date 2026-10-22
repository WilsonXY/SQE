"""Word count and wording similarity for the writing experiment.

Counting method (WRITING-EXPERIMENT-PROTOCOL.md section 8): whitespace tokens
containing a letter or digit, after removing Markdown-only delimiters, HTML
comments and link targets. Headings, captions, table cells and diagram text
count.

Usage:
    python count_words.py FILE [FILE ...]
    python count_words.py --similarity FILE_A FILE_B
"""
import difflib
import re
import sys


def strip_markdown(text):
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"\]\([^)]*\)", "]", text)  # drop link targets
    text = re.sub(r"^\s*```.*$", " ", text, flags=re.M)  # fence lines
    text = re.sub(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$", " ", text, flags=re.M)
    text = re.sub(r"[#*_`|>]", " ", text)
    return text


def count_words(text):
    return sum(1 for tok in strip_markdown(text).split() if re.search(r"[A-Za-z0-9]", tok))


def tokens(text):
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    return re.findall(r"\w+(?:['’-]\w+)*", text.lower())


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--similarity":
        a, b = tokens(read(args[1])), tokens(read(args[2]))
        ratio = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
        print(f"{ratio:.3f}\t{args[1]} vs {args[2]}")
    else:
        total = 0
        for path in args:
            n = count_words(read(path))
            total += n
            print(f"{n}\t{path}")
        if len(args) > 1:
            print(f"{total}\tTOTAL")
