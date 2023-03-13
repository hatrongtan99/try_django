from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "content"
        ]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        print("clean_title_def", title)
        return title
