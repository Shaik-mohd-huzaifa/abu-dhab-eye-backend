from django.urls import path
from AbuDhabiEye import views

urlpatterns = [
    path('getUserDetails', views.getUserDetails, name="Gets User Details"),
    path('updateUserDetails', views.UpdateProfile, name="Updates User Details"),
    path('culturalEvents', views.getEvent, name="Get Events"),
    path('groups', views.getGroup, name="Gets Groups"),
    path('ask', views.Ask, name="Reponds to user query")
]