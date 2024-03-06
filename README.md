

# gh_llm_loader

`gh_llm_loader` is a package designed to clone GitHub repositories and prepare their data for ingestion for LLMs.

## Features

- **Prepare Repository Data**: Compiles the contents of repositories into a single, clean file by excluding specified folders and files, or including only specified folders and files. This streamlined format is more accessible for LLM ingestion.
- **Flexible File Filtering**: Filter files based on extensions, filenames, or custom functions for maximum control over the included content.
- **CLI and Library Integration**: Flexibility for various use cases and workflows.

## Installation

To install `gh_llm_loader`, make sure you have Python installed on your system, then run the following command:

```sh
git clone https://github.com/mewmix/gh_llm_loader
cd gh_llm_loader
pip install .
```

**Prerequisites:**
- Python 3.6 or newer
- Git installed on your system

## Usage

### Library Usage

`gh_llm_loader` can be easily integrated into Python scripts. Here's an example of how to use it:

```python
from gh_llm_loader import clone_and_prepare_repo

# Define the GitHub repository URL
git_url = "https://github.com/yourusername/yourrepository.git"

# Clone and prepare the repository, specifying folders and files to ignore or include
clone_and_prepare_repo(git_url, ignored_folders={'node_modules', '.git'}, ignored_files={'README.md'}, included_folders={'.teamcity'}, file_filter=lambda f: f.endswith('.xml'))
```

This function will clone the specified GitHub repository and prepare its data by compiling the files into a single file, excluding any folders or files specified, and including only the specified folders and files that match the filter criteria.

If you wish to simply curate a non github folder with the same methods the core function is available for import and use-

```python
import os
from gh_llm_loader import compile_files_to_single_file

# Specify the path to your project directory
source_path = "/path/to/your/project"

# Define the name for the output file
output_filename = "project_compiled.txt"

# Specify any folders or files you want to ignore during compilation
ignored_folders = {'node_modules', '.git', 'build'}
ignored_files = {'README.md', 'LICENSE'}

# Compile the project files into a single file
compile_files_to_single_file(source_path, output_filename, ignored_folders, ignored_files)

print(f"Compilation complete. The output is saved in {output_filename}")
```

### Command-Line Interface (CLI)

For those preferring to use the command line, here are some examples:

a) Include only Python files:
```sh
gh-llm-loader --git-url https://github.com/psf/requests --file-filter "lambda f: f.endswith('.py')"
```

b) Include only Markdown and text files:
```sh
gh-llm-loader --git-url https://github.com/tensorflow/models --file-filter "lambda f: f.endswith('.md') or f.endswith('.txt')"
```

c) Include only files with "test" in the filename:
```sh
gh-llm-loader --git-url https://github.com/django/django --file-filter "lambda f: 'test' in f"
```

d) Include only JavaScript files and the "package.json" file:
```sh
gh-llm-loader --git-url https://github.com/facebook/react --file-filter "lambda f: f.endswith('.js') or f == 'package.json'"
```

e) Include only files in the "src" and "docs" folders:
```sh
gh-llm-loader --git-url https://github.com/vuejs/vue --included-folders src docs
```

f) Exclude the "tests" folder and include only Python files:
```sh
gh-llm-loader --git-url https://github.com/pallets/flask --ignored-folders tests --file-filter "lambda f: f.endswith('.py')"
```


## Contributing

Contributions to `gh_llm_loader` are highly encouraged and appreciated. 


## License

`gh_llm_loader` is made available under the MIT License. For more details, see the LICENSE file in the repository.

