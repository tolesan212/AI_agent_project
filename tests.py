from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_dir = "calculator"

    # #test get_file_info
    # root_contents = get_files_info(working_dir)
    # print(root_contents) #print root contents
    # pkg_contents = get_files_info(working_dir, "pkg")
    # print(pkg_contents) #print pkg folder contents
    # #test that it won't work if trying to inspect files outside of working directory
    # pkg_contents = get_files_info(working_dir, "/bin") #/bin is outside of working directory (root of file system)
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir, "../") # ../ walks up one directory
    # print(pkg_contents)

    # #test get_file_content
    # #print(get_file_content(working_dir, "lorem.txt")) #warning: this file is large, may take a while to print
    # print(get_file_content(working_dir, "main.py"))
    # print(get_file_content(working_dir, "pkg/calculator.py"))
    # print(get_file_content(working_dir, "pkg/notexists.py")) #file does not exist
    # print(get_file_content(working_dir, "/bin/cat")) #/bin is outside of working directory (root of file system)

    #test write_file
    #print(write_file(working_dir, "lorem.txt", "wait, this isn't lorem ipsum!")) #edits an existing file
    #print(write_file(working_dir, "pkg/morelorem.txt", "lorem ipsum!")) #creates a new file if it doesn't exist
    #print(write_file(working_dir, "/tmp/temp.txt", "this should not be allowed")) #/tmp is outside of working directory (root of file system)
    
    #test run_python_file
    #print(run_python_file(working_dir, "main.py"))
    print(run_python_file(working_dir, "tests.py"))



main()