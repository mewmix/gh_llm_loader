import os

def generate_file_index(path):
    """
    Generates a nested dictionary representing the folder structure and files.
    """
    file_index = {}
    for root, dirs, files in os.walk(path):
        rel_path = os.path.relpath(root, path)
        if rel_path == ".":
            rel_path = ""
        file_list = [f for f in files if not f.startswith('.')]  # Ignore hidden files
        if rel_path not in file_index:
            file_index[rel_path] = file_list
        else:
            file_index[rel_path].extend(file_list)
    return file_index

def compile_files_to_single_file(source_path, output_filename):
    """
    Compiles all code files into a single file, organized by filename, using UTF-8 encoding.
    """
    file_index = generate_file_index(source_path)
    with open(output_filename, 'w', encoding='utf-8') as output_file:  # Specify UTF-8 encoding here
        for dir_path, files in file_index.items():
            for filename in files:
                file_path = os.path.join(dir_path, filename) if dir_path else filename
                try:
                    with open(file_path, 'r', encoding='utf-8') as file_content:  # Also specify UTF-8 encoding here
                        output_file.write(f"// Filename: {filename}\n\n")  # Header for file
                        output_file.write(file_content.read())
                        output_file.write("\n\n")  # Add space between files for readability
                except UnicodeDecodeError as e:
                    print(f"Error reading {file_path}: {e}")


# Adjust 'source_path' to the root directory of the cloned repo
source_path = "."
output_filename = "compiled_repository_code.txt"

compile_files_to_single_file(source_path, output_filename)
