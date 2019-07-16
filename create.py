
#!usr/bin/env python3

import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
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
	
	# Create a GitHub instance
	user = Github(username, password).get_user()
	user.create_repo(repositoryName)

	print("GitHub repo: {} successfully created\n".format(repositoryName))

if __name__ == "__main__":
	create()
