import uuid
from django.db import models
from blog_api.models.author import Author

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blog = models.TextField(null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_blog"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.blog