from django.db import models

class Job(models.Model):
    url = models.URLField()
    posted_by = models.CharField(max_length=255)
    company = models.CharField(max_length=255,default="unknown")
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    year_from = models.IntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')])

    def __str__(self):
        return f"{self.posted_by} - {self.url}"

