from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Books,customer

class PostForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'