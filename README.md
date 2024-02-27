

# gh_llm_loader

`gh_llm_loader` is a package designed to clone GitHub repositories and prepare their data for ingestion for LLMs.

## Features

- **Prepare Repository Data**: Compiles the contents of repositories into a single, clean file by excluding specified folders and files. This streamlined format is more accessible for LLM ingestion.
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

# Clone and prepare the repository, specifying folders and files to ignore
clone_and_prepare_repo(git_url, ignored_folders={'node_modules', '.git'}, ignored_files={'README.md'})
```

This function will clone the specified GitHub repository and prepare its data by compiling the files into a single file, excluding any folders or files specified.

### Command-Line Interface (CLI)

For those preferring to use the command line:

```sh
gh-llm-loader --git-url https://github.com/yourusername/yourrepository.git --ignored-folders node_modules .git --ignored-files README.md
```

This command performs the same operation as the library usage example, cloning and preparing a repository for LLM ingestion.

## Contributing

Contributions to `gh_llm_loader` are highly encouraged and appreciated. 


## License

`gh_llm_loader` is made available under the MIT License. For more details, see the LICENSE file in the repository.

