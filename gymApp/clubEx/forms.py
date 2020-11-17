from django.forms.widgets import Select
from account.models import Account
from django import forms
from django.forms.forms import BaseForm
from .models import Category, Exercise

class AccountForm(forms.Form):
    addSub = forms.CharField(max_length=100)

# CATEGORIES = []
# for i in Category.objects.all():
#     x = i.category_name
#     a = i.id
#     CATEGORIES.append(tuple((a,x)))

#print(CATEGORIES)

    
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
        # make `studio` not required, we'll check for one of `studio` or `new_studio` in the `clean` method
        self.fields['category'].required = False

    def clean(self):
        category = self.cleaned_data.get('category')
        new_category = self.cleaned_data.get('new_category')
        if not category and not new_category:
            # neither was specified so raise an error to user
            raise forms.ValidationError('Must specify either a Category or New Category!')
        elif not category:
            # get/create `Studio` from `new_studio` and use it for `studio` field
            category, created = Category.objects.get_or_create(name=new_category)
            self.cleaned_data['category'] = category

        return super(UploadForm, self).clean()