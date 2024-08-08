# Combine Files to Markdown

This Python script, "Combine Files to Markdown," efficiently aggregates content from various files into a single Markdown document. It simplifies the process of combining content from multiple sources into a cohesive document, designed for streamlined documentation and code snippet compilation. The script offers flexibility for project-related file management, including customizable file selection and `.gitignore` file support.

## Features

### 1. File Aggregation
- **Description**: Merges content from different file types into a single Markdown document, streamlining documentation.
- **Usage**: Run the script to combine specified file types from a directory and its subdirectories into one Markdown file.

### 2. Customizable File Selection
- **Description**: Configure the script to include specific file types in the output.
- **Usage**: Modify the `"file_types"` field in `config.json` to specify desired file extensions.

### 3. Directory Control
- **Description**: Control over which directories are included or excluded from the aggregation process.
- **Usage**: Add folder names to `"exclude_folders"` in `config.json` to exclude them.

### 4. File Exclusion
- **Description**: Exclude specific files from the aggregation process.
- **Usage**: Add file names to `"exclude_files"` in `config.json`.

### 5. Configurable Output
- **Description**: Customize the output file path for the generated Markdown document.
- **Usage**: Set `"output_path"` in `config.json`.

### 6. Encoding Support
- **Description**: Handles file encodings to ensure content readability.
- **Usage**: Automatically managed by the script.

### 7. Automated Section Headers
- **Description**: Adds section headers for each file's content in the generated document.
- **Usage**: Visible in the generated Markdown file.

### 8. CLI-Based Interface
- **Description**: Easy-to-use command-line interface for script execution.
- **Usage**: Provide the path to `config.json` as an argument when executing the script.

### 9. Detailed File Analysis
- **Description**: Provides post-processing analysis of processed files.
- **Usage**: Included in the generated Markdown document.

### 10. .gitignore Pattern Recognition
- **Description**: Excludes files and directories as specified in a `.gitignore` file.
- **Usage**: Specify `.gitignore` path in `config.json`.

### 11. ASCII-style File Tree Generation in Markdown
- **Description**: Generates a Markdown-formatted file tree of the project's structure, with links to actual files.
- **Usage**: The file tree is generated automatically and saved as `tree.md` in the output directory.

### 12. Configurable Heading and Description
- **Description**: Allows setting a custom heading and description for the analysis report.
- **Usage**: Add `heading` and `description` fields in `config.json`.

### 13. Optional HTML Styles for Dark Mode
- **Description**: Adds optional HTML styles for dark mode in the generated Markdown output.
- **Usage**: Run the script with the `--include-html-styles` argument to include the styles.

## Setup and Usage

1. **Clone the Repository**:
   ```shell
   git clone https://github.com/charlpcronje/Combine-files-to-markdown.git
   ```

2. **Navigate to the Project Directory**:
   ```shell
   cd Combine-files-to-markdown
   ```

3. **Install Dependencies**:
   ```shell
   pip install -r requirements.txt
   ```

4. **Configuration**:
   Create or modify the `config.json` file as per your requirements. Example:
   ```json
   {
       "root_path": "src",
       "output_path": "output/combined.md",
       "exclude_folders": ["test", "docs"],
       "exclude_files": [".gitignore", "README.md"],
       "file_types": [".py", ".txt", ".md"],
       "gitignore_path": ".gitignore",
       "heading": "Project File Analysis",
       "description": "This report provides an analysis of the project files."
   }
   ```

5. **Run the Script**:
   - For file aggregation:
     ```shell
     python main.py config.json
     ```
   - To include HTML styles for dark mode:
     ```shell
     python main.py config.json --include-html-styles
     ```

## Configuration Details

- **root_path**: Directory to search for files.
- **output_path**: Path for the generated Markdown file.
- **exclude_folders**: Folders to exclude.
- **exclude_files**: Specific files to exclude.
- **file_types**: File types to include.
- **gitignore_path**: `.gitignore` file path (optional).
- **heading**: Custom heading for the analysis report.
- **description**: Custom description for the analysis report.

## Contributing

Contributions are welcome. Please open an issue first to discuss proposed changes or features.

## Contact

- **Name**: Charl Cronje
- **Email**: [charl.cronje@mail.com](mailto:charl.cronje@mail.com)
- **LinkedIn**: [https://www.linkedin.com/in/charlpcronje](https://www.linkedin.com/in/charlpcronje)

## License

Licensed under the MIT License. See [LICENSE.md](./LICENSE.md) for details.