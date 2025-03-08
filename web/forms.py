from django import forms
from .models import FitLog

class FitLogForm(forms.ModelForm):
    class Meta:
        model = FitLog
        fields = ['weight', 'height']

    height = forms.FloatField(required=False)
    weight = forms.FloatField(required=True)