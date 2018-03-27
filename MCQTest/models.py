from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=15)
    phone_number = models.IntegerField('Mobile Number')
    address = models.TextField('Address')
    country = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    pin_code = models.IntegerField('Pin_Code')
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    Quetion_Category = models.CharField(max_length = 200, default = 'General')
    Short_Cut = models.CharField(max_length = 10, default = 'GL')
    def __str__(self):
        return self.Quetion_Category

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question.question_text;

class TestSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    schedule_date = models.DateTimeField()
    attended = models.BooleanField(default = False)
    def __str__(self):
        return self.user.username
    
