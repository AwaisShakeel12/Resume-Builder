from django.db import models

# Create your models here.

class Resume(models.Model):

    Experience_level = (
        ('one', 'ONE'),
        ('two', 'TWO'),
        ('three', 'THREE'),
        ('four', 'FOUR'),
        ('five', 'FIVE'),
        ('six', 'SIX'),
        ('seven', 'SEVEN'),
        ('eight', 'EIGHT'),
        ('nine', 'NINE'),
        ('ten', 'TEN'),
        ('internship', 'Internship'),
        ('fresh', 'Fresh'),
    )


    template_choice = models.CharField(max_length=20, default='template1')

    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100 , blank=True, null=True)
    email= models.EmailField(max_length=100 , blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
  

    Headline = models.CharField(max_length=100, blank=True, null=True)
    aboutYou = models.TextField(blank=True, null=True)

    eduTitle1 = models.CharField(max_length=100, blank=True, null=True )
    eduInstitute1 = models.CharField(max_length=100, blank=True, null=True)
    edu1Marks1 = models.CharField( max_length=100 ,blank=True, null=True)
    eduStartDate1 = models.DateField(blank=True, null=True)
    
    eduEndDate1 = models.DateField(blank=True, null=True)

    eduTitle2 = models.CharField(max_length=100 , blank=True, null=True)
    eduInstitute2 = models.CharField(max_length=100 , blank=True, null=True)
    edu1Marks2 = models.CharField( max_length=100,blank=True, null=True)
    eduStartDate2 = models.DateField(blank=True, null=True)
    eduEndDate2 = models.DateField(blank=True, null=True)

    eduTitle3 = models.CharField(max_length=100 , blank=True, null=True)
    eduInstitute3 = models.CharField(max_length=100 , blank=True, null=True)
    edu1Marks3 = models.CharField( max_length=100,blank=True, null=True)
    eduStartDate3 = models.DateField(blank=True, null=True)
    eduEndDate3 = models.DateField(blank=True, null=True)


    skil1 = models.CharField(max_length=100,  blank=True, null=True)
    skil2 = models.CharField(max_length=100,  blank=True, null=True)
    skil3 = models.CharField(max_length=100,  blank=True, null=True)
    skil4 = models.CharField(max_length=100,  blank=True, null=True)
    skil5 = models.CharField(max_length=100,  blank=True, null=True)
    skil6 = models.CharField(max_length=100,  blank=True, null=True)

    projectTitle1 = models.CharField(max_length=100 , blank=True, null=True)
    projectDescription1 = models.TextField(blank=True, null=True)


    projectTitle2 = models.CharField(max_length=100 , blank=True, null=True)
    projectDescription2 = models.TextField( blank=True, null=True)
 



    experienceLevel = models.CharField(max_length=100,choices=Experience_level, default=1)

    experienceTitle1 = models.CharField(max_length=100 , blank=True, null=True)
    experienceCompany1 = models.CharField(max_length=100 , blank=True, null=True)  
    expStartDate1= models.DateField(blank=True, null=True)
    expEndDate1 = models.DateField(blank=True, null=True)


    experienceTitle2 = models.CharField(max_length=100 , blank=True, null=True)
    experienceCompany2 = models.CharField(max_length=100 , blank=True, null=True)
    expStartDate2= models.DateField(blank=True, null=True)
    expEndDate2 = models.DateField(blank=True, null=True)


   
   

    








    



    
