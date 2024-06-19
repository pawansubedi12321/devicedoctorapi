from django.urls import path, include
from .views import RegisterView,LoginView,AddCategoryView,ProblemView,LogoutView,CreateBooking,showproblemview,Editproblem

# from rest_framework_jwt.blacklist.views import BlacklistView
urlpatterns = [
    path("register/",RegisterView.as_view(),name="register"), 
    path("login/",LoginView.as_view(),name="login"),
    path("addcategory/",AddCategoryView.as_view(),name="AddCategory"),    
    path("getcategory/<int:pk>/",AddCategoryView.as_view(),name="getCategory"), 
    # path("addproblem/",ProblemView.as_view(),name="addproblem"), 
    path("getproblem/<int:pk>/",ProblemView.as_view(),name="addproblem"), 
    path("logout/",LogoutView.as_view(),name="logout"),
    path("createbooking/",CreateBooking.as_view(),name="createbooking"),
    path("getbooking/<int:pk>/",CreateBooking.as_view(),name="getbooking"),
    path("showproblem/",showproblemview.as_view(),name="showproblem"),
    path('editproblem/<int:pk>/',Editproblem.as_view(),name='editproblem'),

    # path("auth/logout/", BlacklistView.as_view({"post": "LogoutView"}))

]
