



def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if no user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

        return decorated