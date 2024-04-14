import os

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

        print("Current directory after changing to:", os.getcwd())
