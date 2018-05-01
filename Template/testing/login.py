from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='/home/yevhenii/Study/Programing/CS_UCU/Official_part/testing/chrome_driver/chromedriver')

usr = input('Enter Email Id:')
pwd = input('Enter Password:')

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
print("Opened facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print("Email Id entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("Password entered")

login_box = driver.find_element_by_id('loginbutton')
login_box.click()

print("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
