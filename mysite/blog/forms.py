from django import forms
from .models import Post,Profile
from django.contrib.auth.models import User
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'status',

        )
class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'status',

        )

class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="",widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Enter Password Here...'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Enter Password Here...'}))
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password Mismatch')
        return confirm_password

class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
             
        )

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
