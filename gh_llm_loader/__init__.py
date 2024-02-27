# gh_llm_loader/__init__.py

from .handler import generate_file_index, compile_files_to_single_file
from .repo_cloner import clone_and_prepare_repo

# Optionally, define any package-level variables or initialization code here

# Specify what should be imported with "from gh_llm_loader import *"
__all__ = ['generate_file_index', 'compile_files_to_single_file', 'clone_and_prepare_repo']
