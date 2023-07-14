from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.title} | author: {self.author} | publish date: {self.publication_date.strftime("%Y-%m-%d")}'


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return f"name: {self.name} | bio: {self.bio}"


# class Comment(models.Model):
#     post = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     content = models.TextField()
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f'author: {self.author} | content: {self.content} | date: {self.date.strftime("%Y-%m-%d")}'
