from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

  """
    Permiso personalizado para permitir solo al autor de un objeto realizar operaciones de escritura.

    Esta clase de permiso extiende 'permissions.BasePermission' de Django REST framework.
    Proporciona una regla de permisos que permite operaciones de solo lectura a cualquier usuario,
    pero restringe las operaciones de escritura (como editar o eliminar) exclusivamente al autor del objeto.

    Métodos:
      has_object_permission(self, request, view, obj): 
      Determina si el usuario que realiza la petición tiene permiso para realizar la acción solicitada
      en el objeto 'obj'.

      El método 'has_object_permission' verifica si el método de la petición es uno de los considerados seguros
      (GET, HEAD, OPTIONS). Si es así, permite la acción (lectura). En caso contrario, verifica si el usuario
      que realiza la petición es el mismo que creó el objeto, permitiendo acciones de escritura solo si esta
      condición se cumple.

    Nota:
        Es importante que el modelo al que se aplica este permiso tenga un campo 'usuario' que almacene una
        referencia al usuario que lo creó, ya que la verificación de autoría se basa en este campo.
    """

  def has_object_permission(self, request, view, obj):
    # Los permisos de solo lectura están habilitados para cualquier petición
    if request.method in permissions.SAFE_METHODS:
      return True
    
    # Los permisos de escritura están solo permitidos para quien da de alta un bebé
    return obj.usuario == request.user