from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('token/', obtain_auth_token),
    path('my-account/', MyAccountRetrieveAPIView.as_view()),
    path('update-account/', MyAccountUpdateAPIView.as_view()),
    path('delete-account/', MyAccountDestroyAPIView.as_view()),
    path('change-password/', ChangePasswordAPIView.as_view()),
]