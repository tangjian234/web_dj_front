from django.db import models

# Create your models here.


# In our poll app, we’ll create two models: Question and Choice.
# A Question has a question and a publication date.
# A Choice has two fields: the text of the choice and a vote tally.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# model association :Each Choice is associated with a Question.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
