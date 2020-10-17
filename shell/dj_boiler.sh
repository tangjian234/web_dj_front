

project_name=$1
app_name=$2

echo $project_name
echo $app_name
echo $project_name"_env"

# 1. build virtural env 
source ~/.local/bin/virtualenvwrapper.sh
mkvirtualenv $project_name"_env"

# 2. create project 
#django-admin startproject $project_name
#cd $project_name
#python3 manage.py startapp $app_name 