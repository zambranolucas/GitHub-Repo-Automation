#!/bin/bash

function git-create(){
	source ~/Desktop/Projects/projectInitializationAutomation/.env
	python3 ~/Desktop/Projects/projectInitializationAutomation/create.py $1
	cd $FILEPATH$1
	echo "#"$1 >> README.md
	git init
	git add .
	git commit -m "Initial commit"
	git remote add  git@github.com:$USERNAME/$1.git
	git push -u origin master
	code .
}