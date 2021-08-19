from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    tag_title = models.CharField(max_length=150)
    class Meta:
        db_table = 'Tag'

class Savetext(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Savetext'

