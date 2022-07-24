from django import forms
from core.models import Boat


class BoatForm(forms.ModelForm):
    
    class Meta:
        model = Boat
        fields = "__all__"
