## RESTFUL API

Let’s say you’re trying to find images of nature on Unsplash.com. You open up Unsplash.com and type “Nature” in the search field, hit enter and you see list of various photos of nature. A REST API works in a similar way.

An API is an Application Programming Interface. It is a set of rules that allow programs to talk to each other. Developers create API on the server and allow the client/frontend to talk to it.

REST determines how the API is going to look like. It stands for “Representational State Transfer”. REST consists of a set of instructions that the developer has to follow when they are developing API.
One of these rules states that you should be able to get a piece of data when you click on a URL. Each URL is called a request while the data sent back to you is called a response.

#### Why REST API?
Before we get to the main development part, it’s worth considering why would you want to build an API. If someone had explained these basic concepts to me before I started, I would have been so much better off.

A REST API is a standardized way to provide data to other applications.<br/> These applications can then use the data however they want. Sometimes, APIs also offer a way for other applications to make changes to the data.

These are a few key options for a REST API request:

1. GET — The most common option, returns some data from the API based on the endpoint you visit and any parameters you provide.

2. POST — Creates a new record that gets appended to the database.

3. PUT — Looks for a record at the given URI you provided. If the exists, update the existing record. If not, create a new record.

4. DELETE — Deletes the record at the given URI

5. PATCH — Update the Individual field of the record.

###### NOTE:
The main difference between the PUT and PATCH method is that the PUT method uses the request URI to supply a modified version of the requested resource which replaces the original version of the resource, whereas the PATCH method supplies a set of instructions to modify the resource.

Typically, an API is a window into a database. The API backend handles querying the database and formatting the response, what you receive is a static response, usually in JSON format, or whatever resource you requested.

#### Serialization
The process of querying and converting tabular database values into JSON or another format is called SERIALIZATION. When you’re creating an API, the correct serialization of data is the major challenge.
1. 
#### Why Django Rest Framework?<br/>
Many frameworks allow you to easily build APIs for blog applications, but we will use only one — the Django REST framework.

###### It’s convenient in many ways and offers the following advantages:
* Its Web-browsable API is a huge usability win for developers.
* Authentication policies include packages for OAuth1 and OAuth2.
* Great Serialization supports both ORM and non-ORM data sources, A serializer is a component that will convert Django models to JSON objects and vice-versa.
* It has extensive documentation and great community support.
* In a Django application, you define your structure of the database in the form of models using python. While you can write raw SQL queries, but for the most part, the Django ORM(Object Relation Mapper) handles all the hard and complicated database migrations and queries.

Think of the Django ORM like an accountant, pulling the information you need for you, so you don’t have to go get it yourself.

#### Creating a REST API in Django.
So based on what we learn, let’s try to find out steps to creating a REST API.

* Set-Up Virtual Environment.
* Set-Up Django
* Create a model for the database that the Django ORM will manage.
* Set-Up Django Rest Framework
* Serialize the model data from step-3
* Create the URI endpoint to view the serialized data.

#### Extra installed dependencies
1. typing-extensions-  pip install typing-extensions
2. django-rest-framework to enable us to build a restful api-  pip install djangorestframework

### AUTHENTICATION <br/>
Our API works fine now but we don't want just any random person coming to add new merch items.<br/> We can only allow the Admin to add new Items. Let's see how we can do that. <br/> First, we need to generate an access token before we can start setting any permissions.

project/settings.py
```
INSTALLED_APPS = [
    'rest_framework.authtoken'
]
```
We first add 'rest_framework.authtoken' to our INSTALLED_APPS settings.<br/> Remember to migrate the database to add any changes.<br>

project/settings.py
```
#.....
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
```
We then define the DEFAULT_AUTHENTICATION_CLASSES for the rest_frameworkpackage. <br/> Now we can define the URLConf to allow us to get the token.<br>

project/urls.py
```
from rest_framework.authtoken.views import obtain_auth_token
#.......
urlpatterns = [
#.......
    url(r'^api-token-auth/', obtain_auth_token)
]
```
We first import the obtain_auth_token view from the rest_framework.authtoken.views module.<br/> Then we create a new url function and define the route and pass in the view.<br>

We can run this on postman to see how it works. <br/> We create a new POST request and pass in the username and password in the body. <br/> If successful you will receive an access token that you will use for all your POST requests. <br/> Now we can setup the permissions. We will create a new file permissions.py inside our app.

app/permissions.py
```
from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
```
            
- We import the BasePermission base class and SAFE_METHODS. SAFE_METHODS are request methods that do not change the database like the GET method.
- We then create the permission class IsAdminOrReadOnly which will only allow users with admin privileges to perform certain requests.
- We can use the IsAuthenticatedOrReadOnly class if we wanted to allow any authenticated user in our app to add merch items.
- We then create the has_permission method that checks if the request belongs to the SAFE_METHODS.
- This prevents any request other than SAFE_METHODS to be executed only by Admin users.

We then add the permissions to the API view class.<br>

app/views.py
```
from .permissions import IsAdminOrReadOnly
#........
class MerchList(APIView):
#..........
    permission_classes = (IsAdminOrReadOnly,)
```

We add an attribute permission_classes where we pass in the IsAdminOrReadOnly permission class.





