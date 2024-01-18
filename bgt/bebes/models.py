from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bebe(models.Model):
  """
  Clase Bebe para almacenar información sobre bebés.

  Esta clase es utilizada para registrar y manejar datos de bebés, incluyendo su nombre,
  apellidos, fecha de nacimiento, sexo, una fecha adicional (posiblemente para registrar 
  eventos o controles específicos), un histórico en formato JSON (para almacenar información 
  variable y adicional sobre el bebé), y una imagen.

  Atributos:
    usuario (User): Usuario de Django asociado con el bebé. La relación es una ForeignKey
    que permite la asociación con el modelo User de Django. Si el usuario es eliminado, 
    este campo se establece en NULL.
    
    nombre (str): Nombre del bebé.
    
    apellidos (str): Apellidos del bebé.
    
    fecha_nacimiento (Date): Fecha de nacimiento del bebé.
    
    SEXO_OPCIONES (list of tuple): Opciones de sexo para el bebé, que incluyen 'varon' y 'mujer'.
    sexo (str): Sexo del bebé, elegido de las opciones disponibles
    .
    fecha (Date): Una fecha adicional, cuyo propósito específico puede variar.
    
    historico (JSON): Un campo JSON para almacenar datos históricos o adicionales del bebé.
    
    imagen (Image): Imagen del bebé, almacenada en la ubicación especificada.

  Métodos:
    __str__: Retorna una cadena de caracteres que representa al bebé, incluyendo su nombre,
    apellidos y un ícono que varía según el sexo del bebé.
  """
  
  usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  nombre = models.CharField(max_length=50)
  apellidos = models.CharField(max_length=100)
  fecha_nacimiento = models.DateField()
  SEXO_OPCIONES = [
    ('varon', 'Varon'),
    ('mujer', 'Mujer'),
    ]
  sexo = models.CharField(max_length=5, choices=SEXO_OPCIONES)
  fecha = models.DateField()
  historico = models.JSONField(default=list)
  imagen = models.ImageField(upload_to='imagenes')
  
  def __str__(self):
    if self.sexo == 'varon':
      return f'👦: {self.nombre} {self.apellidos}'
    else:
      return f'👧: {self.nombre} {self.apellidos}'