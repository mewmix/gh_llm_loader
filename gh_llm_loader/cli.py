import argparse
from .repo_cloner import clone_and_prepare_repo

def main():
    parser = argparse.ArgumentParser(description="Tool to clone GitHub repositories and prepare them for LLM ingestion.")
    parser.add_argument("--git-url", type=str, required=True, help="GitHub repository URL to clone.")
    parser.add_argument("--base-dir", type=str, default="./cloned_repos", help="Base directory for cloned repositories.")
    parser.add_argument("--ignored-folders", type=str, nargs="*", default=[".git"], help="Folders to ignore.")
    parser.add_argument("--ignored-files", type=str, nargs="*", default=[], help="Files to ignore.")

    args = parser.parse_args()

    # Convert lists from argparse to sets for ignored folders and files
    ignored_folders = set(args.ignored_folders)
    ignored_files = set(args.ignored_files)

    # Call the clone and prepare function
    clone_and_prepare_repo(git_url=args.git_url, base_dir=args.base_dir, ignored_folders=ignored_folders, ignored_files=ignored_files)

if __name__ == "__main__":
    main()
