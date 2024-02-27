import os
import subprocess
from .handler import compile_files_to_single_file  # Ensure this is correctly imported

def clone_and_prepare_repo(git_url, base_dir="./cloned_repos", ignored_folders=None, ignored_files=None):
    """
    Clones a GitHub repository and prepares its data for ingestion by an LLM, with dynamic naming based on the repo.
    """
    # Extract the repository name from the URL
    repo_name = git_url.split('/')[-1]
    if repo_name.endswith('.git'):
        repo_name = repo_name[:-4]
    
    # Set up local directory and output filename
    local_dir = os.path.join(base_dir, repo_name)
    output_filename = f"{repo_name}_compiled.txt"

    # Ensure the base directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Clone the repository if it's not already cloned
    if not os.path.exists(local_dir):
        subprocess.run(['git', 'clone', git_url, local_dir], check=True)
    else:
        print(f"Repository already cloned at {local_dir}")

    # Compile the repository's contents
    compile_files_to_single_file(local_dir, os.path.join(base_dir, output_filename), ignored_folders, ignored_files)
    
    print(f"Repository cloned and data prepared at {os.path.join(base_dir, output_filename)}")

