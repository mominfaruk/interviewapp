from django.db import models

# Create your models here.
class InterviewModel(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=False)

    def __str__(self):
       return self.title
   

class Session(models.Model):
    interview=models.ForeignKey(InterviewModel,on_delete=models.CASCADE)
    title = models.CharField( max_length=255)
    date = models.DateField(auto_now_add=False)
    aplicant=models.ManyToManyField('interview.Applicants',related_name='+')

    def __str__(self):
        return self.title
    
class Applicants(models.Model):
    name = models.CharField(max_length=50)
    session=models.ManyToManyField(Session)

    def __str__(self):
        return self.name