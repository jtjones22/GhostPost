from django.db import models
import datetime


class PostItem(models.Model):
    CHOICES = (
        ('roast', 'ROAST'),
        ('boast', 'BOAST'),
    )
    category_choice = models.CharField(
        choices=CHOICES,
        max_length=50
        )
    text = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(
        default=datetime.datetime.now,
        blank=True
        )

    def __str__(self):
        return self.category_choice


class Category(models.Model):
    categories = models.ForeignKey(PostItem, on_delete=models.CASCADE)