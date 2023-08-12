from django import forms
from .models import GasServiceRequest


class GasServiceRequestForm(forms.ModelForm):
    class Meta:
        model = GasServiceRequest       
        exclude = ['is_completed', 'timestamp', 'completion_timestamp']