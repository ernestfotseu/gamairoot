#!/bin/bash
ACCES_TOKEN="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"
# Read informations on keyboard
read -p "User Name :" usernamespecify
read -p "Your email adresse :" email
read -p "Description of commit :" descriptioncommit

echo "acces_token=${ACCES_TOKEN}"
# Set authentication
git config --global user.email "${email}"
git config --global user.name "${usernamespecify}"
# create a file, then add it to stage
git init
git add .
echo "*****Commit description : ${descriptioncommit}*****"
git commit -m "User ${usernamespecify} : ${descriptioncommit}"
echo "*****Remove old origin*****"
git remote remove origin
echo "*****Add origin*****"
# git remote add origin https://github.com/ernestfotseu/gamairoot-ce.git
git remote add origin https://${ACCES_TOKEN}@github.com/ernestfotseu/gamairoot-ce.git
echo "https://${ACCES_TOKEN}@github.com/ernestfotseu/gamairoot-ce.git"
echo "*****Pull github origin*****"
git pull origin main --rebase
git remote -v
echo "*****Push data*****"
git push origin main