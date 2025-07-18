"""A model to use a `through` model to define relation between articles and tags"""

from django.db import models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


# Create your models here.
class Tag(TaggedItemBase):
    """Through model for defining m2m rel between Articles and Tags"""

    content_object = ParentalKey(
        "articles.Article",
        on_delete=models.CASCADE,
        related_name="tagged_items",
    )
