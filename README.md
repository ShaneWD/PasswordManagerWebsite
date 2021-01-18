# Password Manager Website
- Html
- CSS
- Django
- Python

Currently, it uses the master account password to encrypt the stored passwords **twice.** Even in the event of a large data breach in production, where all passwords are leaked, the passwords would still be **very** secure. 

The navbar adapts to whether the user is logged in or not

## Notes:
- The username and password for super user / admin is "admin"

## How to set up project (Windows CMD)
```
virtualenv project_name
```
###### create virual environment 
```
cd project_name
```
###### change directories to virual environment 
```
project_name\activate
```
###### activate virual environment 
```
git clone https://github.com/ShaneWD/PasswordManagerWebsite.git
```
###### clone the project
```
cd PasswordManagerWebsite
```
###### change directories into the project
```
pip install requirements.txt
```
###### install the nessessary python packages
```
python manage.py runserver
```
###### start the test server 
