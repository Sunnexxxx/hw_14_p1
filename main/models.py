from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

