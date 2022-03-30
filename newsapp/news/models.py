from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Data model of News 
class News(models.Model):
    # Fields of the model:
    # - title of the news article
    # - date of publication 
    # - body of the news article
    # - images(optionally) of news article
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="newslist", null=True)
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField("date published", default=datetime.now)
    body = models.TextField()
    images = models.ImageField(upload_to="news_images", blank=True)

    # Specifing the storing order
    class Meta:
        ordering=["-publication_date"]

    # Represent News model as a string(for printing purposes)
    def __str__ (self):
        return "News(title: " + str(self.title) + ", date: " + str(self.publication_date) + ")"