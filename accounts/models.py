from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date
# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date, timedelta




class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name    
   
   
Plans_CHOICES = (
    ('Basci', 'Basci'),
    ('p1', 'plan1'),
    ('p2', 'plan2'),
    ('p3', 'plan3'),

)   


SECTOER_CHOICES = (
    ('studies', 'studies '),
 

) 


class Choice(models.Model):
    name = models.CharField(max_length=50 ,choices=SECTOER_CHOICES)

    def __str__(self):
        return self.name
    
    
    
    
class Subscription(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    tittle=models.CharField(max_length=150, blank=True,null=True )
    plan = models.ManyToManyField(Choice)
    start_date = models.DateField()
    end_date = models.DateField()
    activite=models.BooleanField(default=False)
    img_transition = models.ImageField(upload_to='images/',null=True, blank=True)
    
    def __str__(self):
        return f"{self.user}    "
    
  
  
tender_type_choices = (    
    ('Limited national tenders', 'Limited national tenders'),
    ('Open national tenders', 'Open national tenders'),
    ('limited international tenders', 'limited international tenders'),
    ('Open international tenders', 'Open international tenders'),
    ('Limited international consulting', 'Limited international consulting'),
    ('Open international consultation', 'Open international consultation'),   
    ('Open national competition', 'Open national competition'),
    ('Limited National Competition', 'Limited National Competition'),
    ('Notice of qualification', 'Notice of qualification'),
    ('Limited advance national notice', 'LLimited advance national notice'),
    ('Advance national notice', 'Advance national notice'),
    ('Limited advance national and international notice', 'Limited advance national and international notice'),
    ('Extending the deadlines for the limited national tender', 'Extending the deadlines for the limited national tender'),   
    ('Extending the deadlines for the national open tender', 'Extending the deadlines for the national open tender'),
    ('Extending the deadlines for the limited international tender', 'Extending the deadlines for the limited international tender'),
    ('Extension of deadlines for open international tender', 'Extension of deadlines for open international tender'),
    ('Extending the deadlines for the limited national and international tender', 'Extending the deadlines for the limited national and international tender'),  
    ('Extending the deadlines for the national and international open tender', 'Extending the deadlines for the national and international open tender'),
    ('Express interest', 'Express interest'),
    
     
) 
  
class Type_tender(models.Model):
    type_name=models.CharField(max_length=150, blank=True, null=True,choices=tender_type_choices)

    def __str__(self):
        return self.type_name
    
      
  
    
    
    
class tender(models.Model):
    tittle=models.CharField(max_length=150)    
    tittle_ar=models.CharField(max_length=150,blank=True,null=True)    
    start_date = models.DateField(blank=True, null=True)
    end_time=models.DateField()
    state=models.CharField(max_length=150)
    
    city=models.CharField(max_length=150,blank=True, null=True)
    type_Name=models.ManyToManyField(Type_tender)
    
    sectoer = models.ManyToManyField(Choice)
    activity=models.BooleanField(default=False)
    
    def __str__(self):
        return self.tittle  + " in " +  self.state 
    
    
   
   
   
class File(models.Model):
    tender = models.ForeignKey(tender, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='tender/')
    
        



class Archivetender(models.Model):
    tittle=models.CharField(max_length=150)    
    start_date = models.DateField(blank=True, null=True)
    end_time=models.DateField()
    state=models.CharField(max_length=150)
    sectoer = models.ManyToManyField(Choice)
    activity=models.BooleanField(default=False)
    
    def __str__(self):
        return self.tittle  + " in " +  self.state 
    
    
   
   
   
class ArchiveFile(models.Model):
    archive_tender = models.ForeignKey(Archivetender, on_delete=models.CASCADE)
    archive_file = models.ImageField(upload_to='tender/')
    
    
    
