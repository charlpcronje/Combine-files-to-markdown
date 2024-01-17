# Combine Files to Markdown

This Python script, "Combine Files to Markdown," efficiently aggregates content from various files into a single Markdown document. It's designed for streamlined documentation and code snippet compilation, offering flexibility for project-related file management.

## Features

- **File Aggregation**: Merges content from different file types into a single Markdown file.
- **Customizable File Selection**: Configures specific file types to include, like `.py`, `.md`, `.json`, etc.
- **Directory Control**: Inclusion and exclusion of specified directories for targeted file processing.
- **File Exclusion**: Capability to ignore specific files, focusing only on relevant content.
- **Configurable Output**: Allows users to specify the output file path for custom output location.
- **Encoding Support**: Ensures consistent readability by properly handling file encodings.
- **Automated Section Headers**: Adds a header for each file's content in the Markdown output for easy navigation.
- **CLI-Based Interface**: Easy-to-use command-line interface for integration into various workflows.
- **Detailed File Analysis**: Post-processing analysis of each file, counting lines, words, and AI tokens, enhancing content insight.

## Setup and Usage

1. **Clone the Repository**:
   ```shell
   git clone https://github.com/charlpcronje/Combine-files-to-markdown.git
   ```

2. **Navigate to the Project Directory**:
   ```shell
   cd Combine-files-to-markdown
   ```

3. **Install Dependencies** (if any):
   ```shell
   pip install -r requirements.txt
   ```

4. **Configuration**:
   Create a `config.json` file in the project directory. Here's a template:
   ```json
   {
       "root_path": "<path-to-files>",
       "output_path": "<output-markdown-file-path>",
       "exclude_folders": ["folder1", "folder2"],
       "exclude_files": ["file1.md", "file2.py"],
       "file_types": [".py", ".md", ".json"]
   }
   ```

5. **Run the Script**:
   ```shell
   python main.py config.json
   ```

## Configuration Details

- **root_path**: The directory to search for files.
- **output_path**: Path for the generated Markdown file.
- **exclude_folders**: List of folders to exclude from the search.
- **exclude_files**: Specific files to exclude.
- **file_types**: Types of files to include in the output.

## Contributing

Contributions are welcome. For major changes or new features, please open an issue first to discuss what you'd like to change. Feel free to fork the project and submit pull requests.

## Contact

- **Name**: Charl Cronje
- **Email**: [charl.cronje@mail.com](mailto:charl.cronje@mail.com)
- **LinkedIn**: [https://www.linkedin.com/in/charlpcronje](https://www.linkedin.com/in/charlpcronje)

## License

This project is licensed under the MIT License. See the [LICENSE.md](./LICENSE.md) file for details.