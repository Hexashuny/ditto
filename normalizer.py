# -*- coding: utf-8 -*-
import re

def normalize_line(line: str) -> str:
    """
    Normalize a line by:
    - stripping leading/trailing whitespace
    - removing trailing punctuation like ., â€¦, â€¢
    - converting to lowercase
    """
    if not line:
        return ""
    line = line.strip()
    # Remove dots, bullets, ellipsis safely in UTF-8
    line = re.sub(r'[.\u2022\u2026]+$', '', line)
    return line.lower()
