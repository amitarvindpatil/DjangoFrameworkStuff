# ORM - Object Relational Mapper
# Defin Data Modules Entirely in Python.You get Dynamic database-access API for Free
# A Model is the single,definative source of information about your data.
# It contains the required field to store your data Generally each maodel map to a single database table

# The Basic
# -Each Module in python class that subclasses django.db.Models.Model
# -Each Attribute of models represent a database field
# -with all if this ,Django gives you automatically generated database-access

# Example
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


# Retriving All objects
all_entries = Entry.objects.all()

# Retriving Perticuler Object
pert_entries = Entry.objects.filter(pub_date__year=2006)
pert_entries = Entry.objects.all().filter(pub_date__year=2006)

# Retrieving a single object with get()
one_entry = Entry.objects.get(pk=1)

# Limiting QuerySets¶
# For example, this returns the first 5 objects (LIMIT 5)
first_five = Entry.objects.all()[:5]

# This returns the sixth through tenth objects (OFFSET 5 LIMIT 5):
five_ten = Entry.objects.all()[5:10]

#  (e.g. SELECT foo FROM bar LIMIT 1), use an index instead of a slice. For example,
#  this returns the first Entry in the database, after ordering entries alphabetically by headline:
op = Entry.objects.order_by('headline')[0]

# Exact Match
op = Entry.objects.get(headline__exact="Cat bites dog")

# Case insensative
Blog.objects.get(name__iexact="beatles blog")
# Like statements
Entry.objects.filter(headline__contains='%')
