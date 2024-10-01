"""
Reaction model

Fields:
- user: Reaction owner
- article: Article reacted to
- emoji: Reaction emoji
- updated_at: Last update
- created_at: Date reacted
"""

from django.db import models
from django.contrib.auth import get_user_model


REACTIONS = (
    ("👍🏻", "👍🏻 Like"),
    ("❤️", "❤️ Love"),
    ("🤣", "🤣 Funny"),
    ("😲", "😲 Wow"),
    ("🤔", "🤔 Thinking"),
    ("😡", "😡 Angry"),
)


# Create your models here.
User = get_user_model()


class Reaction(models.Model):
    """Article Reactions"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    article = models.ForeignKey(
        "articles.Article",
        on_delete=models.CASCADE,
        help_text="Article",
    )
    emoji = models.CharField(
        max_length=8,
        default="👍🏻",
        help_text="Reaction",
        choices=REACTIONS,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date reacted",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                fields=["user", "article"],
                name="unique_reaction",
            )
        ]

    def __str__(self) -> str:
        return f"{self.user} --{self.emoji}-> {self.article}"
