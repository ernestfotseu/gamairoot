#!/bin/bash
# Read informations on keyboard
read -p "User Name :" username
read -p "Password :" passwd
read -p "Your email adresse :" email
read -p "Description of commit :" descriptioncommit

# Set authentication
git config --global user.email '${email}'
git config --global user.name '${username}'
git config --global user.passwd '${passwd}'
# create a file, then add it to stage
git init
git add .
echo "*****Commit description : ${descriptioncommit}*****"
git commit -m '${descriptioncommit}'
echo "*****Remove old origin*****"
git remote remove origin
echo "*****Add origin*****"
git remote add origin https://github.com/ernestfotseu/gamairoot-ce.git
echo "*****Pull github origin*****"
git pull origin main --rebase
git remote -v
echo "*****Push data*****"
git push origin main         # push to github