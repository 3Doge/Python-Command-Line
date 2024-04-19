import os

# ignore this it is just setup
# setup for create directory
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print("Directory '{}' created successfully.".format(directory_name))
    except FileExistsError:
        print("Directory '{}' already exists.".format(directory_name))



username = input("Baps name eg: BapsisGod: ")

i = 0
while i <= 10:
    text = input(username + os.getcwd() + ": ")
    # list files
    if text.lower() == "lf":
        files = os.listdir()
        print("Files in the current directory:")
        for file in files:
            print(file)
    # set directory
    if text.lower() == "sd":
        new_directory = input("which directory?")
        os.chdir(new_directory)
    # make directory
    if text.lower() == "cd":
        new_directory = input("Enter the name of the directory to create: ")
        create_directory(new_directory)

        print("Current directory after changing to:", os.getcwd())


