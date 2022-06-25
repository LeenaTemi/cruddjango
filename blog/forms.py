from django import forms
from .models import TodoApp

#creating a form
class BlodAppForm(forms.ModelForm):

    #create meta class
    class Meta:
        model=BlogApp

        fields = {
            "little",
            "description"
        }