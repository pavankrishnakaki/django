from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=10,unique=True)
    
    name = models.CharField(max_length=30) 
    
    pass_percentage = models.PositiveIntegerField()
    
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} ({})".format(self.name,self.code)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    is_active = models.BooleanField(default=False)
