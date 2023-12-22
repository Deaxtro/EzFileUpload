from django.db import models
from .typeChecker import *

# Create your models here.
class Ez(models.Model):

    title = models.CharField(max_length=100)
    ezFile = ContentTypeRestrictedFileField(upload_to='ez/files/', content_types=[
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation'
        ])

    def __str__(self):
        return self.title