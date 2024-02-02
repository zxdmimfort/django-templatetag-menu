from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)
    url = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="children"
    )
    menu = models.ForeignKey(
        Menu, null=True, blank=True, on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self):
        return self.name
