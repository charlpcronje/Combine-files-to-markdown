# file_analysis.py

import os
import re

def count_words_and_tokens(text):
    words = text.split()
    tokens = re.findall(r'\b\w+\b', text)
    return len(words), len(tokens)

def analyze_file_contents(contents):
    line_count = contents.count('\n') + 1
    word_count, token_count = count_words_and_tokens(contents)
    return line_count, word_count, token_count

def generate_analysis_report(file_paths):
    report = "## Analysis Report\n\n"
    total_lines, total_words, total_tokens = 0, 0, 0

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
        
        line_count, word_count, token_count = analyze_file_contents(contents)
        report += f"- **File**: {os.path.basename(file_path)}\n"
        report += f"  - **Lines**: {line_count}\n"
        report += f"  - **Words**: {word_count}\n"
        report += f"  - **Tokens**: {token_count}\n\n"

        total_lines += line_count
        total_words += word_count
        total_tokens += token_count

    report += "## Total Counts Across All Files\n"
    report += f"- **Total Lines**: {total_lines}\n"
    report += f"- **Total Words**: {total_words}\n"
    report += f"- **Total Tokens**: {total_tokens}\n"

    return report