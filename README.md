A place to practice git and GitHub
--------------
Rachael Stickland
--------------

TEST!!!!!!!! 
ANOTHER TEST !!!!!

This repository contains two bash scripts that pre-process a T1-weighted MRI dataset.
Don't worry about doing anything wrong - this is a place for practicing and permissions are set so you cannot change the original code without my approval. 

Please read this page on the lab website before trying the steps below: https://sites.northwestern.edu/anvil/wiki/lab-coding/git/

This practice is written for MacOS.
To do this practice you need git configured on your computer, and a GitHub account. 
You will also need a good text editor, like Atom. It will help if you can get Atom to open from the terminal. 

1. *On GitHub*: Copy the address of the repo https://github.com/BrightLab-ANVIL/Practice.git
2. *Locally*: Clone this repo to your local machine.   **git clone https://github.com/BrightLab-ANVIL/Practice.git**
3. *Locally*: Make a new branch  - this is where you will do any edits. **git branch [new-branch]**
4. *Locally*: Move to your new branch **git checkout [new-branch]**

*Optional*: Try to run the code, locally. You will need AFNI and FSL installed. Run the scripts from your terminal like:
x.T1_bet *input1* *input2* and x.T1_seg *input1* *input2*

5. *Locally*: Make minor changes to one of the files. 
6. *Locally*: Stage these changes **git add [file]** then commit these changes **git commit -m [message]**
7. *Locally*: Check remote 'origin' is what you expect (Should be https://github.com/BrightLab-ANVIL/Practice.git) **git remote -v** 
8. *Locally*: Whilst in new-branch, pull any new changes from origin/master **git pull origin master** 
9. *Locally*: If there are no conflicts from step (7), push changes you made in new-branch  **git push origin [new-branch]** 
10. *On GitHub*: Make a pull request (PR) to compare new-branch and master branch. One person needs to review this PR.
11. *On GitHub*: Once the PR has been approved, you should merge the new-branch into the master, AND delete the new-branch. 
12a. *Locally*: Delete new-branch **git branch -d [new-branch]**  OR update it (12b)
12b. *Locally* Whilst in new-branch, make sure it is up to date with origin/master on GitHub. **git pull origin master** 
13. *Locally*: Whilst in your local master branch, make sure it is up to date with the origin/master on GitHub. **git pull origin master** 

IMPORTANT NOTES
--------------

Some of the git commands you can do in Atom (text editor) but some you may have to do on the terminal. 
There are other git clients, and there is GitHub Desktop that may help with this process, using GUIs instead of terminal.

*Branches*
See these as temporary places to do edits. People should not typically have permanent branches on the GitHub repo. Once the changes have been merged, the branch can be deleted (on GitHub and locally). 

*Permissions*
The master branch on ANVIL GitHub will be protected. This means that people cannot push to this branch, but can only do pull requests that require at least one reviewer. Other branches will not be protected. Everyone in the organization will have write privileges, so don't edit other people's branches without permission! 

*Fetch and merge*
An alternative "safer" way to do **git pull** is to do **git fetch** then **git merge**.
