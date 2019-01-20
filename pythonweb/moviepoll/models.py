import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_img = models.ImageField(null=True, blank=True, upload_to="movie_images")
    choice_genre = models.CharField(null=True, max_length=200, blank=True)
    choice_imdb = models.FloatField(null=True, blank=True, default=False)
    choice_description = models.CharField(null=True, max_length=500, blank=True, default=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text