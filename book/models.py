from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User





class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)  # New attribute

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='publisher_images/', null=True, blank=True)  # New attribute

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='author_images/', null=True, blank=True)  # New attribute

    def __str__(self):
        return self.name





from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    national_number = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    liked_books = models.JSONField(default={})


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email








from django.contrib.auth import get_user_model
User = get_user_model()
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    description = models.TextField()
    price = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    page_count = models.PositiveIntegerField()
    average_rating = models.FloatField()
    is_available = models.BooleanField(default=True)
    
    def default_liked_by():
        return {}
    
    likes = models.IntegerField(default=0)





from django.db import models
from django.utils import timezone

class Comment(models.Model):
    text = models.TextField()  # Text of the comment
    email = models.EmailField()  # Email of the commenter
    name = models.CharField(max_length=100)  # Name of the commenter
    date = models.DateTimeField(default=timezone.now)  # Date and time of the comment (automatically set to current time)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.text  # This will display the text of the comment in the admin panel

    class Meta:
        ordering = ['-date']  # Display comments in descending order of date (newest first)


class Request(models.Model):
    national_id = models.CharField(max_length=20)
    email = models.EmailField()  # Email of the commenter
    name = models.CharField(max_length=100)  # Name of the commenter
    phonenumber = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
