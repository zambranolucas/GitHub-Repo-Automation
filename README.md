# git-create Automation

Easily create and initialize a GitHub project with a single command.
'git-create' creates a new directory on your machine, initializes a git repo with a README and pushes it to the configured GitHub account.

## Setup
This project requires Python3, PIP and python-dotenv.
You'll also need to ensure yoru SSH keys are store in Github fot the machine you're creating projects from.


## Installation
	1. Clone this project
	2. Navigate to this project directory
	3. Copy the '.env.example' file to a new '.env' file and update the values.
	4. And then run each of the following commands:

	'''
	pip install -r requirements.txt

	source .my_command.sh
	'''
	5. ***Optional**: Add to your '~/.bash_profile' the following command 'source /path/to/this/project/.my_command.sh' if you want to run the new command whenever you open a new terminal window.


## Usage
To run the script type in 'git-create <name of your new project>'
