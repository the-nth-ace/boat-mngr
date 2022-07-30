from django import forms
from core.models import Boat


class BoatForm(forms.ModelForm):
    class Meta:
        model = Boat
        fields = "__all__"


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=255)
    new_password = forms.CharField(max_length=255)
    new_password_confirm = forms.CharField(max_length=255)

    def clean(self):
        cd = self.cleaned_data
        if cd.get("new_password") != cd.get("new_password_confirm"):
            self.add_error("new_password_confirm", "Passwords do not match")
        return cd
