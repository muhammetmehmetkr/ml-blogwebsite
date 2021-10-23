from django.db import models


class PredResults(models.Model):

    age = models.FloatField()
    Medu = models.FloatField()
    Fedu = models.FloatField()
    failures = models.FloatField()
    freetime = models.FloatField()
    goout = models.FloatField()
    Walc = models.FloatField()
    absences = models.FloatField()
    G1 = models.FloatField()
    G2 = models.FloatField()
    classification = models.CharField(max_length=15)

    def __str__(self):
        return self.classification