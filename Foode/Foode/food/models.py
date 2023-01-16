from django.db import models

# Create your models here.


class Food(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    address = models.CharField(max_length=150, null=True, blank=True)
    econtact = models.CharField(max_length=15) 

    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "food"