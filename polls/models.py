from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=20)
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 150)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text