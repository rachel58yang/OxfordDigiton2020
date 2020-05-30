from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    response = models.IntegerField(default=None)

    def publish(self):
        self.create_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text