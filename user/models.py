from django.db import models

# Create your models here.
class Register(models.Model):
    GENDER_CHOICES = (
        ('Male', 'M'),
        ('Female', 'F'),
        ('Other', 'O'),
    )
    username = models.CharField(
        max_length=255
        
    )
    phone_number = models.CharField(max_length=255)  # PhoneNumberField(blank=False, null=False)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    district = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to="user/images", blank=True, null=True)
    
    def __str__(self):
        return self.username

    
class Login(models.Model):
    username=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=200)
    
    
class AddCategory(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Problem(models.Model):
    name = models.CharField(max_length=255)
    price = models.TextField()
    est_time = models.CharField(max_length=50)
    short_description = models.TextField()
    image = models.ImageField(upload_to='problem_images/', null=True, blank=True)
    category = models.ForeignKey(AddCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    user=models.ForeignKey(Register,on_delete=models.CASCADE)
    question=models.TextField()

class Answer(models.Model):
    user=models.ForeignKey(Register,on_delete=models.CASCADE)  
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
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.location
    
class Showproblem(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)

    booked_problem = models.ForeignKey(Problem, on_delete=models.CASCADE,null=True)
    
    class Meta:
        abstract = True

    

