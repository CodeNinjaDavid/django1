from django import forms
from newform.model import Registration

class Names(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
