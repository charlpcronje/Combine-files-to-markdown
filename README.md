# Combine Files to Markdown

This Python script, "Combine Files to Markdown," is a versatile tool designed to aggregate content from various files into a single, cohesive Markdown document. Primarily aimed at streamlining documentation or code snippet compilation, it offers a flexible and efficient solution for managing and presenting project-related files.

## Features

- **File Aggregation**: Merges content from different file types into a single Markdown file.
- **Customizable File Selection**: Allows configuration of specific file types to include, such as `.py`, `.md`, `.json`, etc.
- **Directory Control**: Supports inclusion and exclusion of specified directories, enabling targeted file processing.
- **File Exclusion**: Provides the ability to ignore specific files, ensuring only relevant content is included.
- **Configurable Output**: Users can specify the output file path, tailoring the output location to their needs.
- **Encoding Support**: Ensures proper handling of file encodings for consistent readability.
- **Automated Section Headers**: Each file's content is preceded by a header in the Markdown output for easy navigation and reference.
- **CLI-Based Interface**: Simple command-line usage for straightforward operation and integration into various workflows.

## Setup and Usage

1. **Clone the Repository**:
   ```shell
   git clone https://github.com/charlpcronje/Combine-files-to-markdown.git
   ```
   
   2. **Navigate to the Cloned Directory**:
   ```shell
   cd Combine-files-to-Markdown

   
Here's a comprehensive update for your README.md to include detailed features, usage instructions, configuration details, and your contact information. You can replace the existing content in your README.md with this:

markdown
Copy code
# Combine Files to Markdown

This Python script, "Combine Files to Markdown," is a versatile tool designed to aggregate content from various files into a single, cohesive Markdown document. Primarily aimed at streamlining documentation or code snippet compilation, it offers a flexible and efficient solution for managing and presenting project-related files.

## Features

- **File Aggregation**: Merges content from different file types into a single Markdown file.
- **Customizable File Selection**: Allows configuration of specific file types to include, such as `.py`, `.md`, `.json`, etc.
- **Directory Control**: Supports inclusion and exclusion of specified directories, enabling targeted file processing.
- **File Exclusion**: Provides the ability to ignore specific files, ensuring only relevant content is included.
- **Configurable Output**: Users can specify the output file path, tailoring the output location to their needs.
- **Encoding Support**: Ensures proper handling of file encodings for consistent readability.
- **Automated Section Headers**: Each file's content is preceded by a header in the Markdown output for easy navigation and reference.
- **CLI-Based Interface**: Simple command-line usage for straightforward operation and integration into various workflows.

## Setup and Usage

1. **Clone the Repository**:
```shell
git clone https://github.com/charlpcronje/Combine-files-to-markdown.git
```

2. **Navigate to the Project Directory:**
```shell
cd Combine-files-to-markdown
``` ```
3. **Configuration**:
Create a `config.json` file in the project directory with the following structure:

```json
{
    "root_path": "<path-to-files>",
    "output_path": "<output-markdown-file-path>",
    "exclude_folders": ["folder1", "folder2"],
    "exclude_files": ["file1.md", "file2.py"],
    "file_types": [".py", ".md"]
}
```
- root_path: Directory to search for files.
- output_path: Path for the generated Markdown file.
- exclude_folders: Folders to exclude from the search.
- exclude_files: Specific files to exclude.
- file_types: Types of files to include in the output.

4. Run the Script:
`Execute` the script with the configuration file as an argument:

```sh
python main.py config.json
```

## Configuration Details

- **Root Path**: Designates the starting point for file search.
- **Output Path**: Determines where the compiled Markdown file will be saved.
- **Exclude Folders**: List of directories to be omitted during file search.
- **Exclude Files**: Specific files to be excluded.
- **File Types**: Extensions of the files to be included in the final Markdown document.

## Contributing
Contributions are welcome and greatly appreciated. For major changes or feature additions, please open an issue first to discuss what you'd like to change. Feel free to fork the project and submit pull requests.


## Contact
For inquiries, contributions, or further information about the project, please reach out to:

- **Name**: Charl Cronje
- **Email**: [charl.cronje@mail.com](mailto:charl.cronje@mail.com)
- **LinkedIn**: [https://www.linkedin.com/in/charlpcron](https://www.linkedin.com/in/charlpcron)

## License
This project is licensed under the MIT License. See the [LICENSE.md](./LICENSE.md) file for details