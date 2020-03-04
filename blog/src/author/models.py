from django.contrib.auth import get_user_model

from django.db import models

from lib.models import BaseModel

USER = get_user_model()


class Author(BaseModel):
    avatar = models.ImageField(verbose_name="avatar", upload_to="static/avatars")
    user = models.OneToOneField(USER, on_delete=models.CASCADE, related_name="author")

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return 'User : {}'.format(self.user.username)