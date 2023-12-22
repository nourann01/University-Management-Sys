from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input-container-input'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input-container-input'}))    
    Major = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input-container-input'}))
    StudyYear = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input-container-input'}))

    class Meta:
        model = User
        fields = ("username", "first_name","last_name","Major","StudyYear", "password1", "password2")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(RegisterUserForm,self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "input-container-input"
        self.fields["username"].widget.attrs["placeholder"] = "rickGrimes@AHN.edu.eg"
        self.fields["username"].label = "Email"
        self.fields["username"].help_text = ""
        self.fields["username"].widget.forms="EmailInput"
        self.fields["username"].widget.attrs["autocomplete"] = "off"
        self.fields["username"].widget.attrs["required"] = True
        self.fields["username"].widget.attrs["autofocus"] = True

        self.fields["password1"].widget.attrs["class"] = "input-container-input"
        self.fields["password1"].widget.attrs["placeholder"] = "password"
        self.fields["password1"].label = "Password"
        self.fields["password1"].help_text = ""
        self.fields["password1"].widget.attrs["autocomplete"] = "off"
        self.fields["password1"].widget.attrs["required"] = True
        self.fields["password1"].widget.attrs["autofocus"] = True

        self.fields["password2"].widget.attrs["class"] = "input-container-input"
        self.fields["password2"].widget.attrs["placeholder"] = "password"
        self.fields["password2"].label = "Confirm Password"
        self.fields["password2"].help_text = ""
        self.fields["password2"].widget.attrs["autocomplete"] = "off"
        self.fields["password2"].widget.attrs["required"] = True
        self.fields["password2"].widget.attrs["autofocus"] = True

