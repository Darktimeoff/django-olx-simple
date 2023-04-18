from rest_framework.permissions import BasePermission
from django.http import HttpRequest, Http404
from .container import selection_dao
from .models import Selection

class SelectionUpdatePermission(BasePermission):
    message = 'Managing others selection not permitted.'

    def has_permission(self, request: HttpRequest, view):
        try:
            pk = view.kwargs["pk"]
            entity = selection_dao.get_by_id(pk)
        except Selection.DoesNotExist:
            raise Http404
        
        if entity.owner_id == request.user.id:
            return True
        
        return False

        

       