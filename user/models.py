from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
class User(AbstractUser):
    GENDER_CHOICES = (
        ('Male', 'M'),
        ('Female', 'F'),
        ('Other', 'O'),
    )
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    district = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to="user/images", blank=True, null=True)
    # password = models.CharField(max_length=128, default='password1234')
    email = models.EmailField(unique=True,null=True)
    is_customer=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    
    
class Login(models.Model):
    username=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=200)
    
    
class AddCategory(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Problem(models.Model):
    name = models.CharField(max_length=255)
    price = models.TextField(null=True)
    # est_time = models.CharField(max_length=50)
    short_description = models.TextField()
    image = models.ImageField(upload_to='problem_images/', null=True, blank=True)
    category = models.ForeignKey(AddCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.TextField()

class Answer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  
    answer=models.TextField() 
    

    
class createBooking(models.Model):
   
    Status_CHOICES=[
        ('appoint','appoint'),
        ('completed','completed'),
        ('onwork','onwork'),
        ('pending','pending'),
    ]
    # booked_problem = models.CharField(max_length=36)  # Assuming it's a UUID
    selected_brand = models.CharField(max_length=255)
    phone_number=models.TextField(max_length=12,default="0")
    booked_date = models.DateTimeField()
    # item_count = models.PositiveIntegerField()
    time_period = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    problem_interval = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=Status_CHOICES,default="appoint")
    # image = models.ImageField(upload_to='problem_images/', null=True, blank=True)
    # Foreign key to the Problem model
    booked_problem = models.ForeignKey(Problem, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.location
    
class Showproblem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    booked_problem = models.ForeignKey(Problem, on_delete=models.CASCADE,null=True)
    
    class Meta:
        abstract = True

    

