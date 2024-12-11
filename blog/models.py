from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Título del post
    content = models.TextField()  # Contenido del post
    date_posted = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return self.title
