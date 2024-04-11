from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer,AddCategorySerializer,AddProblemSerializer,CreateBookingSerializer,ShowProblemserializer
from rest_framework.response import Response
from .models  import User,AddCategory,Problem,createBooking,Showproblem
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
from rest_framework import status as http_status
class RegisterView(APIView):
    def post(self, request):
        # hello world
        
        username=request.data.get("username")
        phone_number=request.data.get("phone_number")
        gender=request.data.get("gender")
        district=request.data.get("district")
        profile_image=request.data.get("profile_image")
        data={'username':username,'phone_number':phone_number,'gender':gender,'district':district,'profile_image':profile_image}
       
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    



class LoginView(APIView):
    
    def post(self, request):
        # Check if user is not already logged in
        if 'student_user' not in request.session:  
            username = request.data.get("username")
            phone_number = request.data.get("phone_number")
            # Check if a user with the provided username and phone number exists
            stu_exists = User.objects.filter(username=username, phone_number=phone_number).exists()
            if stu_exists:
                # Set session variable to mark user as logged in
                request.session['student_user'] = username
                # Get the user details
                student = User.objects.get(username=username)
                data = {
                    "id": student.id,
                    "username": student.username,
                    "phone_number": student.phone_number,
                    "gender": student.gender,
                    "district": student.district,
                    "profile_image": student.profile_image.url if student.profile_image else None,
                }
                # Generate JWT tokens for the user
                tokens = self.get_tokens_for_user(student)
                response_message = f"Welcome, {username}"
                print("this is student", data)
                return Response({"message": response_message, "data": data, "tokens": tokens}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "User is already logged in"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
class LogoutView(APIView):
    def post(self, request):
        # Delete session variables
        if 'student_user' in request.session:
            del request.session['student_user']

        # Alternatively, you can use pop() method
        # request.session.pop('student_user', None)

        # No need to call logout() function as it's not defined in Django's default session handling
        
        response_message = "You have been successfully logged out."
        return Response({"message": response_message}, status=status.HTTP_200_OK)
    
class AddCategoryView(APIView):
    def post(self,request):
        register_id=request.data.get("user")
        # register = get_object_or_404(AddCategory, pk=pk)
        # print("this is register id",register)
        
        name=request.data.get("name")
        image=request.data.get("image")
        data={'user':register_id,'name':name,'image':image}
        serializer =AddCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk=None):
        # register=Register.objects.get(pk=pk) 
        if pk is not None:
            register = get_object_or_404(User, pk=pk)
            categories=AddCategory.objects.filter(user=register.id)
            serializer=AddCategorySerializer(categories,many=True)
            if categories:
                return Response(serializer.data)
            else:
                return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Invalid  get request"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        #
        category = get_object_or_404(AddCategory, pk=pk)
        print(category)
        # user=request.data.get("user")
        
        name=request.data.get("name")
        image=request.data.get("image")
        category.name=name
        category.image=image
        # category.user=user
        category.save()
        serializer =AddCategorySerializer(category)
  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        # Retrieve the category object by pk or raise a 404 error if it doesn't exist
        category = get_object_or_404(AddCategory, pk=pk)
        
        # Delete the category object
        category.delete()
        
        # Return a success response
        return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 
          
            
class ProblemView(APIView):
    def post(self,request):
        category=request.data.get("category")
        name=request.data.get("name")
        # price=request.data.get("price")
        est_time=request.data.get("est_time")
        short_description=request.data.get("short_description")
        image=request.data.get("image")
        data={'name':name,'est_time':est_time,'short_description':short_description,'image':image,'category':category}
        serializer=AddProblemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk):
          categories=Problem.objects.filter(category=pk)
        #   problems=Problem.objects.filter(id=categories)
          serializer=AddProblemSerializer(categories,many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)
      
    def put(self, request, pk):
        #
        problem = get_object_or_404(Problem, pk=pk)
        
        name=request.data.get("name")
        price=request.data.get("price")
        est_time=request.data.get("est_time")
        short_description=request.data.get("short_description")
        image=request.data.get("image")
        problem.name=name
        problem.price=price
        problem.est_time=est_time
        problem.short_description=short_description
        problem.image=image
        problem.save()
        # category.image=image
        # # category.user=user
        # category.save()
        serializer =AddProblemSerializer(problem)
  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        # Retrieve the category object by pk or raise a 404 error if it doesn't exist
        category = get_object_or_404(Problem, pk=pk)
        
        # Delete the category object
        category.delete()
        
        # Return a success response
        return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    # this i s delete
          

       
class CreateBooking(APIView):
    def post(self, request):
        # Parse request data
        #hello this is create booking 
        selected_brand = request.data.get("selected_brand")
        booked_problem = request.data.get("booked_problem")
        booked_date = request.data.get("booked_date")
        item_count = request.data.get("item_count")
        time_period = request.data.get("time_period")
        location = request.data.get("location")
        user = request.data.get("user")
        problem_interval = request.data.get("problem_interval")
        description = request.data.get("description")
        image=request.data.get('image')
        data = {
            'selected_brand': selected_brand,
            'booked_date': booked_date,
            'item_count': item_count,
            'time_period': time_period,
            'location': location,
            'problem_interval': problem_interval,
            'description': description,
            'booked_problem':booked_problem,
            'user':user,
            'image':image,
          
        }
        serializer = CreateBookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=http_status.HTTP_201_CREATED)  # Use http_status
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)  # Use http_status
    
    
    def get(self, request, pk=None):
        if pk is not None:
            
            try:
                booking =createBooking.objects.filter(user=pk)
                print("this is booking",booking)
                serializer = CreateBookingSerializer(booking,many=True)
                return Response(serializer.data, status=http_status.HTTP_200_OK)
            except:
                return Response({'error': 'Booking not found'}, status=http_status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Please provide a valid pk'}, status=http_status.HTTP_400_BAD_REQUEST)
        
class showproblemview(APIView):
    def get(self,request):
        # if pk is not None:
            # try:
                problemlist=Problem.objects.all()
                print("this is problemlist",problemlist)
                serializer=AddProblemSerializer(problemlist,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
