from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import *
from tkinter import filedialog
import os
from tkinter import messagebox
import tkinter.font


f_name = ""
root = Tk()
root.title('GAMEOPHILE PRODUCTIONS')
root.geometry('1000x700')
root.config(bg="black")
root.resizable(False, False)

f = 0


def status_ping(str):

    if len(str) > 0:
        screen.insert(END, str + "\n")


def begin():
    global f
    global f_name

    f_name = str(input_file_name.get())
    open(f_name, mode='a').close()

    print(f_name)
    f = open(str(f_name), 'a+')
    #messagebox.showinfo("Complete", "File Succesfully Updated")
    status_ping("Changes Updated Succesfully on "+f_name)


def import_libs():
    global f_name
    global f
    f.write("from selenium import webdriver")
    f.write("\n")
    f.write("from selenium.webdriver.common.keys import Keys")
    f.write("\n")
    f.write("from time import sleep")
    f.write("\n")
    f.write("\n")
    button_import_lib.config(state=DISABLED)
    status_ping("Imported all necessary libraries in "+str(f_name))
    begin()


def import_driver(location_chromedriver, isHeadless=False):
    global f
    f.write("options = webdriver.ChromeOptions()")
    f.write("\n")

    if(isHeadless):
        f.write("options.add_argument('--headless')")
        f.write("\n")
        f.write("options.add_argument('--no-sandbox')")
        f.write("\n")

    f.write("options.add_argument('window-size=1200x1040')")
    f.write("\n")
    f.write("driver = webdriver.Chrome("+"executable_path=\"" +
            str(location_chromedriver)+"\",options = options)")
    f.write("\n")

    status_ping("ChromeDriver Imported")


def go_to_site():
    url = go_to_site_input.get()
    global f
    f.write("driver.get(\'"+str(url)+"\')")
    f.write("\n")
    status_ping("Driver opens the site :"+str(url))
    begin()


def wait():
    seconds = str(wait_input.get())
    global f
    f.write('sleep('+str(seconds)+')')
    f.write("\n")
    status_ping("Delay for "+seconds+" seconds added")

    begin()


def action(element_type, element_type_name, element_action):
    global f
    f.write("driver.find_element_by_"+str(element_type) +
            "(\""+str(element_type_name)+"\")."+str(element_action))
    f.write("\n")

    status_ping("Performed "+element_action+" on " +
                element_type+" with a value of "+element_type_name)


def quit():
    global f
    f.write("driver.quit()")
    f.write("\n")
    status_ping("Quitted Active Drivers")
    begin()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to close SandAutoWeb?"):
        root.destroy()


def dir_chromedriver_loc():
    directory = str(askopenfile())
    dir1_ins1 = directory.index("name='")
    dir1_ins2 = directory.index("'", dir1_ins1+7)
    dir1 = directory[dir1_ins1+6:dir1_ins2]
    print(dir1)
    import_driver(dir1, False)
    begin()
    btn_loc_driver.config(state=DISABLED)


def action__():
    action(str(action_input_identity.get()), str(
        action_input_id_value.get()), str(action_input_id_act.get()))

    begin()


Desired_font_heading = tkinter.font.Font(
    family="Comic Sans MS",  size=30, weight="bold")
Desired_font_usual = tkinter.font.Font(
    family="Comic Sans MS",
    size=14,
    weight="bold"
)
label_heading = Label(text="SandAutoWeb", fg="white",
                      bg="black", font=Desired_font_heading)
label_heading.place(x=220, y=20)

button_import_lib = Button(root, height=3, width=40, text="Import All Packages", transition=None,
                           bg="grey", command=import_libs, font=Desired_font_usual)
button_import_lib.place(x=150, y=170)

input_file_name_lbl = Label(
    text="Save file as:", bg="black", fg="white", font=Desired_font_usual)
input_file_name_lbl.place(x=100, y=110)
input_file_name = Entry()
input_file_name.place(x=200, y=110)

input_file_name_btn = Button(
    text="Save", width=10, height=2, command=begin, font=Desired_font_usual)
input_file_name_btn.place(x=400, y=100)


label_r1 = Label(text="Choose Location of driver:",
                 fg="white", bg="black", font=Desired_font_usual)
label_r1.place(x=100, y=250)
btn_loc_driver = Button(text="Select Directory",
                        command=dir_chromedriver_loc, width=20, height=2, font=Desired_font_usual)
btn_loc_driver.place(x=300, y=245)


go_to_site_lbl = Label(text="Go To Site:", bg="black",
                       fg="white", font=Desired_font_usual)
go_to_site_lbl.place(x=100, y=300)
go_to_site_input = Entry()
go_to_site_input.place(x=200, y=300)

go_to_site_btn = Button(
    text="Save This Step", width=12, height=2, command=go_to_site, font=Desired_font_usual)
go_to_site_btn.place(x=400, y=294)


action_lbl = Label(text="Actions:", bg="black",
                   fg="white", font=Desired_font_usual)
action_lbl.place(x=100, y=350)


action_input_identity_label = Label(text="Identifier Type :", bg="black",
                                    fg="white", font=Desired_font_usual)
action_input_identity_label.place(x=200, y=350)

action_input_identity = Entry()
action_input_identity.place(x=350, y=350)

action_input_id_value_label = Label(text="Identifier Value :", bg="black",
                                    fg="white", font=Desired_font_usual)
action_input_id_value_label.place(x=200, y=380)

action_input_id_value = Entry()
action_input_id_value.place(x=350, y=380)


action_input_id_act_label = Label(text="Identifier Action :", bg="black",
                                  fg="white", font=Desired_font_usual)
action_input_id_act_label.place(x=200, y=410)

action_input_id_act = Entry()
action_input_id_act.place(x=350, y=410)


action_btn = Button(
    text="Add Action", width=10, height=2, command=action__, font=Desired_font_usual)
action_btn.place(x=80, y=380)

wait_lbl = Label(text="Delay:", bg="black",
                 fg="white", font=Desired_font_usual)
wait_lbl.place(x=100, y=500)
wait_input = Entry()
wait_input.place(x=150, y=500)

wait_btn = Button(
    text="Add Delay", width=10, height=2, command=wait, font=Desired_font_usual)
wait_btn.place(x=350, y=497)

quit_btn = Button(
    text="QUIT Drivers", width=10, height=2, command=quit, font=Desired_font_usual)
quit_btn.place(x=200, y=550)

scroll_bar = Scrollbar(root, orient=VERTICAL)
scroll_bar2 = Scrollbar(root, orient=HORIZONTAL)
screen = Listbox(height=30, width=40, yscrollcommand=scroll_bar.set,
                 font=Desired_font_usual, selectmode=MULTIPLE)

screen.configure(state=NORMAL)
screen.place(x=600, y=20)

scroll_bar.configure(command=screen.yview)
scroll_bar.pack(side=RIGHT, fill='y')

scroll_bar2.pack(side=BOTTOM, fill='x')


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
