from rest_framework import serializers
from .models import User,Login,AddCategory,Problem,createBooking,Showproblem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =['id','username','phone_number','gender','district','profile_image','is_customer','is_admin']
        
# class UserLoginSerializer(serializers.Serializer):
#     username=serializers.CharField(max_length=255)
#     password=serializers.CharField(max_length=255)
 

class AddCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=AddCategory
        fields=['id','name','image']


class AddProblemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Problem
        fields=('id','name','price','short_description','image','category')
        
class CreateBookingSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=createBooking
        fields=('id','phone_number','booked_problem','selected_brand','booked_date','time_period','user','location','problem_interval','description','status')
        
    Status_CHOICES=[
        ('appoint','appoint'),
        ('completed','completed'),
        ('onwork','onwork'),
        ('pending','pending'),
    ]
    status = serializers.ChoiceField(choices=Status_CHOICES, default='appoint')
    
class ShowProblemserializer(serializers.ModelSerializer):
    class Meta:
        model=Showproblem
        fields=('id','user','booked_problem')
    
    