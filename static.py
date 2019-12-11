# Static content
website generally need to serve addtional files such as images, javascript, bootstrap, css files

django.contrib.staticfiles for manage that files
# configure the static files
-Make sure that django.contrib.staticfiles is included in your INSTALLED_APPS.
-define
STATIC_URL = '/static/'
-In your templates
{% load static % }
<img src = "{% static "my_app/example.jpg" %}" alt = "My image" >

-Store your static files in a folder called static in your app. For example my_app/static/my_app/example.jpg.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]


-Serving files uploaded by a user during development¶
-mention below code in urls.py
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA
