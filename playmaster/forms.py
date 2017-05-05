from django import forms
from django.utils import timezone
from .models import Activity

class ActForm(forms.ModelForm):
    
    class Meta:
        model = Activity
        fields = ('title', 'content','activateDate')