# Templates
# Templates are contain static part of HTML page
# create the template directory and subdirectory for creating HTML pages
# Django need to know about the templates by editing the DIR key inside the Template Directory in Setting.py file

# How to communicate the HTML template with View.py or how the inject content into HTML
# - By using render() function inside of View.py file

# setting.py file
from django.shortcuts import render
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abs(__file__)))
Template_DIR = os.path.join(BASE_DIR, "templates")

# after tha we declare the "Template_DIR" name in Template Directory in setting.py file

# add content in HTML file
{{data}}

# view.py


def index(request):
    my_dict = {"data": "Output is here!"}
    return render(request, 'index.html', context=my_dict)
