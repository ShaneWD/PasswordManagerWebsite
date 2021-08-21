# Password Manager Website
- Html
- CSS
- Django
- Python

Currently, it uses the master account password to encrypt the stored passwords **twice.** Even in the event of a large data breach in production, where all passwords are leaked, the passwords would still be **very** secure. 

The navbar adapts to whether the user is logged in or not

### How the project behaves:
<image src="https://user-images.githubusercontent.com/70982928/130323803-c30e46d0-e6c2-409a-a996-41fab5698c5d.gif">
  
###### Demo video is for release v1.2 ( https://github.com/ShaneWD/PasswordManagerWebsite/releases/tag/v1.2 )

## How to set up project (Windows CMD)
  

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

