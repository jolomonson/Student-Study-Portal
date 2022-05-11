# Student-Study-Portal
With varieties of Learning Materials, this Student Study Portal provides an efficient and effective way students take notes, read books, take homeworks and so much more with different learning APIs (Youtube, Wikipedia, Dictionary etc) embedded in the application.

# Deployed App (Production mode):
https://studentstudyportal1.herokuapp.com/
# Local Server (Development mode):
http://127.0.0.1:8000/
# Local Server (Admin):
http://127.0.0.1:8000/admin
# Application Setup
## - Cloning the Repository
Open a command prompt on your PC and run the command below:
> git clone https://github.com/JolomonSon/Student-Study-Portal.git
## - Installing requirements
Before installing the requirements, you need to have python installed on your PC.
[Python Setup and Installation](https://realpython.com/installing-python/).
Open the cloned application (folder) and run the command below to install all requirements for the application.
> pip install -r requirements.txt
## - Settings Configurations
Now you need to make a few changes in your settings.py file. 
Open your settings.py which should be located in your projects file and follow the instructions in Line 30, 50, 143 respectively and save the file.
## - Running local server
Start your application using the following command in your command prompt:
> python manage.py runserver
## - Local Server
You can access your local server using this address on any web browser:
http://127.0.0.1:8000/
## - Local Server (admin)
Before you access the admin dashboard, you need to create a superuser.
> python manage.py createsuperuser
After following instructions of creating username, email address and password, you can access your admin dashboard with your login details
## Documentation
You can check up django documentation page for any further information.
[Django Docs](https://docs.djangoproject.com/en/4.0/).
