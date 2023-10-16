from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseForbidden

def admin_required(view_func):
    @staff_member_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Brak dostępu")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
