#!/bin/bash
# Read informations on keyboard
read -p "User Name : " uname
read -p "Password : " passwd
read -p "Your email adresse : " email
read -p "Description of commit : " descriptioncommit

# Set authentication
git config user.email '$email'
git config user.name '$uname'
git config user.passwd '$passwd'
echo "User is: $uname"
echo "Email is: $email"
# create a file, then add it to stage
git init
git add .
git commit -m '$descriptioncommit'
git remote remove origin
git remote add origin https://github.com/ernestfotseu/gamairoot-ce.git
git pull origin main --rebase
git remote -v
git push origin main         # push to github