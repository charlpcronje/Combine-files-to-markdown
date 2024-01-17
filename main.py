import os
import json
import re
import nltk
import sys
from nltk.tokenize import word_tokenize

# Ensure required NLTK resources are downloaded
nltk.download('punkt')

class FileCombiner:
    def __init__(self, config_path):
        """
        Initializes the FileCombiner with a configuration file.
        - config_path: Path to the JSON configuration file.
        """
        with open(config_path, 'r') as file:
            self.config = json.load(file)
        self.combined_content = ""
        self.processed_files = []
        self.gitignore_patterns = self.load_gitignore_patterns()

    def load_gitignore_patterns(self):
        """
        Loads patterns from the .gitignore file specified in the config, if present.
        Returns a list of patterns from the .gitignore file.
        """
        gitignore_path = self.config.get('gitignore_path')
        patterns = []
        if gitignore_path and os.path.exists(gitignore_path):
            with open(gitignore_path, 'r') as file:
                patterns = file.readlines()
        return patterns

    def should_exclude(self, path, exclude_list, root_path):
        """
        Determines whether a file or directory should be excluded based on the exclude list.
        - path: The file or directory path to check.
        - exclude_list: List of paths to be excluded.
        - root_path: Root path of the directory structure.
        Returns: True if the path should be excluded, False otherwise.
        """
        abs_path = os.path.abspath(path)
        for exclude in exclude_list:
            exclude_abs_path = os.path.abspath(os.path.join(root_path, exclude))
            if abs_path.startswith(exclude_abs_path):
                return True
        return False

    def is_file_type_supported(self, file_name, supported_types):
        """
        Checks if the file extension is in the list of supported types.
        - file_name: Name of the file to check.
        - supported_types: List of supported file extensions.
        Returns: True if the file type is supported, False otherwise.
        """
        file_extension = os.path.splitext(file_name)[1]
        return file_extension in supported_types

    def process_files(self):
        """
        Processes files from the root directory, combining content from files that match
        the criteria specified in the configuration. Keeps track of processed file paths.
        """
        root_path = self.config['root_path']
        exclude_folders = self.config['exclude_folders']
        exclude_files = self.config['exclude_files']
        file_types = self.config['file_types']

        for root, dirs, files in os.walk(root_path):
            dirs[:] = [d for d in dirs if not self.should_exclude(os.path.join(root, d), exclude_folders, root_path)]
            for file in files:
                file_path = os.path.join(root, file)
                if self.should_exclude(file_path, exclude_files, root_path) or not self.is_file_type_supported(file, file_types):
                    continue
                # Check against gitignore patterns
                if any(re.match(pattern, file_path) for pattern in self.gitignore_patterns):
                    continue
                self.processed_files.append(file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    print(f'File opened for reading: {file_path}')
                    self.combined_content += f"## File: {os.path.relpath(file_path, root_path)}\n```{os.path.splitext(file)[1][1:]}\n{f.read()}\n```\n\n"

    def analyze_files(self):
        """
        Analyzes each processed file for line, word, and AI token counts.
        Returns a markdown formatted string report with analysis results for each file and overall totals.
        """
        total_lines = total_words = total_tokens = 0
        report = "## Analysis Report\n\n"

        report += "| No. | File | Lines | Words | AI Tokens |\n"
        report += "| --- | ---- | ----- | ----- | --------- |\n"

        for idx, file_path in enumerate(self.processed_files, start=1):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                lines, words, tokens = self.count_words_and_tokens(content)
                rel_path = "./" + os.path.relpath(file_path, start=self.config['root_path'])
                report += f"| {idx} | {rel_path} | {lines} | {words} | {tokens} |\n"
                total_lines += lines
                total_words += words
                total_tokens += tokens
        report += f"|  | Total | {total_lines} | {total_words} | {total_tokens} |\n\n"
        
        report += "\n## Total Counts Across All Files. Tokenizer Used: NLTK's Punkt Tokenizer\n"
        report += f"- Total Lines: {total_lines}\n"
        report += f"- Total Words: {total_words}\n"
        report += f"- Total AI Tokens: {total_tokens}\n"
        
        return report


    def count_words_and_tokens(self, text):
        """
        Counts the number of lines, words, and AI tokens in the given text.
        Args:
        - text: Text to be analyzed.
        Returns: Tuple of line count, word count, and AI token count.
        """
        lines = text.count('\n') + 1  # Counting the number of lines
        words = text.split()
        tokens = word_tokenize(text)  # NLTK's word_tokenize is used for AI tokenization
        return lines, len(words), len(tokens)


    def write_combined_file(self):
        """
        Writes the combined content of all processed files to the output file specified in the configuration.
        """
        with open(self.config['output_path'], 'w', encoding='utf-8') as output_file:
            print(f'File opened for writing: {self.config["output_path"]}')
            output_file.write(self.combined_content)


    def append_html_styles(self):
        """
        Appends HTML content for styling, including a hidden comment and style tags, 
        to the end of the Markdown file. This method assumes that the Markdown file 
        will be converted to HTML and the styles will be applied there.
        """
        html_content = """
<p id="hidden_comment">
    This is a hidden comment. It explains that the following style tag is meant to 
    style HTML content if this Markdown is converted to HTML. This comment should 
    not be visible in most Markdown renderers.
</p>
<style>
    #hidden_comment {
        display: none;
    }
    table {
        width: 100%;
    }
    table tr:first-child {
        font-weight: bold;
    }
    table tr:last-child {
        font-style: italic;
    }
</style>
"""
        return html_content
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <config.json>")
        sys.exit(1)

    file_combiner = FileCombiner(sys.argv[1])
    file_combiner.process_files()
    file_combiner.write_combined_file()

    # Perform analysis and prepend the analysis report to the combined file 
    analysis_report = file_combiner.analyze_files()
    html_content = file_combiner.append_html_styles()
    with open(file_combiner.config['output_path'], 'r+', encoding='utf-8') as file:
        combined_content = file.read()
        file.seek(0, 0)
        file.write(analysis_report + '\n' + combined_content + '\n' + html_content)

if __name__ == "__main__":
    main()


