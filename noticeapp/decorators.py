from django.http import HttpResponseForbidden

from noticeapp.models import Notice

def notice_ownership_required(func):
    def decorated(request, *args, **kwargs):
        notice = Notice.objects.get(pk=kwargs['pk'])
        if not notice.writer == request.user:
            return HttpResponseForbidden()
        if not request.user.is_superuser == 1:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
