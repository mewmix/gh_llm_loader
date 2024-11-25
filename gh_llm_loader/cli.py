import argparse
import os
from .repo_cloner import clone_and_prepare_repo
from .handler import compile_files_to_single_file  # Assuming the handler is imported here

def main():
    parser = argparse.ArgumentParser(description="Tool to clone GitHub repositories or prepare directories for LLM ingestion.")
    parser.add_argument("--git-url", type=str, help="GitHub repository URL to clone.")
    parser.add_argument("--base-dir", type=str, default="./cloned_repos", help="Base directory for cloned repositories or directory to process.")
    parser.add_argument("--ignored-folders", type=str, nargs="*", default=[".git"], help="Folders to ignore.")
    parser.add_argument("--ignored-files", type=str, nargs="*", default=[], help="Files to ignore.")
    parser.add_argument("--included-folders", type=str, nargs="*", default=[], help="Folders to include.")
    parser.add_argument("--file-filter", type=str, default=None, help="Custom file filter function (e.g., 'lambda f: f.endswith('.txt') or f == 'README.md')'")
    parser.add_argument("--output-file", type=str, default="compiled_output.txt", help="Output file name for compiled content.")

    args = parser.parse_args()

    # Convert lists from argparse to sets for ignored folders and files
    ignored_folders = set(args.ignored_folders)
    ignored_files = set(args.ignored_files)
    included_folders = set(args.included_folders)
    file_filter = eval(args.file_filter) if args.file_filter else None

    # If --git-url is provided, clone the repository and prepare it
    if args.git_url:
        print(f"Cloning repository from {args.git_url}...")
        clone_and_prepare_repo(
            git_url=args.git_url,
            base_dir=args.base_dir,
            ignored_folders=ignored_folders,
            ignored_files=ignored_files,
            included_folders=included_folders,
            file_filter=file_filter,
        )
    else:
        # If only --base-dir is provided, process the directory
        if not os.path.exists(args.base_dir):
            print(f"Error: Base directory {args.base_dir} does not exist.")
            return

        print(f"Processing directory {args.base_dir}...")
        compile_files_to_single_file(
            source_path=args.base_dir,
            output_filename=args.output_file,
            ignored_folders=ignored_folders,
            ignored_files=ignored_files,
            included_folders=included_folders,
            file_filter=file_filter,
        )
        print(f"Compilation complete. Output saved to {args.output_file}.")

if __name__ == "__main__":
    main()
