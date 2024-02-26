from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=100, default="My Title")
    summary = models.TextField(default="This is my breif summary")

    def __str__(self):
        return self.title
    
class Certification(models.Model):
    title = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.school