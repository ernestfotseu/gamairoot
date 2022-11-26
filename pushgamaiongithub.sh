#!/bin/bash
# Read informations on keyboard
username = "ernestfotseu"
read -p "User Name :" usernamespecify
read -p "Your email adresse :" email
read -p "Description of commit :" descriptioncommit

acces_token = "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"

# Set authentication
git config --global user.email "${email}"
git config --global user.name "${username}"
# create a file, then add it to stage
git init
git add .
echo "*****Commit description : ${descriptioncommit}*****"
git commit -m 'User ${usernamespecify} : ${descriptioncommit}'
echo "*****Remove old origin*****"
git remote remove origin
echo "*****Add origin*****"
# git remote add origin https://github.com/ernestfotseu/gamairoot-ce.git
git remote add origin https://${acces_token}@github.com/${username}/gamairoot-ce.git
echo "*****Pull github origin*****"
git pull origin main --rebase
git remote -v
echo "*****Push data*****"
git push origin main