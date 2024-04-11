from rest_framework import serializers
from .models import User,Login,AddCategory,Problem,createBooking,Showproblem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =['id','username','phone_number','gender','district','profile_image']
        
# class UserLoginSerializer(serializers.Serializer):
#     username=serializers.CharField(max_length=255)
#     password=serializers.CharField(max_length=255)
 

class AddCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=AddCategory
        fields=['id','user','name','image']


class AddProblemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Problem
        fields=('id','name','est_time','short_description','image','category')
        
class CreateBookingSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=createBooking
        fields=('id','phone_number','booked_problem','selected_brand','booked_date','item_count','time_period','location','problem_interval','description','status','user','image')
        
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
    
    