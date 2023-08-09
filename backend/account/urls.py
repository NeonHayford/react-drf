from django.urls import path
from .views import *

urlpatterns = [
    # path('rest-password', ChangePasswordView.as_view(), name = 'rest_user_password'),
    path('logout', LogoutView.as_view(), name='logout'),
]