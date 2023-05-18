from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,null=True,blank = True)
    mobile=models.CharField(max_length=10,null=True,blank = True)
    email=models.CharField(max_length=20,null=True,blank = True)
    password=models.CharField(max_length=50,null=True,blank = True)
    address=models.CharField(max_length=50,null=True,blank = True)

class Skill(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="skills")
    skills=models.CharField(max_length=50)