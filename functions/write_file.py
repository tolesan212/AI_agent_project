import os




def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    #check if the file exists and its path is within the working directory
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: File path "{file_path}" is outside the working directory'
    
    # #If it's not a file, make all the necessary directories (unnecessary)
    # if not os.path.isfile(abs_file_path):
    #     parent_dir = os.path.dirname(abs_file_path)
    #     try:
    #         os.markedirs(parent_dir)
    #     except Exception as e:
    #         return 'Could not create parent directories: {parent_dir} = {e}'
    
    try:
        with open(abs_file_path, 'w') as file:
            file.write(content)
        return f'File "{file_path}" has been written successfully. ({len(content)} characters/bytes written)'
    except Exception as e:
        return f'Error: Could not write to file "{file_path}": {e}'
    

