# Urls
# use for mapping between URL path expression to python function(views)
# include() allow us to look  for a match with reguler expression and link back to our application's its own
# url.py. we have to manually add this file

# Application urls.py

from . import views
from django.urls import path
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('abc.urls'))  # import link from curd_application->urls
]

# project Url.py add mannually


urlpatterns = [
    path('bands/', views.band_listing, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/search/', views.band_search, name='band-search'),
]


def band_listing(request):
    """A view of all bands."""
    bands = models.Band.objects.all()
    return render(request, 'bands/band_listing.html', {'bands': bands})


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('add_book', views.add_book, name='add_book'),
    path('delete/<id>/', views.delete, name='delete'),
    path('edit/<id>/', views.edit, name='edit'),
    path('update/<id>/', views.update, name='update'),
    # path('search',views.search,name='search'),

]
