from django.db import models

# Create your models here.


class Hireme(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.email

    # class Meta:
    #     verbose_name_plural = 'Hireme'
    #     verbose_name = 'Hireme'
    #     ordering = ['-created_at']
