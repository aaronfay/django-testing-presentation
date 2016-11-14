from django.db import models


class Participant(models.Model):
    email = models.EmailField()
    # TODO: track commits