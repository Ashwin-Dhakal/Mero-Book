from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse

ST_CHOICES = (
        ('Open', 'Open'),
        ('Reserved', 'Reserved'),
    )
EDITION_CHOICES=(
    ('First','First'),
    ('Second', 'Second'),
    ('Third', 'Third'),
    ('Forth', 'Forth'),
    ('Fifth', 'Fifth'),
    ('Sixth', 'Sixth'),
    ('Seventh', 'Seventh'),
    ('Eighth', 'Eighth'),
    ('Ninth', 'Ninth'),
    ('Tenth', 'Tenth'),

)

class Details(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    Name = models.CharField(max_length=200)
    Class= models.IntegerField(validators=[MaxValueValidator(13), MinValueValidator(1)])
    Publisher= models.CharField(max_length=200)
    Edition= models.CharField(max_length=10, choices=EDITION_CHOICES)
    Status= models.CharField(max_length=10, choices=ST_CHOICES)
    Your_District= models.CharField(max_length=100)
    Ward_number= models.IntegerField(validators=[MaxValueValidator(36), MinValueValidator(1)])
    Phone_number= models.CharField(max_length=100)


    def __unicode__(self):
        return self.Name

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={'id': self.id})

    # def get_delete_url(self):
    #     return reverse("book_detail:delete", kwargs={'id': self.id})





