
#!usr/bin/env python3

import sys
import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def delete_repo():
	repositoryName = str(sys.argv[1])

	# Open and sign in Github
	browser = webdriver.Chrome('/Users/franciscozambrano/Documents/Projects/projectInitializationAutomation/chromedriver')
	browser.get("https://github.com/login")
	pointer = browser.find_element_by_name("login")
	pointer.send_keys(username)
	pointer = browser.find_element_by_xpath("//input[@id='password']")
	pointer.send_keys(password)
	pointer = browser.find_element_by_xpath("//input[@name='commit']")
	pointer.click()

	# Create the new repo on Github
	browser.get("https://github.com/{}/{}/settings".format(username,repositoryName))
	pointer = browser.find_element_by_xpath("//div[@class='Box Box--danger']/ul/li[4]/details/summary")
	pointer.click()
	pointer = browser.find_elements_by_xpath("//input[@class='form-control input-block']")[2]
	pointer.send_keys(repositoryName)
	
	try:
		pointer = browser.find_elements_by_xpath("//button[@class='btn btn-block btn-danger']")[3]
		pointer.click()
	except NoSuchElementException as exception:
		print(exception)
		print("Element not found")
	except ElementNotInteractableException as exception:
		print(exception)
		print("Element not interactable")
	else:
		print("GitHub repo: {} successfully deleted\n".format(repositoryName))

if __name__ == "__main__":
	delete_repo()
