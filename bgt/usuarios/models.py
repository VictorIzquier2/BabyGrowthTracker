from django.db import models

# Create your models here.
class Usuario(models.Model):
  usuario = models.CharField(max_length=50, unique=True)
  contrasenha = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  
  def __str__(self):
    return f'👤{self.id}: {self.usuario}, 📧: {self.email}'
  