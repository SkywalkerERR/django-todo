from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    discriptions = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    importend = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title