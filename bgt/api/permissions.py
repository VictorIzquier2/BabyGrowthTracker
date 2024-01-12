from rest_framework import permissions

class isAuthorOrReadOnly(permissions.BasePermission):
  """_summary_
  Permiso para que un usuario solo tenga acceso al contenido que él creó y no al contenido de los demás.

  Args:
      permissions (_type_): _description_
  """
  
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.usuario == request.user