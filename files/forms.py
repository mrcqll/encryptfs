from django import forms
from .models import UploadedFile


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ["file"]

    def clean_file(self):
        uploaded_file = self.cleaned_data["file"]

        if uploaded_file.size > 10 * 1024 * 1024:
            raise forms.ValidationError(
                "Files must be 10 MB or smaller."
            )

        return uploaded_file