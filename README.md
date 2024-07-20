#Prerequisites
Python Installed
Git Installed

#Setup Instructions

#Create a Directory: 

mkdir My_Directory
cd My_Directory

#Clone Repository:

git clone https://github.com/Satish1097/HackerKernel.git

#Create and Activate a Virtual Environment:

pip install virtualenv
python -m venv env
# For Windows
env\Scripts\activate
# For macOS/Linux
source env/bin/activate


#Install Django Dependencies:

cd Library_Manage
pip install django
pip install pandas openpyxl

#Initialization

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

#Run Application

python manage.py runserver

If you encounter any issues, feel free to reach out:

M: +91 -776-201-9670
Email: 2019kumarsatish2019@gmail.com


