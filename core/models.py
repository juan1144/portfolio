# mypy: ignore-errors
from datetime import datetime

from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    greeting = models.CharField(max_length=100)
    welcome_text = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="profile/", null=True, blank=True)
    start_date = models.DateField(default=datetime(2023, 5, 25))

    def __str__(self):
        return self.name


class Biography(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="biographies"
    )
    text = models.TextField()

    def __str__(self):
        return self.text[:50] + "..."


class Social(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="socials"
    )
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("Frontend", "Frontend"),
        ("Backend", "Backend"),
        ("Framework", "Framework"),
        ("Database", "Database"),
        ("Automation", "Automation"),
    ]
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="skills"
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category} - {self.name}"


class Work(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="works")
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="companies/", null=True, blank=True)

    def __str__(self):
        return f"{self.position} @ {self.company}"
