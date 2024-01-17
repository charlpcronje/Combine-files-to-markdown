# Combine Files to Markdown

This Python script, "Combine Files to Markdown," efficiently aggregates content from various files into a single Markdown document. It's designed for streamlined documentation and code snippet compilation, offering flexibility for project-related file management. It also offers the ability to customize the file selection process to include only the files that you need. .gitignore files are also supported.

Certainly, let's break down each feature into its own heading and provide detailed explanations:

## Features

### 1. File Aggregation

- **Description**: This feature allows the script to merge content from different types of files into a single Markdown file. It simplifies the process of combining content from multiple sources into a cohesive document.
- **Usage**: When you run the script, it will aggregate the content of specified file types from a directory and its subdirectories into a Markdown file.

### 2. Customizable File Selection

- **Description**: You can configure the script to include specific file types in the output. For example, you can choose to include `.py`, `.md`, `.json`, or any other file types that are relevant to your project.
- **Usage**: Modify the `"file_types"` field in the `config.json` file to specify the file extensions you want to include.

### 3. Directory Control

- **Description**: This feature provides control over which directories are included or excluded from the file aggregation process. You can specify folders to be excluded, ensuring that only relevant content is processed.
- **Usage**: Add folder names to the `"exclude_folders"` field in the `config.json` file to exclude them from processing.

### 4. File Exclusion

- **Description**: You can specify individual files to be excluded from the aggregation process. This is useful when you have specific files that you want to skip.
- **Usage**: Add file names (including extensions) to the `"exclude_files"` field in the `config.json` file to exclude them from processing.

### 5. Configurable Output

- **Description**: This feature allows you to specify the output file path for the generated Markdown document. You can customize where the combined content will be saved.
- **Usage**: Set the `"output_path"` field in the `config.json` file to define the path and name of the output Markdown file.

### 6. Encoding Support

- **Description**: The script ensures consistent readability by properly handling file encodings. It takes care of encoding-related issues, ensuring that the content is correctly interpreted during aggregation.
- **Usage**: No additional configuration is required; the script automatically handles encoding.

### 7. Automated Section Headers

- **Description**: To enhance navigation within the generated Markdown file, the script adds automated section headers for each file's content. This makes it easy to locate specific content within the document.
- **Usage**: When you view the generated Markdown file, you'll find section headers for each aggregated file.

### 8. CLI-Based Interface

- **Description**: The script provides a user-friendly command-line interface (CLI) for easy integration into various workflows. You can run the script from the command line without needing to modify its code.
- **Usage**: Execute the script with the appropriate command, providing the path to your `config.json` file as an argument.

### 9. Detailed File Analysis

- **Description**: After aggregating the content, the script offers a post-processing analysis of each processed file. It calculates line counts, word counts, and AI token counts for deeper insights into the content.
- **Usage**: The analysis report is included in the generated Markdown file, providing valuable information about the processed files.

These features collectively make the "Combine Files to Markdown" script a versatile tool for aggregating and analyzing content from diverse files into a single, well-structured Markdown document.

### .gitignore Pattern Recognition

- **Description**: The script includes a feature that recognizes patterns from a `.gitignore` file specified in the configuration. If you have a `.gitignore` file in your project, this feature ensures that the files and directories excluded by your Gitignore rules are also excluded from the file aggregation process. It respects your version control settings, preventing unnecessary files from being included in the Markdown output.
- **Usage**: If you have a `.gitignore` file in your project, simply specify its path in the `"gitignore_path"` field of the `config.json` file. The script will read the patterns from the Gitignore file and use them to exclude files and directories during aggregation.

This feature is particularly useful when you want to ensure that your Markdown output aligns with your project's version control settings and excludes files that should not be part of the documentation. It simplifies the management of content inclusion and exclusion based on Gitignore rules.

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
    "root_path": "<absolute_path-to-files>",
    "output_path": "<absolute_markdown-file-path>",
    "gitignore_path": ".gitignore",
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
- **gitignore_path**: Path to the .gitignore file for pattern recognition (optional).

## Contributing

Contributions are welcome. For major changes or new features, please open an issue first to discuss what you'd like to change. Feel free to fork the project and submit pull requests.

## Contact

- **Name**: Charl Cronje
- **Email**: [charl.cronje@mail.com](mailto:charl.cronje@mail.com)
- **LinkedIn**: [https://www.linkedin.com/in/charlpcronje](https://www.linkedin.com/in/charlpcronje)

## License

This project is licensed under the MIT License. See the [LICENSE.md](./LICENSE.md) file for details.