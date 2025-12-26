from django import forms
from .models import Resume


class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data['file']

        allowed_types = [
            'application/pdf',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        ]

        if file.content_type not in allowed_types:
            raise forms.ValidationError(
                'Разрешены только PDF или DOCX файлы'
            )

        if file.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                'Размер файла не должен превышать 5 МБ'
            )

        return file
