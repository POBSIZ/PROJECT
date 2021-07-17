from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from noticeapp.forms import NoticeCreationForm
from noticeapp.models import Notice
from noticeapp.decorators import notice_ownership_required


@login_required(login_url='accountapp:login')
def Notice_create(request):
    """
    공지사항 등록
    """
    if not request.user.is_superuser == 1:
        return render(request, 'error.html')

    if request.method == 'POST':
        form = NoticeCreationForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.writer = request.user
            notice.title = request.POST['title']
            notice.save()
            return redirect('noticeapp:list')
    else:
        form = NoticeCreationForm()

    context = {'form': form }
    return render(request, 'noticeapp/create.html', context)


def Notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    context = {'target_notice': notice}

    response = render(request, 'noticeapp/detail.html', context)

    expire_time = 600
    cookie_value = request.COOKIES.get('hitboard', '_')

    if f'_{pk}_' not in cookie_value:
        cookie_value += f'{pk}_'
        response.set_cookie('hitboard', value=cookie_value, max_age=expire_time, httponly=True)

        notice.watches += 1
        notice.save()

    return response

# class NoticeDetailView(DetailView):
#     model = Notice
#     context_object_name = 'target_notice'
#     template_name = 'noticeapp/detail.html'


@method_decorator(notice_ownership_required, 'get')
@method_decorator(notice_ownership_required, 'post')
class NoticeUpdateView(UpdateView):
    model = Notice
    context_object_name = 'target_notice'
    form_class = NoticeCreationForm
    template_name = 'noticeapp/update.html'

    def get_success_url(self):
        return reverse('noticeapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(notice_ownership_required, 'get')
@method_decorator(notice_ownership_required, 'post')
class NoticeDeleteView(DeleteView):
    model = Notice
    context_object_name = 'target_notice'
    success_url = reverse_lazy('noticeapp:list')
    template_name = 'noticeapp/delete.html'


class NoticeListView(ListView):
    model = Notice
    context_object_name = 'notice_list'
    template_name = 'noticeapp/list.html'

    paginate_by = 5

    ordering = ['-pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request

        page = request.GET.get('page', '1')  # 페이지
        kw = request.GET.get('kw', '')  # 검색어

        notice_list = Notice.objects.order_by('-pk')
        if kw:
            notice_list = notice_list.filter(
                Q(title__icontains=kw) |  # 제목검색
                Q(content__icontains=kw) |  # 내용검색
                Q(writer__username__icontains=kw) # 질문 글쓴이검색
            ).distinct()

        context['notice_list'] = notice_list
        context['kw'] = kw
        context['page'] = page

        return context
