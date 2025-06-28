from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating', 'sentiment']
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'}),
            'sentiment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional sentiment'}),
        }
