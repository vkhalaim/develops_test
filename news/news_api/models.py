from django.db import models


class Post(models.Model):
    """Post model"""

    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def vote(self):
        self.upvotes += 1
        self.save(force_update=True)


class Comment(models.Model):
    """Comment model"""

    author = models.CharField(verbose_name="author", max_length=50)
    content = models.TextField(verbose_name="content")
    created = models.DateTimeField(
        verbose_name="creation date", auto_now_add=True
        )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self):
        return f"{self.author}'s comment to {self.post}"
