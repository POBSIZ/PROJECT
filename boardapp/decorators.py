from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden

from boardapp.models import Post


def post_ownership_required(func):
    def decorated(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        if not post.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated


def admin_ownership_required(func):
    User = get_user_model()

    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if user.is_superuser != 1:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated