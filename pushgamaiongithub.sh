#!/bin/bash
# Read informations on keyboard
read -p "User Name : " uname
read -p "Password : " passwd
read -p "Your email adresse : " email
read -p "Description of commit : " descriptioncommit

# Set authentication
git config --global user.email '$email'
git config --global user.name '$uname'
git config --global user.passwd '$passwd'
# create a file, then add it to stage
git init
git add .
git commit -m '$descriptioncommit'
git remote remove origin
git remote add origin https://github.com/ernestfotseu/gamairoot-ce.git
git pull origin main --rebase
git remote -v
git push origin main         # push to github