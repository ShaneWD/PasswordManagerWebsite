# Password Manager Website
- Html
- CSS
- Django
- Python

Currently, it uses the master account password to encrypt the stored passwords **twice.** Even in the event of a large data breach in production, where all passwords are leaked, the passwords would still be **very** secure. 

The navbar adapts to whether the user is logged in or not

### How the project behaves:
<image src="https://github.com/ShaneWD/PasswordManagerWebsite/blob/master/demo.gif">
  
###### This video was created when release v1.0 was published ( https://github.com/ShaneWD/PasswordManagerWebsite/releases/tag/v1.0 )

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
###### install the nessessary python packages
```
pip install requirements.txt
```
###### start the test server 
```
python manage.py runserver
```
###### setup SQLite database
```
python manage.py migrate
```
