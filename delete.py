
#!usr/bin/env python3

import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def delete_repo():
	repositoryName = str(sys.argv[1])
	
	# Create a GitHub instance
	user = Github(username, password).get_user()
	repo = user.create_repo(full_name=repositoryName)

	repo.delete()
	print("GitHub repo: {} successfully deleted\n".format(repositoryName))

if __name__ == "__main__":
	delete_repo()
