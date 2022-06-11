RESTFUL API

Let’s say you’re trying to find images of nature on Unsplash.com. You open up Unsplash.com and type “Nature” in the search field, hit enter and you see list of various photos of nature. A REST API works in a similar way.

An API is an Application Programming Interface. It is a set of rules that allow programs to talk to each other. Developers create API on the server and allow the client/frontend to talk to it.

REST determines how the API is going to look like. It stands for “Representational State Transfer”. REST consists of a set of instructions that the developer has to follow when they are developing API.
One of these rules states that you should be able to get a piece of data when you click on a URL. Each URL is called a request while the data sent back to you is called a response.

Why REST API?
Before we get to the main development part, it’s worth considering why would you want to build an API. If someone had explained these basic concepts to me before I started, I would have been so much better off.

A REST API is a standardized way to provide data to other applications. These applications can then use the data however they want. Sometimes, APIs also offer a way for other applications to make changes to the data.

These are a few key options for a REST API request:

GET — The most common option, returns some data from the API based on the endpoint you visit and any parameters you provide.

POST — Creates a new record that gets appended to the database.

PUT — Looks for a record at the given URI you provided. If the exists, update the existing record. If not, create a new record.

DELETE — Deletes the record at the given URI

PATCH — Update the Individual field of the record.

NOTE: The main difference between the PUT and PATCH method is that the PUT method uses the request URI to supply a modified version of the requested resource which replaces the original version of the resource, whereas the PATCH method supplies a set of instructions to modify the resource.

Typically, an API is a window into a database. The API backend handles querying the database and formatting the response, what you receive is a static response, usually in JSON format, or whatever resource you requested.

The process of querying and converting tabular database values into JSON or another format is called SERIALIZATION. When you’re creating an API, the correct serialization of data is the major challenge.

Why Django Rest Framework?
Many frameworks allow you to easily build APIs for blog applications, but we will use only one — the Django REST framework. It’s convenient in many ways and offers the following advantages:

Its Web-browsable API is a huge usability win for developers.
Authentication policies include packages for OAuth1 and OAuth2.
Great Serialization supports both ORM and non-ORM data sources, A serializer is a component that will convert Django models to JSON objects and vice-versa.
It has extensive documentation and great community support.
In a Django application, you define your structure of the database in the form of models using python. While you can write raw SQL queries, but for the most part, the Django ORM(Object Relation Mapper) handles all the hard and complicated database migrations and queries.

Think of the Django ORM like an accountant, pulling the information you need for you, so you don’t have to go get it yourself.

Main points for creating a REST API in Django.
So based on what we learn, let’s try to find out steps to creating a REST API.

Set-Up Virtual Environment.
Set-Up Django
Create a model for the database that the Django ORM will manage.
Set-Up Django Rest Framework
Serialize the model data from step-3
Create the URI endpoint to view the serialized data.

Extra installed dependencies
1. typing-extensions-  pip install typing-extensions
2. django-rest-framework to enable us to build a restful api
   pip install djangorestframework