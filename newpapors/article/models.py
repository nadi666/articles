from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50, null=True)
    desc = models.TextField()
    date_number = models.DateField('data')

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    connect = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor_name = models.CharField(max_length=50, null=True)
    text = models.TextField()
    data_comment = models.DateField('data')

    def __str__(self):
        return str(self.autor_name)