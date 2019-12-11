# Forms.py
# Django Provide the powerful form library that handdle the rendering form as HTML,validating
# user-submitting data,converting that data to native pathon types,
# Django also provide the way to generate a forms from your existing your models and use those
# forms to create and update data


# forms.py

from .forms import NameForm
from django.shortcuts import render
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


# views.py


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

# HTML page
    <form action = "/your-name/" method = "post" >
    {% csrf_token % }
    {{form}}
    <input type = "submit" value = "Submit" >


</form >
