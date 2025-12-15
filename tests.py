from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    working_dir = "calculator"

    # #test get_file_content
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
    #print(get_file_content(working_dir, "lorem.txt"))
    print(get_file_content(working_dir, "main.py"))
    print(get_file_content(working_dir, "pkg/calculator.py"))
    print(get_file_content(working_dir, "pkg/notexists.py")) #file does not exist
    print(get_file_content(working_dir, "/bin/cat")) #/bin is outside of working directory (root of file system)


main()