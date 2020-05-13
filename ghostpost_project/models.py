from django.db import models


class PostItem(models.Model):
    boast_roast_boolean = models.BooleanField()
    text = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Boast' if self.boast_roast_boolean else 'Roast'
