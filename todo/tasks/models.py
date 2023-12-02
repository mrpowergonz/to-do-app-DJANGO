from django.db import models

# Create your models here.
#añado una carpeta nueva en la pagina admin
class Task(models.Model):
    title = models.CharField( max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    