# Github Repo Automation

Easily create, initialize and remove a GitHub project with a single command.  
`git-create` creates a new directory on your machine, initializes a git repo with a README and pushes it to the configured GitHub account.  
`git-remove` removes from GitHub your repo in an easy way by a single command.

## Setup
This project requires `Python3`, `PIP` and `python-dotenv`.  
You'll also need to ensure your SSH keys are stored in Github for the machine you're creating projects from.


## Installation
1. Clone this project
2. Navigate to this project directory
3. Copy the *.env.example* file to a new *.env* file and update the values.
4. Eventually change on `.my_commands.sh` with your path to this project.  
5. And then run each of the following commands:  
   `pip install -r requirements.txt`  
   `source .my_command.sh`
6. **Optional**: Add to your `~/.bash_profile` the following command `source <path to this project>/.my_command.sh` if you want to run the new commands whenever you open a new terminal window.


## Usage
There are 2 version either working for each command.  
To run the script type in `git-create <name of your new repo>` if you want to create a new repo.  
Instead if you want to delete it type in `git-remove <name of your repo>`.

