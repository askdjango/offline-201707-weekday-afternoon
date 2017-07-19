from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        # '/weblog/{}/'.format(self.id)
        return reverse('blog:post_detail', args=[self.id])
        # return reverse('blog:post_detail', kwargs={'pk': self.id})

