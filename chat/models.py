from django.db import models

class Chat(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['created_at']