# Practice

A place to practice git (with code that processes MRI files using bash, AFNI and FSL).
--------------

This repository contains two scripts that pre-process a T1-weighted MRI dataset. 
Use this to practice your git and github skills. 
It assumes you have AFNI and FSL installed.

Run the scripts like:

x.T1_bet *input1* *input2* and 
x.T1_seg *input1* *input2*

Suggested steps:

1. *On GitHub*: fork this repository ('central repo' in git_interactions_schematic.png ) to your own GitHub ('your fork' in
   git_interactions_schematic.png)
2. *On GitHub*: make a new branch  - this is where you will do any edits, not on the master branch. 
3. *Locally*: Clone your fork to your local machine, so it's easy to edit the code.   **git clone [forked-repo-address]**
4. *Locally*: Move to your new branch **git checkout [new-branch-name]**
5. *Locally*: Check origin with **git remote -v** (it should be the address of your fork)
6. *Locally*: Push changes you made back to your fork  **git push origin [new-branch-name]** 
7. *On GitHub*: put in a pull request to compare new-branch of your fork and master-branch of the central repo. 

The person in charge of the central repo will now review your changes, and has the option of merging them into the master branch.

-------------

*If* that all made sense, you might be thinking (1) What if someone updates the master branch on the central repo? and (2) How do I make sure 'master' on GitHub and 'master' on my local machine is up to date with the central repo?

8.  *Locally*: set the upstream remote to be the central repo  **git remote add upstream [central-repo-address]**
9. *Locally*: download the history of changes in the master branch of the upstream remote   **git fetch upstream/master**
10. *Locally*: make sure you are in the master branch, and now merge the changes from the upstream remote  **git merge**  
    upstream/master
11. *Locally*: push change back to the master branch of your fork

--------------

NOTE, the workflow could be simpler/different, for example:

Steps 10 and 11 can be done with one command (git pull) but doing it in two stages is 'safer' . Git fetch allows you to review changes and then decide to merge but git pull fetches and merges in one command.

You could (1) clone the central repo directly to your local machine (2) make a branch in which you do edits *very important that you make a branch* (3) push this branch back to the central repo. Then there will be two branches in the central repo, which can be compared. Even though this seems much simpler, it will likely get messier more quickly. However, this is likely the steps you would take when working on your own individual code, and wanting to back it up to GitHub. 

NOTE, some of the local commands you can do in Atom but some you may have to do on the terminal. There are other git clients, and there is GitHub Desktop that may help with this process. 






