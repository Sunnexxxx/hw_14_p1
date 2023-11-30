from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title




