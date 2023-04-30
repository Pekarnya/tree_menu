"""
 Implementation of the menu item model
contains very few methods in purpose to pass
the excercise UpTrade
Returns:
    models.Model obj: string value in default format
"""

from django.db import models

# Create your models here.


class MenuItem(models.Model):
    """
    MenuItem basic model with data
    for rendering menu items

    Includes the following attributes:
        name: The name of the menu item
        url: The URL to the menu item
        parent: The parent menu item

    Args:
        models (Model class): MenuItem is a child of basic
        Model class from Django framework
    """
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey("self", null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name="children")
    order = models.PositiveIntegerField(default=0)
    menu = models.CharField(max_length=255, default="main")
    is_active = models.BooleanField(default=True)

    class Meta:
        """
         Container class specifying options for
         the model.

        _extended_summary_
        """
        ordering = ["order"]

    def __str__(self) -> str:
        return self.name
