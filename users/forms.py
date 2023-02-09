from django import forms

from users.models import MyUser, Profile


class UserCreateForm(forms.ModelForm):
    """ User Create or Registration Form """
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'city', 'user_type')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}),
            'password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }


class UserUpdateForm(forms.ModelForm):
    """ User Update Form by Admin """
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'username', 'email', 'city', 'user_type')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }


class CustomerUpdateForm(forms.ModelForm):
    """ User Profile Detail Update Form"""
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'username', 'email', 'city',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomerProfileForm(forms.ModelForm):
    """ User profile photo form """
    class Meta:
        model = Profile
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
        }
