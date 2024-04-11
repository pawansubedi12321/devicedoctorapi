from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# class Register(AbstractBaseUser):
#     GENDER_CHOICES = (
#         ('Male', 'M'),
#         ('Female', 'F'),
#         ('Other', 'O'),
#     )
#     username = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=255)  # PhoneNumberField(blank=False, null=False)
#     gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
#     district = models.CharField(max_length=255)
#     profile_image = models.ImageField(upload_to="user/images", blank=True, null=True)
#     password = models.CharField(max_length=128, default='password1234')  
#     # Add a custom user manager
#     objects = BaseUserManager()


    
#     def __str__(self):
#         return self.username

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, phone_number, gender, district, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, phone_number=phone_number, gender=gender, district=district)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone_number, gender, district, password=None):
        user = self.create_user(email=email, username=username, phone_number=phone_number, gender=gender, district=district, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
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
    password = models.CharField(max_length=128, default='password1234')
    email = models.EmailField(unique=True,null=True)

    # Custom user manager
    # objects = BaseUserManager()

    # Set the field which is going to be used for authentication
    USERNAME_FIELD = 'username'
    
    objects = CustomUserManager()
    # Add required fields for create_superuser method
    REQUIRED_FIELDS = ['phone_number', 'gender', 'district','email']
    
    
    is_staff = models.BooleanField(default=False)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username
    
class Login(models.Model):
    username=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=200)
    
    
class AddCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Problem(models.Model):
    name = models.CharField(max_length=255)
    # price = models.TextField()
    est_time = models.CharField(max_length=50)
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
    booked_date = models.DateTimeField()
    item_count = models.PositiveIntegerField()
    time_period = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    problem_interval = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=Status_CHOICES,default="appoint")
    image = models.ImageField(upload_to='problem_images/', null=True, blank=True)
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

    

