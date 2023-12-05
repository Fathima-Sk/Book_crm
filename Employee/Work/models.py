from django.db import models

# Create your models here..


class Employee(models.Model):
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.name


#python manage.py makemigrations

#python manage.py migrate

# models:which is used to perform certain actions using data eg:--CRUD(create,read,upadte,delete)

# django default database-sqlite3

# python manage.py shell

# create student 

class student(models.Model):
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    email=models.EmailField(null=True)
    gender=models.CharField(max_length=10)
    place=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
# create employee
    
class Emp(models.Model):

    name=models.CharField(max_length=20)
    place=models.CharField(max_length=30)
    salary=models.PositiveIntegerField()
    contact=models.IntegerField()

# create book

class book(models.Model):
    title=models.CharField(max_length=30)
    auther=models.CharField(max_length=20)
    publication_year=models.PositiveIntegerField()
    genre=models.CharField(max_length=20)

    def __str__(self):
        return self.title
    def __str__(self):
        return self.auther
    def __str__(self):
        return self.genre

