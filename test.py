#THIS IS THE PYTHON FILE WHICH GOT GENERATED


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('window-size=1200x1040')
driver = webdriver.Chrome(executable_path="Users/chromedriver.exe",options = options)
sleep(5)
print("going to the site")
driver.get('https://tweetdeck.twitter.com/')
sleep(4)
print("Entered login page")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/section/div[1]/a").click()
sleep(5)
driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input").send_keys('username')
sleep(10)
driver.quit()
