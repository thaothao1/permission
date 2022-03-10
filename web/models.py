from django.db import models

# Create your models here.
# class User(AbstractUser):
#     username = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)
#     password = models.CharField(max_length=200)
#     USERNAME_FIELD = 'username'
#     REQUEST_FIELDS =[]

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
