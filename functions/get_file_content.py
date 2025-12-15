import os


from config import MAX_CHARS #MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    #check if the file exists and its path is within the working directory
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: File path "{file_path}" is outside the working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: file "{file_path}" does not a file'

    file_content_string = ''

    try:
        with open(abs_file_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += f'[... File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f'Error, exception occurred while reading file: {str(e)}'