
#!usr/bin/env python3

import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

# homedir = os.getenv("FILEPATH")
homedir = os.getcwd() + '/'
path = os.path.expanduser(homedir)
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def create():
	repositoryName = str(sys.argv[1])

	try:
		# Create target Directory
		os.mkdir(path + repositoryName)
		print("\n... > Local directory " + repositoryName + " succesfully created.\n")
	except OSError as err:
		print("\n... > !Local directory " +  repositoryName + " already exists\n")
	
	# Create a GitHub instance
	user = Github(username, password).get_user()
	user.create_repo(repositoryName)

	print("\n... > GitHub repo: {} successfully created\n".format(repositoryName))

if __name__ == "__main__":
	create()
