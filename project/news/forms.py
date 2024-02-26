from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        title = cleaned_data.get("name")

        if title == text:
            raise ValidationError(
                "Заголовок не должен быть идентичен названию."
            )

        return cleaned_data