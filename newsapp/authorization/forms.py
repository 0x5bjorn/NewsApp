from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# ModelForm that maps User model (for registration)
class UserForm(UserCreationForm):
     # Specifing the model and its fields
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
