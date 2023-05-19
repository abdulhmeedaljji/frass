from .models import CustomUser
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse



User = get_user_model()

class PhoneBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
        


class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            if not request.user.is_authenticated or not request.user.is_staff:
                return redirect('Home')  # Replace with your desired redirect URL
        response = self.get_response(request)
        return response        