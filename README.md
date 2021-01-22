# Password Manager Website
- Html
- CSS
- Django
- Python

Currently, it uses the master account password to encrypt the stored passwords **twice.** Even in the event of a large data breach in production, where all passwords are leaked, the passwords would still be **very** secure. 

The navbar adapts to whether the user is logged in or not

### How the project behaves:
<image src="https://github.com/ShaneWD/PasswordManagerWebsite/blob/master/demo.gif">
  
###### Demo video is for release v1.1 ( https://github.com/ShaneWD/PasswordManagerWebsite/releases/tag/v1.1 )

## How to set up project (Windows CMD)
###### create virual environment 
```
virtualenv project_name
```
###### change directories to virual environment 
```
cd project_name
```
###### activate virual environment 
```
project_name\activate
```
###### clone the project
```
git clone https://github.com/ShaneWD/PasswordManagerWebsite.git
```
###### change directories into the project
```
cd PasswordManagerWebsite
```
###### install the necessary python packages
```
pip install requirements.txt
```
###### setup SQLite database
```
python manage.py migrate
```
###### start the test server 
```
python manage.py runserver
```

