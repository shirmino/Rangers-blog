from django.db import models 
from articles.models import Article


# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return '{}'.format(self.body[:50] + '...', self.name)