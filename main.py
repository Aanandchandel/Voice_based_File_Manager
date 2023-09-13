import speech_recognition as sr

import os
import pyttsx3
import shutil
import tkinter as tk


def get_list_files_and_folders():
    # Get current directory
    current_dir = os.getcwd()

    # Get list of files and folders
    files_and_folders = os.listdir(current_dir)

    # Return list of files and folders
    return files_and_folders


def open_file(file_path):
    os.startfile(file_path)


def display_list(lst, exit_string="exit"):
    # Create a tkinter window with a fixed size of 800x600
    window = tk.Tk()
    window.title("File Manager")
    window.geometry("800x600")
    window.configure(bg="black")

    # Create a table to display the list
    for i, item in enumerate(lst):
        e = tk.Entry(window, width=80, fg='blue', font=('Arial', 12, 'bold'))
        e.grid(row=i, column=0)
        e.insert(tk.END, item)

    # Create a label widget to display instructions for the exit string
    label = tk.Label(
        window, text=f"Type '{exit_string}' in the entry below to close the window", font=("Arial", 12))
    label.grid(row=len(lst)+1, column=0)

    # Create an entry widget for the user to type 'exit'
    entry = tk.Entry(window)
    entry.grid(row=len(lst)+2, column=0)

    # Define a function to check if the user typed 'exit'
    def check_exit(event):
        if entry.get() == exit_string:
            window.destroy()

    # Bind the check_exit function to the Entry widget
    entry.bind("<Return>", check_exit)

    # Set a timer to close the window after 10 seconds
    window.after(10000, window.destroy)

    # Start the tkinter main loop to display the window
    window.mainloop()


def text_s(a):
    # function is designe for converting text message to voice nessage
    engine = pyttsx3.init()
    engine.say(a)
    engine.runAndWait()


def creat_folder(x):
    # this funtion is designe for create any sapcific folder
    # by just giving the name  of the foleder to the function
    os.mkdir(x)
    print(os.listdir())

def delete():  # d is the name of the dir in current dir
    
    file_path = destination_path
    try:
        try:
            os.remove(file_path)

        except Exception as r:
            text_s("it may cantain so may sub dir")
            it = input("it may cantain so may sub dir still want to delete")
            h = it.rfind("yes")
            if h != -1:
                shutil.rmtree(file_path)
            else:
                text_s("ok dont  worry")

        print(" has been deleted.")
    except Exception as e:
        os.rmdir(file_path)
        print(" directory has been deleted.")


# def delete():  # d is the name of the dir in current dir
   #  filename=input("enter the folder name if file then with extention")
   #  file_path = os.path.join(os.getcwd(), filename)
   #  try:
      #   try:
            # os.remove(file_path)
# 
      #   except Exception as r:
            # text_s("it may cantain so may sub dir")
            # it = input("it may cantain so may sub dir still want to delete")
            # h = it.rfind("yes")
            # if h != -1:
               #  shutil.rmtree(file_path)
            # else:
               #  text_s("ok dont  worry")
# 
      #   print(f"{filename} has been deleted.")
   #  except Exception as e:
      #   os.rmdir(file_path)
      #   print(f"{filename} directory has been deleted.")
# 

def past_fo_fi(source_path):
    """
    Copies a folder or file from the source_path to the current directory
    """
    # Check if source_path is a file or a directory
    if os.path.isfile(source_path):
        # If it's a file, use shutil.copy2 to copy it to the current directory
        shutil.copy2(source_path, os.getcwd())
        print(f"File {source_path} copied to current directory")
    elif os.path.isdir(source_path):
        # If it's a directory, use shutil.copytree to copy it to the current directory
        shutil.copytree(source_path, os.path.join(
            os.getcwd(), os.path.basename(source_path)))
        print(f"Folder {source_path} copied to current directory")
    else:
        print(f"{source_path} is not a valid file or directory")


def manage(path):  # path is the variable which stors the info or proper path of the perticuler dir which you have to manage
    # this funtion will manage all the folder or file on the bases of name of the extenion
    file_name = os.listdir(path)

    for i in file_name:
        file_name, extention = os.path.splitext(i)
        extention_1 = extention[1:]
        fold_path = path + "\\" + extention_1

        if os.path.exists(fold_path):
            shutil.move(path + "\\" + i, path + "\\" + extention_1 + "\\" + i)
        else:
            os.makedirs(fold_path)
            shutil.move(path + "\\" + i, path + "\\" + extention_1 + "\\" + i)


def get():  # this funtion returns \\
    return "\\\\"


def filt(a):  # this funtion avoid the \\error give the fit pat for system
    out = ""
    z = "\\"
    for i in a:
        if i == z:
            k = get()
            out += k
            # print(k)
        if i != z:
            out += i
        else:
            pass

    return out


def searcht(file_tosearch):
    # file_tosearch = input("enter the file namme with exton")
    currentpath = os.getcwd()
    rootdir = currentpath
    # rootdir=input("root")#have to give the root path
    for relpath, dirs, files in os.walk(rootdir):
        if (file_tosearch in files):
            fullpath = os.path.join(relpath, file_tosearch)
            # print(fullpath)
        #   print(relpath,"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            print("this is  a file")
            return fullpath

        elif (file_tosearch in dirs):
            fullpath = os.path.join(rootdir, relpath, file_tosearch)
            # print(fullpath)
            print("this is not a file")
            return fullpath
        else:
            print("dint get anything")


def search():
    listcurrentdir
    file_tosearch = input("enter the file namme with exton")
    currentpath = os.getcwd()
    rootdir = currentpath
    # rootdir=input("root")#have to give the root path
    for relpath, dirs, files in os.walk(rootdir):
        if (file_tosearch in files):
            fullpath = os.path.join(relpath, file_tosearch)
            # print(fullpath)
        #   print(relpath,"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            print("this is  a file")
            return fullpath

        elif (file_tosearch in dirs):
            fullpath = os.path.join(rootdir, relpath, file_tosearch)
            # print(fullpath)
            print("this is not a file")
            return fullpath
        else:
            print("dint get anything")


def move_back():
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    os.chdir(parent_dir)


def move_to_directory(destination_path):
    # Get the absolute path of the destination directory
    abs_path = os.path.abspath(destination_path)

    # Check if the destination directory exists
    if not os.path.isdir(abs_path):
        print(f"Error: '{destination_path}' is not a valid directory")
        return

    # Change the current working directory to the destination directory
    os.chdir(abs_path)
    print(f"Moved to directory: {os.getcwd()}")


def listcurrentdir():  # to list the curruen dir files and folder
    text_s("here is the list of the folders and files")

    path = os.getcwd()
    file_name = os.listdir(path)
    for i in file_name:
        file_name, extention = os.path.splitext(i)
        print("file name(", file_name, ")        file type   =", extention)


def voice_to_text():
    # create a recognizer object
    r = sr.Recognizer()

    # use the default microphone as the audio source
    with sr.Microphone() as source:
        # adjust the microphone sensitivity to reduce background noise
        r.adjust_for_ambient_noise(source)

        print("Speak now...")

        # record the audio for 5 seconds
        audio = r.listen(source, timeout=10)

        print("Transcribing.(..")

        try:
            # recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)
            print(text)
            global inptttt
            inptttt = text
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand what you said.")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))

# call the function


def common_strings(list1, list2):
    # Convert the lists to sets to find the common elements
    set1 = set(list1)
    set2 = set(list2)
    # Find the intersection of the sets to get the common elements
    common_set = set1.intersection(set2)
    # Convert the set back to a list
    common_list = list(common_set)
    return common_list

#       0          1        2       3       4        5        6        7       8       9        10
c = ['delete', 'create', 'search','copy', 'pest', 'manage', 'move', 'break', 'list', 'select', 'open']
while True:
    text = voice_to_text()
    try:
        a = text.split()    
        b = common_strings(a, c)
        separator = ''
        inpt = separator.join(b)
   #      print(inpt)
        if inpt == c[0]:
            try:
                delete()
            except Exception as dlltt:
                text_s("faild while deleting")
                # ............................................................................................................................
        elif inpt == c[10]:
            try:
                 
             substring="current"
             if inptttt.find(substring) != -1:
                 curtdirt=os.getcwd()
                 open_file(curtdirt)
             else:    
             
                 open_file(destination_path)
            except Exception as opnnn:
                text_s("something is wrong while opening")                
        elif inpt == c[8]:
            try:
                substring="current"
                if inptttt.find(substring) != -1:
                 curtdirt=os.getcwd()
                 kkkkk=os.listdir(curtdirt)
                 display_list(kkkkk)
                 
                # 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 
                else: 
                    kkkkk=os.listdir(destination_path)
                    display_list(kkkkk)
            except Exception as glfaf:
                    text_s("somthing is missing while displayig")               
        elif     inpt == c[1]:
            try:
                text_s('enter the new folder name')
                fold_creat = input("enter the new folder name")
                creat_folder(fold_creat)
                text_s("success")
            except Exception as crtfld:
                text_s("faild while creating a folder")
        elif inpt == c[2]:
            try:
                destination_path = search()
                print(destination_path)
                copy_copy = destination_path
            except Exception as srchtpy:
                text_s("dint get anything")
        elif inpt == c[3]:
            try:
                copy_copy = search()
                text_s("can search if you want")
            except Exception as cpy:
                text_s("file dose not exist while searching")
    
            print("copy")
        elif inpt == c[4]:
            try:
                past_fo_fi(copy_copy)
            except Exception as pts:
                text_s("first you have to copy")
    
            print("pest")
    # this line will detect the folder name frome the input only workon current folder
        elif inpt == c[9]:
            # ////////////////////////////////////////////////////////////////////////////////////////
            try:
                select_a = get_list_files_and_folders()
                select_k = inptttt.split()
                print(inptttt)
                out = common_strings(select_a, select_k)
                print(out)
                select_my_string = ''.join(out)
                print(select_my_string)
                destination_path = searcht(select_my_string)
                print(destination_path)
                print("select")
            except Exception as selcttttt:
                text_s("problem while selecting")    
        elif inpt == c[5]:
            try:
                substring = 'current'
                substring2 = 'selected'
                if inptttt.find(substring) != -1:
                    pttt = os.getcwd()
                    manage(pttt)
                    text_s("folder has been managed")
                    listcurrentdir()
                #   this block required selected path to get exicuted..................................................................
                elif inptttt.find(substring2) != -1:
                    manage(destination_path)
                    text_s("folder has been managed")
                    listcurrentdir()
    
                print("maage")
            except Exception as kk:
                pass
                        # 
        elif inpt == c[6]:
            try:
                substring = 'back'
                substring2 = 'destination'
                if inptttt.find(substring) != -1:
                    move_back()
                    listcurrentdir()
                #  this block required selected path to get exicuted..................................................................
                elif inptttt.find(substring2) != -1:
                    move_to_directory(destination_path)
                    listcurrentdir
            except Exception as z:
                text_s("you have to select the destination path")
    
        elif inpt == c[7]:
            print("break")
            break
    except Exception as brkkk:
        pass
        # m
    