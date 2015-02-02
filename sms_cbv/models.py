from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    class Meta:
        verbose_name_plural = "Courses"

    def __unicode__(self):
        return self.course

    course = models.CharField(max_length=100)


class Students(models.Model):
    class Meta:
        verbose_name_plural = "Students"

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    courses = models.ForeignKey(Courses)


