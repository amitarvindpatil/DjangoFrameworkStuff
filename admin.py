# admin Site
# one of most powerful part in django framework is the auto admin interface,
# it read metadata from your modules to provide quick, model-centic interface where tursted user manage the web Site
# the admin can handdle the all authentication from this interface


from myproject.myapp.models import Author
from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
