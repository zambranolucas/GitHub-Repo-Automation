# python3 -m venv env, non e' necessario il virtualenv il problema stava nel file sh in utilizzavo python invece di python3
# source env/bin/activate


#!usr/bin/env python3

import sys
import os
import time
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

homedir = os.getenv("FILEPATH")
path = os.path.expanduser(homedir)
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def create():
	repositoryName = str(sys.argv[1])

	try:
		# Create target Directory
		os.mkdir(path + repositoryName)
		print("... Local directory " + repositoryName + " succesfully created.\n")
	except OSError as err:
		print("! Local directory " +  repositoryName + " already exists\n")
	
	# Open and sign in Github
	browser = webdriver.Chrome()
	browser.get("https://github.com/login")
	pointer = browser.find_element_by_name("login")
	pointer.send_keys(username)
	pointer = browser.find_element_by_xpath("//input[@id='password']")
	pointer.send_keys(password)
	pointer = browser.find_element_by_xpath("//input[@name='commit']")
	pointer.click()

	# Create the new repo on Github
	browser.get("https://github.com/new/")
	pointer = browser.find_element_by_id("repository_name")
	pointer.send_keys(repositoryName)
	pointer = browser.find_element_by_css_selector("button.first-in-line ")
	pointer.submit()
	#time.sleep(4) # ferma l'esecuzione della chiusura dovuta al fully-load event della pagina innescata dal browser.get() 
	
	print("GitHub repo: {} successfully created\n".format(repositoryName))

if __name__ == "__main__":
	create()
