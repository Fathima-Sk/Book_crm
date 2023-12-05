from django import forms
from Work.models import book


class Empform(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.IntegerField()
    contact=forms.IntegerField()

# class bookform(forms.Form):
#     title=forms.CharField()
#     auther=forms.CharField()
#     publication_year=forms.IntegerField()
#     genre=forms.CharField()

#or

class bookform(forms.ModelForm):
    class Meta:
        model=book
        fields=['title','auther','publication_year','genre']

        #or
        #fields='__all__'

