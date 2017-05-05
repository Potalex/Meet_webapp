from django import forms

from .models import Activity

class ActForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ('title', 'content',)