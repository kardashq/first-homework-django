from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, help_text='Enter period of life')

    def __str__(self):
        return f"{self.title}"


class Event(models.Model):
    title = models.CharField(max_length=200, help_text='Event title')
    description = models.TextField(help_text='Event description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='event', help_text='Select a category')

    def __str__(self):
        return f"{self.title} "
