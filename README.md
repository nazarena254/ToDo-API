## ToDo-Api

## Description
This is a Django web application that uses rest API build using Django Rest Framework

## Author
Nazarena Wambura.</br>
[Github Account](https://github.com/nazarena254)

### Api route page
![ToDoApi](./todoapp/static/images/apipage.png)
### Admin panel
![ToDoApi](./todoapp/static/images/admin.png)


## User Story
1. View all to-do tasks.
2. Dreate a to do task.
3. Update a to do task.
4. Delete a to do task


## Setup/Installation Requirements
1. Create a folder and cd to it.
2. Clone the repository below with the command `git clone <https option url> .`  <br>
    https://github.com/nazarena254/InstagramClone  
3. Install dependencies in the requirements.txt file `pip install -r requirements.txt` .
4.  Type code . or atom . based on the text editor you have and work on it.   

## Database
1. Set up Database(postgresql),and put your username and password in the code
2. Make migrations
    python3 manage.py makemigrations
3. Migrate
   python3 manage.py migrate 
       
## Running the Application
1. Run main aplication<br>    
   * python3.9 manage.py runserver<br>
    Note: python version will vary in future

## Creating Admins
1. Creating Admin Locally<br>
     python manage.py createsuperuser. Then set username, email & password

2. Creating Django Admin   
     heroku run python manage.py createsuperuser. Then set username, email & password

## Technologies Used
* Python3.9.2 - as backend language
* Django4.0.5 - as a Framework
* Bootstrap4 - for responsiveness & styling 
* PostgreSQL - as database
* Heroku - for deploying app

## Support & Contact Information
For any further inquiries, bugs, contributions or comments, reach me at:<br>
Email:<nancyngunjiri1@gmail.com>

## License
[MIT License](https://github.com/nazarena254/ToDo-API/blob/master/LICENSE)<br>
Copyright (c) 2021 **Nazarena Wambura**