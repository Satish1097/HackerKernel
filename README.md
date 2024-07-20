//Steps to run the project

Create a Directory
mkdir My_Directory
cd My_Directory

//Clone Repository

git clone https://github.com/Satish1097/HackerKernel.git

//Virtual invironment

pip install virtualenv
python -m venv env

//activate Virtual environment env
for windows
env/scripts/activate

//Install Django dependencies
cd Library_Management
pip install django
pip install pandas openpyxl


//Initialization

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

//Run Application

python manage.py runserver


if there is any issue feel free to connet 
M: +91 -776-201-9670
Email: 2019kumarsatish2019@gmail.com
