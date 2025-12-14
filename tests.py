from functions.get_files_info import get_files_info

def main():
    working_dir = "calculator"
    root_contents = get_files_info(working_dir)
    print(root_contents) #print root contents
    pkg_contents = get_files_info(working_dir, "pkg")
    print(pkg_contents) #print pkg folder contents

    #test that it won't work if trying to inspect files outside of working directory
    pkg_contents = get_files_info(working_dir, "/bin") #/bin is outside of working directory (root of file system)
    print(pkg_contents)
    pkg_contents = get_files_info(working_dir, "../") # ../ walks up one directory
    print(pkg_contents)

main()