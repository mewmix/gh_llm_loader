import os

def generate_file_index(path, ignored_folders=None, ignored_files=None):
    """
    Generates a nested dictionary representing the folder structure and files,
    excluding specified folders and files.
    """
    if ignored_folders is None:
        ignored_folders = set()
    if ignored_files is None:
        ignored_files = set()

    file_index = {}
    for root, dirs, files in os.walk(path):
        # Update dirs in place to exclude ignored folders
        dirs[:] = [d for d in dirs if d not in ignored_folders]

        rel_path = os.path.relpath(root, path)
        rel_path = "" if rel_path == "." else rel_path

        # Filter out ignored files and hidden files
        file_list = [f for f in files if f not in ignored_files and not f.startswith('.')]
        if rel_path not in file_index:
            file_index[rel_path] = file_list
        else:
            file_index[rel_path].extend(file_list)
    return file_index

def compile_files_to_single_file(source_path, output_filename, ignored_folders=None, ignored_files=None):
    """
    Compiles all code files into a single file, organized by filename, using UTF-8 encoding,
    excluding specified folders and files. Includes a header showing directory structure.
    """
    file_index = generate_file_index(source_path, ignored_folders, ignored_files)
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for dir_path, files in sorted(file_index.items()):
            if files:  # Only include directories in the header that contain files
                # Write directory path as a header
                output_file.write(f"// Directory: {dir_path if dir_path else '/'}\n")
                for filename in files:
                    file_path = os.path.join(source_path, dir_path, filename) if dir_path else os.path.join(source_path, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file_content:
                            output_file.write(f"// Filename: {filename}\n\n")
                            output_file.write(file_content.read())
                            output_file.write("\n\n")  # Separator between files
                    except UnicodeDecodeError as e:
                        print(f"Error reading {file_path}: {e}")
                output_file.write("// End of Directory\n\n")  # Mark the end of a directory's content



