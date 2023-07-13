from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.title} | author: {self.author} | publish date: {self.publication_date.strftime("%Y-%m-%d")}'


class Author(models.Model):
    pass


class Comment(models.Model):
    pass
