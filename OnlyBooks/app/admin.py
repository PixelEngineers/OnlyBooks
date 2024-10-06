from django.contrib import admin
from .models import User, Book, Tag, Event

# Register your models here.


admin.site.register(User)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Event)
