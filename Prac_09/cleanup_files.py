"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    # Change to desired directory
    os.chdir('Lyrics/Christmas')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            #print(f"Renaming {filename} tp {new_name} ")
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.renames(full_name, new_name)

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # name_list = []
    # name_list.append(filename)
    # for line in name_list:
    #     if line.split() == line.islower():
    #         if len(line.islower()) + 1 == line.isupper():
    #             line.islower() + "_"
    # print(name_list)

    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name







main()
