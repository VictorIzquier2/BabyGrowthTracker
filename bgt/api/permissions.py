from rest_framework import permissions

class isAuthorOrReadOnly(permissions.BasePermission):
  """
  Permiso personalizado para permitir solo al autor de un objeto realizar modificaciones.

  Este permiso es parte de la API de 'babygrowthtracker', asegurando que solo el usuario
  (autor) que creó un objeto específico (como un registro de bebé) tiene permiso para
  editar o eliminar ese objeto. Otros usuarios pueden solo leer el objeto, pero no
  modificarlo.

  Métodos:
    has_object_permission: Este método determina si el usuario que realiza la solicitud
    tiene permiso para realizar la acción solicitada en el objeto. Si el método HTTP de 
    la solicitud está en `permissions.SAFE_METHODS` (GET, HEAD, OPTIONS), se concede 
    acceso de solo lectura a todos.   Para cualquier otro método HTTP 
    (como POST, PUT, DELETE), el acceso se restringe solo al usuario que creó el objeto.

  Atributos:
    SAFE_METHODS (tuple): Métodos considerados "seguros", donde solo se lee la información,
    y no se modifica. Incluye GET, HEAD y OPTIONS.

  Esta clase es utilizada para controlar el acceso a los objetos en las vistas de la API,
  donde se requiere que solo el autor del objeto pueda hacer cambios, mientras que otros
  usuarios pueden acceder a la información de manera de solo lectura.
  """
  
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.usuario == request.user