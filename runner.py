from code_compiler import CodeCompiler

def main():
    # Test data: specify the source directory containing the Python files to compile
    source_dir = 'User/Sandbox/example'
    # Test data: specify the destination directory to copy the compiled files to
    dest_dir = 'User/Sandbox/target'
    # Test data: specify a list of directories to exclude from the compilation and copy process
    exclude_dirs = ['ignoreDir']

    compiler = CodeCompiler(source_dir, dest_dir, exclude_dirs)
    compiler.compile_and_copy()

if __name__ == "__main__":
    main()
