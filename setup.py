from tkinter import *
from tkinter import messagebox

f_name = ""


def begin(filename):
    global f_name

    open(filename, mode='w').close()
    f_name = str(filename)


def import_libs():
    global f_name

    f.write("from selenium import webdriver")
    f.write("\n")
    f.write("from selenium.webdriver.common.keys import Keys")
    f.write("\n")
    f.write("from time import sleep")
    f.write("\n")
    f.write("\n")


def import_driver(location_chromedriver, isHeadless=False):

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


def go_to_site(url):
    f.write("driver.get(\'"+str(url)+"\')")
    f.write("\n")


def wait(seconds):
    f.write('sleep('+str(seconds)+')')
    f.write("\n")


def println(text):
    f.write("print(\""+str(text)+"\")")
    f.write("\n")


def action(element_type, element_type_name, element_action):
    f.write("driver.find_element_by_"+str(element_type) +
            "(\""+str(element_type_name)+"\")."+str(element_action))
    f.write("\n")


def quit():
    f.write("driver.quit()")
    f.write("\n")

                    ### OKAY , SO NOW LET'S TEST THE BOT ###
begin("test.py")  #this creates a test.py file in the working directory with the name provided[here 'test'.py]
f = open(f_name, 'w')

import_libs()     #This imports all the libraries which are necessary for the program 
import_driver("Users/chromedriver.exe")   #This will provide the path of the chromedriver to the selenium webdriver(chromedriver should be downloaded online and should be of the suitable version for your google chrome)
wait(5)   
println("going to the site")    #you might think why it is println and not print, well this does not print anything in this console, rather in the newly generated python file, it puts the print statement
go_to_site("https://tweetdeck.twitter.com/")      #The chromedriver automatically opens the website provided to it(here twitter)
wait(4)
println("Entered login page")     
action("xpath", '/html/body/div[1]/div[3]/div/div[2]/section/div[1]/a', "click()")  #The first parameter shows that the element we want to perform action on is identified using its xpath,the second parameter provides the identifiable xpath and the third parameter provides the action which needs to be performed on it
wait(5)
action("xpath",
       "//*[@id=\\\"react-root\\\"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input",
       "send_keys('username')") #The first parameter denotes that the element we're trying to perform action on is to be identified via its xpath, second paramter provides it the unique xpath of that element, the third parameter asks it to enter the username on the element(the element is an input tag to accept the username)

wait(10) # this will add a sleep function in the output python file !
quit()      #this will close all necessary drivers 
