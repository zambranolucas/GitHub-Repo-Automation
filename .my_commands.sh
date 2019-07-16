#!/bin/bash

source ~/Desktop/Projects/projectInitializationAutomation/.env

function git-create(){
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

function git-remove(){
	python3 ~/Desktop/Projects/projectInitializationAutomation/delete_v2.py $1
}