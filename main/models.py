from django.db import models

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=20)
    writer = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.writer