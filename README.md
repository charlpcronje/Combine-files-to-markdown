# Combine Files to Markdown

This Python script combines specified types of files (like Python and Markdown files) into a single Markdown file. It's designed to compile documentation or code snippets from various files into a cohesive format.

## Features

- Combines specified file types (configurable) from a given root directory into a single Markdown file.
- Supports exclusion of specific directories and files.
- Customizable output file path.

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/charlpcronje/Combine-files-to-markdown.git
    ```

2. Navigate to the cloned directory:

    ```
    cd Combine-files-to-markdown
    ```

3. Create a JSON configuration file (`config.json`) with the following structure:

    ```json
    {
        "root_path": "<path-to-files>",
        "output_path": "<output-markdown-file-path>",
        "exclude_folders": [
          "folder1",
          "folder2"
        ],
        "exclude_files": [
          "file1.md",
          "file2.py"
        ],
        "file_types": [
          ".py",
          ".md"
        ]
    }
    ```

    - `root_path`: The root directory for searching files.
    - `output_path`: The path and file name for the output Markdown file.
    - `exclude_folders`: List of folders to be excluded from search.
    - `exclude_files`: List of specific files to exclude.
    - `file_types`: List of file extensions to include in the combination.

4. Run the script:

    ```
    python script.py config.json
    ```

## Contributing

Feel free to fork the project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact

- **Name**: Charl Cronje
- **Email**: [charl.cronje@mail.com](mailto:charl.cronje@mail.com)
- **LinkedIn**: [https://www.linkedin.com/in/charlpcronje](https://www.linkedin.com/in/charlpcronje)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
