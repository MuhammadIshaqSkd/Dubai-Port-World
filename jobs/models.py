from django.db import models

# Create your models here.

class Ad(models.Model):
    type = (
        ('Ad', 'Ad'),
        ('News', 'News'),
    )
    Ad_name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    pub_date=models.DateField()
    TYPE = models.CharField(max_length=50, null=True, choices=type, default='Ad')
    Ad_image= models.ImageField(upload_to="DubaiPortWorld/media",default="")

    def __str__(self):
        return self.Ad_name


class Applicant(models.Model):
    Ap_name=models.CharField(max_length=50)
    adddress=models.CharField(max_length=500)
    country=models.CharField(max_length=90)
    city=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField(default=0)
    zip=models.IntegerField(default=0)

    def __str__(self):
        return self.Ap_name