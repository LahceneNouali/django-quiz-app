from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=255)
    status = models.CharField(max_length=25, default='Not answered')
    note = models.PositiveIntegerField(default=0)
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.TextField(max_length=4000)
    choose = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
