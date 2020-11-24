from django.forms import fields
from django.forms.models import model_to_dict
from django.forms.widgets import Select
from account.models import Account
from django import forms
from django.forms.forms import BaseForm
from .models import Category, Exercise

class AccountForm(forms.Form):
    addSub = forms.CharField(max_length=100)


    
class UploadForm(forms.ModelForm): 
    exercise_name = forms.CharField(max_length=50, label="Exercise name")
    category = forms.ModelChoiceField(Category.objects)
    new_category = forms.CharField(max_length=30, required=False, label = "New Category Name")
    videofile = forms.FileField()
    class Meta:
        model = Exercise
        exclude = ['views', 'likes']
    

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)

        self.fields['category'].required = False

    def clean(self):
        category = self.cleaned_data.get('category')
        new_category = self.cleaned_data.get('new_category')
        if not category and not new_category:
 
            raise forms.ValidationError('Must specify either a Category or New Category!')
        elif not category:

            category, created = Category.objects.get_or_create(name=new_category)
            self.cleaned_data['category'] = category

        return super(UploadForm, self).clean()

CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
]
class RatingForm(forms.Form):
    stars = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
   
