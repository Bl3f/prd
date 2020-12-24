from django.db import models


class Podcast(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    rss = models.URLField(primary_key=True, null=False, blank=False)

