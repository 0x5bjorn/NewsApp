from django.forms import ModelForm

from .models import News

# ModelForm that maps News model (for news adding)
class NewsForm(ModelForm):
    # Specifing the model and its fields
    class Meta:
        model = News
        fields = ["title", "body", "images"]