from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
# reverse : 함수형에서 사용  reverse_lazy : 클래스형에서 사용
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import *
from profileapp.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from boardapp.models import Post
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model, logout

has_ownership = [account_ownership_required, login_required]


def AccountIDCheck(request):
    if (request.method == 'POST'):
        username = request.POST['username']
    else:
        username = ''
    user = get_user_model()
    idObject = user.objects.filter(username__exact=username)
    idCount = idObject.count()

    if idCount > 0:
        msg = "<span>이미 존재하는 ID입니다.</span><input type='hidden' name='idcheck-result'\
               id='IDCheckResult' value=0>"
    else:
        msg = "<span>사용할 수 있는 ID입니다.</span><input type='hidden' name='idcheck-result'\
               id='IDCheckResult' value=1>"

    return HttpResponse(msg)


def AccountCreate(request):

    if (request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        realname = request.POST['realname']
        phone = request.POST['phone']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
    else:
        return render(request, 'accountapp/create.html')

    try:
        if username and get_user_model().objects.filter(username__exact=username).count() == 0:
            user = get_user_model().objects.create_user( \
                username, password, realname, email, phone, date_of_birth)

            user.save()

            redirection_page = "accountapp:createcomplete"
        else:
            redirection_page = "mainapp:error"
    except:
        redirection_page = "mainapp:error"

    return redirect(redirection_page)


def AccountCreateComplete(request):
    return render(request, 'accountapp/createcomplete.html')


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = get_user_model()
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 5

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = get_user_model()
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('main')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = get_user_model()
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'


from .forms import CheckPasswordForm


@login_required(login_url='accounts:login')
def profile_delete_view(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/accounts/login/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'accountapp/user_delete.html', {'password_form': password_form})
