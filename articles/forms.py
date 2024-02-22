from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Articles, Comments


class CreateArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["body"].required = False

    class Meta:
        model = Articles
        fields = ("title", "summery", "slug", "body", "photo", "published", "status")
        widgets = {
            "body": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }


class UpdateArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["body"].required = False

    class Meta:
        model = Articles
        fields = ("title", "summery", "body", "photo")
        widgets = {
            "body": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ("comment", )


