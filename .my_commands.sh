
#!/bin/bash

# set variables to be used in the script
source ~/Documents/Learning/Programming/Python/GitHub-Repo-Automation/.env

# function git-init(){
# 	python3 ~/Documents/Learning/Python/GitHub-Repo-Automation/init.py
# }

function git-create(){
	python3 ~/Documents/Learning/Programming/Python/GitHub-Repo-Automation/create.py $1
	cd ./$1
	#echo "# "$1 >> README.md
	git init
	git add .
	git commit -m "Initial commit"
	git remote add origin git@github.com:$USERNAME/$1.git # set-url instead of add
	git push -u origin master
	# code .
}

function git-remove(){
	python3 ~/Documents/Learning/Programming/Python/GitHub-Repo-Automation/delete.py $1
}

function get_path(){
	python3 ~/Documents/Learning/Programming/Python/GitHub-Repo-Automation/os.py
}
