import os
import re
import shutil
import compileall

class CodeCompiler:
    """
    A class to compile Python files to bytecode and copy them to a destination directory,
    excluding specified directories and removing version-specific parts of filenames so that destination contains exact replica.
    """
    
    def __init__(self, src, dest, exclude_dirs=None):
        """
        Initialize the CodeCompiler.

        Parameters:
        src (str): The source directory containing the Python files to compile.
        dest (str): The destination directory to copy the compiled files to.
        exclude_dirs (list, optional): A list of directories to exclude from the compilation and copy process.
        """
        self.src = src
        self.dest = dest
        self.exclude_dirs = exclude_dirs or []
        self.exclude_dirs_complete_path = [os.path.join(self.src, str(directory)) for directory in self.exclude_dirs]
        self.src = self.src.replace('\\', '/')
        self.dest = self.dest.replace('\\', '/')

    def compile_and_copy(self):
        """
        Compile all Python files in the source directory to bytecode and copy them to the destination directory,
        excluding specified directories and adjusting filenames to remove version-specific parts.
        """
        # Compile all Python files in the source directory
        compileall.compile_dir(self.src, force=True, legacy=True)
        
        # Create the destination directory if it does not exist
        if not os.path.exists(self.dest):
            os.makedirs(self.dest)

        # Walk through the source directory
        for root, dirs, files in os.walk(self.src):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in self.exclude_dirs_complete_path]
           
            for file in files:
                if not file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, self.src)

                    # Adjust the filename to remove version-specific part
                    dest_file_name = re.sub(r'\.cpython-\d+\.pyc$', '.pyc', os.path.basename(file))
                    
                    dest_path = os.path.join(self.dest, os.path.dirname(relative_path), dest_file_name)

                    # Remove __pycache__ from the path
                    if '__pycache__' in dest_path:
                        dest_path = dest_path.replace('__pycache__\\', '').replace('__pycache__/', '')

                    dest_dir = os.path.dirname(dest_path)
                    # Create the destination directory if it does not exist
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    
                    # Copy the compiled file to the destination directory
                    shutil.copy2(file_path, dest_path)
