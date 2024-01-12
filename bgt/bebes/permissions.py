from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
  
  def has_object_permission(self, request, view, obj):
    # Los permisos de solo lectura están habilitados para cualquier petición
    if request.method in permissions.SAFE_METHODS:
      return True
    
    # Los permisos de escritura están solo permitidos para quien da de alta un bebé
    return obj.usuario == request.user