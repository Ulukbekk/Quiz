from django.db import models

from quesAPP.models import Question


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    total = models.IntegerField()

    def __str__(self):
        return self.username

class User_question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT,
                             related_name='user')
    question = models.ForeignKey(Question, on_delete=models.SET_DEFAULT,
                                 related_name='user_question')
    is_correct = models.BooleanField()

    def __str__(self):
        return f'{self.user.username} - {self.question.question}'