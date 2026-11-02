#mkdir - make a file/directory
#rmdir - remove a file/directory

import os
os.mkdir("Hello")
os.rmdir("hello")








'''
FILE
x - this mode will only create the file and if already exist then it will error
w - agar file exist nhi krrhi h so this mode will create one and insert the content inside the file.
a - 
r - 
'''

#Mode 1: x - Just to create the file
# open("Garba.txt", "x")



#Mode 2: w - if there is any content inside the file then it will rewrite it.
# file = open("Garba.txt", "w")
# file.write("huhbunecndbu")

#Mode 3: a - add the text to the last.
# file = open("Garba.txt", "a")
# file.write("\nThis messsage is newly added")


#Mode 4: r - read the content inside the file
# file = open("Garba.txt","r")
# print(file.read())



'''
with open("sample.txt", "w") as file:
    file.write("This is new file")
'''  # this will automatically open and close the file



# CURD- Create, Read, Update, Delete
# import os
# os.remove("Garba.txt")
# print("Press 1 for Creating a new file : ")
# print("Press 2 for Reading any file : ")
# print("Press 3 for Updating any file : ")
# print("Preass 4 for DEleting any file : ")





'''-----------------------------------------------------------------------------------------------------------------------------------------------'''
from pathlib import Path
import os


def create_folder():
    name = input("Tell your folder name :- ") 
    p = Path(name)

    if p.exists():
        print("This folder already exist please try again")
        create_folder()
    else:
        p.mkdir()
        print("folder created successfully")


def read_folder():
    p = Path("")
    names = list(p.rglob("*"))

    for i in range(len(names)):
        print(f"{i+1} - {names[i]}")


def update_folder():
    read_folder()
    name = input("Which folder you want to update :- ")
    old_p = Path(name)

    if old_p.exist():
        new_name = input("Tel new folder name :- ")
        new_p = Path(new_name)
        old_p.rename(new_p)
        print("folder name changed successfully")
    else:
        print("Folder not exist, try again")
        update_folder()


def delete_folder():
    name = input("Tell your folder name :- ") 
    p = Path(name)
    
    if p.exists():
        p.rmdir()
        print("folder deleted successfully")
    else:
        print("This folder does not exist please try again")
        create_folder()


def create_file():
    name = input("tell your name with extension :- ")
    p = Path(name)
    if p.exists():
        print("file already exist!")
        create_file()
    else:
        with open(p,"w") as file:
            data = input("Enter what you want to write :")
            file.write(data)
            print("file created sucessfully!")


def read_file():
    name = input("which file you want to read :- ")
    p = Path(name)
    if p.exists() and p.is_file():        #is_file is a function to check if the given path is file or not.
        with open (p,"r") as file:
            data = file.read()
            print("\n\n\nYour file data is\n\n\n")
            print(data)

def delete_file():
    name = input("Enter file name :- ")
    p = Path(name)
    if p.exists():
        os.remove(p)
        print("file deleted sucessfully!")
    else:
        print("file not exist!")
        delete_file()


def update_file():
    names = read_folder()
    for i in names:
        i = str(i)
        p = Path(i)
        if p.is_file():
            print(i)
    name = input("Which file yoy want to update :- ")
    p = Path(name)

    if p.exists() and p.is_file():
        print("Press 1 to change file name")
        print('Press 2 to overwrite the file')
        print("press 3 to append")

        check = int(input("enter your response :- "))
        if check == 1:
            new_name = input("Tell the new name :- ")
            new_p = Path(new_name)
            p.rename(new_p)

        elif check == 2:
            with open(p,'w') as file:
                data = input("what do you want to overwrite:- ")
                file.write(data)
                print("overwritten successfully ")

        elif check == 3:
            with open(p,'a') as file:
                data = input("what do you want to append:- ")
                file.write(" "+ data)
                print("appended successfully ")
            

    else:
        print("no such file exists please try again ")
        update_file()

print("press 1 - for creating a folder")
print("press 2 - for reading a folder")
print("press 3 - for updating a folder")
print("press 4 - for deleting a folder")
print("press 5 - for creating a file")
print("press 6 - for reading a file")
print("press 8 - for updating a file")
print("press 8 - for deleting a file")

res = int(input("Tell your response:- "))

if res == 1:
    create_folder()

if res == 2:
    read_folder()

if res == 3:
    update_folder()

if res == 4:
    delete_folder()

if res == 5:
    create_file()

if res == 6:
    read_file()

if res == 8:
    delete_file()

if res == 7:
    update_file()



#pip install streamlit