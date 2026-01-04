from django.urls import path
from .views import *


urlpatterns = [
    path('test-auth/', TestAurhAPIView.as_view()),
    path('my-plans/', PlanListAPIView.as_view()),
    path('my-plans/<int:pk>/', PlanRetrieveUpdateDestroyAPIView.as_view()),
]