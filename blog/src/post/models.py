from django.db import models

from author.models import Author

from category.models import Category

from lib.models import BaseModel


class Post(BaseModel):
    DRAFT = 0
    PUBLISHED = 1
    ARCHIVED = 2

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (ARCHIVED, 'Archived'),
    )

    title = models.CharField(max_length=255, verbose_name="title")
    body = models.TextField(max_length=255, verbose_name="body")
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=1, related_name='post')
    categories = models.ManyToManyField(Category, related_name='post')
    # post ha ra az in table mikhanad CategoryPost
    attachment = models.FileField(
        verbose_name='attach', upload_to='post/attachments', null=True)
    status = models.PositiveSmallIntegerField(verbose_name='status', choices=STATUS_CHOICES, default=0)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    # class CategoryPost(models.Model):
    #     category = models.ForeignKey(Category)
    #     post = models.ForeignKey(Post)
    #     created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title