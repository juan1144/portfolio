# mypy: ignore-errors
from datetime import datetime

from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    role_es = models.CharField(max_length=100)
    role_en = models.CharField(max_length=100, blank=True, null=True)
    greeting_es = models.CharField(max_length=100)
    greeting_en = models.CharField(max_length=100, blank=True, null=True)
    welcome_text_es = models.CharField(max_length=200)
    welcome_text_en = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile/", null=True, blank=True)
    start_date = models.DateField(default=datetime(2023, 5, 25))

    def __str__(self):
        return self.name


class Biography(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="biographies"
    )
    text_es = models.TextField()
    text_en = models.TextField(blank=True, null=True)

    def __str__(self):
        return (self.text_es or self.text_en)[:50] + "..."


class Social(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="socials"
    )
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    icon = models.TextField()
    show_in_navbar = models.BooleanField(default=False)

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
    position_es = models.CharField(max_length=100)
    position_en = models.CharField(max_length=100, null=True, blank=True)
    start_es = models.CharField(max_length=50)
    start_en = models.CharField(max_length=50, null=True, blank=True)
    end_es = models.CharField(max_length=50)
    end_en = models.CharField(max_length=50, null=True, blank=True)
    logo = models.ImageField(upload_to="companies/", null=True, blank=True)

    def __str__(self):
        return f"{self.position} @ {self.company}"
