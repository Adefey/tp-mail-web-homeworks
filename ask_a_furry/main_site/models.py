from django.db import models
from django.utils import timezone

class Tag(models.Model):
    text = models.CharField(max_length=30, blank=True)
    @classmethod
    def create(cls, text):
        tag = Tag(text = text)
        return tag


class User(models.Model):
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    registration_date = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=0, blank=True, null=True)
    @classmethod
    def create(cls, email, username, password):
        user = User(email=email, username=username, password=password)
        return user

class Question(models.Model):
    header = models.CharField(max_length=128)
    full_text = models.CharField(max_length=512)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+')
    date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, default=None, blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True, null=True)

    @classmethod
    def create(cls, header, full_text, author, tags):
        tags_models = [Tag.create(tag) for tag in tags]
        question = Question(header=header, full_text=full_text, author=author)
        return question


class Answer(models.Model):
    full_text = models.CharField(max_length=128)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+')
    date = models.DateTimeField(default=timezone.now)
    is_correct = models.BooleanField()
    rating = models.IntegerField()
