from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import User, TeacherUser


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User

        fields=['username','email','password1','password2']
