from django.db import models

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
