from django import forms 
from .models import PaperList


class UploadForm(forms.ModelForm):
  class Meta:
    model = PaperList
    fields = ('title','names','abstract','keywords','accepted','file')
    widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control','rows':'2','required':'','placeholder': 'Full paper title with capitalised first letters of all words.'}),
            'names': forms.Textarea(attrs={'class': 'form-control','rows':'2','required':'','placeholder': 'Seperated full names with commas.'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control','rows':'3','required':'','placeholder': 'Enter the Abstract.'}),
            'keywords': forms.Textarea(attrs={'class': 'form-control','rows':'2','required':'','placeholder': 'Keywords seperated by commas.'}),
    }
      


