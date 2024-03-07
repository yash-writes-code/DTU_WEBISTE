from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError

class MenuItem(models.Model):
    item_name=models.CharField(max_length=50)
    item_price=models.IntegerField()

    def __str__(self):
        return self.item_name

class Event(models.Model):
    name_of_dept=models.CharField(max_length=50)
    date_of_indent=models.DateField()
    date_of_arrangement=models.DateField()
    
    No_of_person=models.IntegerField()
    menu=models.ManyToManyField(to=MenuItem)
    payment_status=models.IntegerField(choices=[(1,"paid"),(0,"pending")])

    bill=models.FileField(blank=True)

    # def save(self,*args, **kwargs):
    #     if(self.payment_status==1):
    #         if(self.bill ==None):
    #             raise ValidationError("You must attach a bill for paid events")
    #         else:
    #             return super(Event,self).save(*args, **kwargs)
    #     else:
    #         return super(Event,self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.payment_status == 1:  # Check if payment_status is "paid"
            if not self.bill:  # Check if a bill file is attached
                raise ValidationError("You must attach a bill for paid events")
        
        # Save the Event instance and continue with the save operation
        return super(Event, self).save(*args, **kwargs)