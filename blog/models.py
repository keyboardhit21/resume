from django.db import models
from django.db.models import TextField, CharField, DateField, ImageField


class Blog(models.Model):
    title = CharField(max_length=250)
    date = DateField()
    banner = ImageField(upload_to='static/images/article', default='static/images/article/default.jpg')
    thumbnail = ImageField(upload_to='static/images/article', default='static/images/article/default.jpg')
    short_content = TextField(default='such empty...')
    content = TextField()

    def __str__(self):
        return self.title[:100]

