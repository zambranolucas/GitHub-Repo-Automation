#!/bin/bash

source ~/Documents/Projects/projectInitializationAutomation/.env

function git-create(){
	python3 ~/Documents/Projects/projectInitializationAutomation/create_v2.py $1
	cd $FILEPATH$1
	echo "# "$1 >> README.md
	git init
	git add .
	git commit -m "Initial commit"
	git remote add origin git@github.com:$USERNAME/$1.git
	git push -u origin master
	code .
}

function git-remove(){
	python3 ~/Documents/Projects/projectInitializationAutomation/delete.py $1
}