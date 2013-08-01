from django.db import models
from django.utils import timezone
import datetime


# Create your models here.


class User(models.Model):
    name= models.CharField(max_length=20)
    email = models.EmailField()

    def __unicode__(self):
        return self.name+'-'+self.email

class Count(models.Model):
    user=models.ForeignKey(User)
    name = models.CharField(max_length=20)
    count=models.IntegerField(default=0)
    last_update = models.DateTimeField()


    def __unicode__(self):
        return self.user.name+'.'+self.name+':'+str(self.count)+' ('+str(self.last_update)+')'

    def recently_updated(self):
        return self.last_update >= timezone.now() - datetime.timedelta(days=7)
