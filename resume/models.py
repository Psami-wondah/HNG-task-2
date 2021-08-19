from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    subject = models.CharField(max_length=200)
    body = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
