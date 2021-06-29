# from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model


def account_ownership_required(func):
    User = get_user_model()

    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user.username == request.user.username:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated