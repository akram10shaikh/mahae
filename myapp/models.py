from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person_Detail(models.Model):
    no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_no = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    aadhar_no = models.IntegerField()
    pan_no = models.CharField(max_length=100)

    education = models.CharField(max_length=100)
    university_name = models.CharField(max_length=200)
    date_of_addmission = models.DateField()
    date_of_leaving = models.DateField()

    father_name = models.CharField(max_length=100)
    photo = models.FileField(upload_to='')

    doc_aadhar = models.FileField(upload_to='')
    doc_pan = models.FileField(upload_to='')
    doc_tc = models.FileField(upload_to='')
    doc_election = models.FileField(upload_to='')

    doc_for = models.CharField(max_length=100,null=True)
    progress = models.CharField(max_length=100,null=True,choices=(('Progress','Progress'),('Waiting','Watiting'),('Success','Success')))
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    dateandtime = models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self):
        return self.first_name


class Document_ready(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    person = models.ForeignKey(Person_Detail,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person.first_name
