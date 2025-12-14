import os

# Example usage
#- README.md: file_size=1032 bytes, is_dir=False
#- src: file_size=128 bytes, is_dir=True
#- package.json: file_size=1234 bytes, is_dir=False


def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory) #absolute path of working directory
    abs_directory = os.path.abspath(os.path.join(working_directory, directory)) #absolute path of the specified directory
    #abs_directory = ""
    # if directory is None:
    #     #directory = working_directory
    #     abs_directory = os.path.abspath(working_directory)
    # else:
    #     abs_directory = os.path.abspath(os.path.join(working_directory, directory)) #absolute path of the specified directory

    
    #If the absolute directory is not in the working directory, its outside of it, and we return an error message
    if not abs_directory.startswith(abs_working_dir):
        return f'Error: The specified directory "{directory}" is not within the working directory.'
    
    final_response = ""
    contents = os.listdir(abs_directory) #list of all files and directories in the specified directory
    # for every content in the directory
    for content in contents:
        content_path = os.path.join(abs_directory, content) #absolute path of the content
        is_dir = os.path.isdir(content_path) #check if the content is a directory
        size = os.path.getsize(content_path) #get the size of the content in bytes
        final_response += f"- {content}: file_size={size} bytes, is_dir={is_dir}\n" #add the information to the final response string
    return final_response

