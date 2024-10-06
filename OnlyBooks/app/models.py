from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class User(AbstractUser):
    name = models.CharField(max_length=150)
    wishlisted_books = models.ManyToManyField('Book', related_name="wishlisted_by")
    favourite_tags = models.ManyToManyField('Tag', related_name="favourited_by")

    # Fix group and permissions related_name clashes
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Custom related_name for groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Custom related_name for permissions
        blank=True
    )



class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    time_range_start = models.DateTimeField()
    time_range_end = models.DateTimeField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.event_name