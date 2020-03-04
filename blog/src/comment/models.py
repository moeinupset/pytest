from django.db import models


class Comment(models.Model):
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, auto_created=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Commentes"
