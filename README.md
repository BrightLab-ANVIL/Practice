# Practice

A place to practice git and GitHub
--------------

This repository contains two bash scripts that pre-process a T1-weighted MRI dataset.
Don't worry about doing anything wrong - this repo is for practising. 
Please read this page on the lab website first: https://sites.northwestern.edu/anvil/wiki/lab-coding/git/

This practice is written for MacOS.
To do this practice you need git configured on your computer, and a GitHub account. 
You will also need a good text editor, like Atom. 

**Suggested steps**:

1. *On GitHub*: fork this repository ('central repo' in png file) to your own GitHub ('your fork' in png file)
2. *Locally*: Clone your fork to your local machine.   **git clone [forked-repo-address]**
3. *Locally*: Make a new branch  - this is where you will do any edits. **git branch [new-branch-name]**
4. *Locally*: Move to your new branch **git checkout [new-branch-name]**
5. *Locally*: Check origin with **git remote -v** (it should be the address of your fork)

*Optional*: Try to run the code, locally. You will need AFNI and FSL installed. Run the scripts from your terminal like:
x.T1_bet *input1* *input2* and 
x.T1_seg *input1* *input2*

6. *Locally*: Make minor changes to one of the files. Stage these changes **git add [file]** then commit these changes **git commit -m [message]**
7. *Locally*: Push changes you made back to your fork on GitHub  **git push origin [new-branch-name]** 
8. *On GitHub*: put in a pull request to compare [new-branch] of your fork and master-branch of the central repo. 

The person in charge of the central repo will now review your changes, and has the option of merging them into the master branch.

-------------

*If* that all made sense, you might be thinking (1) What if someone updates the master branch on the central repo? and (2) How do I make sure 'master' on GitHub and 'master' on my local machine is up to date with the central repo?

9.  *Locally*: set the upstream remote to be the central repo  **git remote add upstream [central-repo-address]**
10. *Locally*: download the history of changes in the master branch of the upstream remote   **git fetch upstream**
11. *Locally*: make sure you are in the master branch, and now merge the changes from the upstream remote  **git merge upstream/master**
12. *Locally*: push change back to the master branch of your fork

--------------

NOTE, the workflow could be simpler/different, for example:

Steps 10 and 11 can be done with one command (git pull) but doing it in two stages is 'safer' . Git fetch allows you to review changes and then decide to merge but git pull fetches and merges in one command.

You could (1) clone the central repo directly to your local machine (2) make a branch in which you do edits *very important that you make a branch* (3) push this branch back to the central repo. Then there will be two branches in the central repo, which can be compared. Even though this seems much simpler, it will likely get messier more quickly. However, this is likely the steps you would take when working on your own individual code, and wanting to back it up to GitHub. 

NOTE, some of the local commands you can do in Atom but some you may have to do on the terminal. 
There are other git clients, and there is GitHub Desktop that may help with this process. 






