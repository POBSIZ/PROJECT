from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
        form = NoticeCreationForm(request.POST)
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


class NoticeDetailView(DetailView):
    model = Notice
    context_object_name = 'target_notice'
    template_name = 'noticeapp/detail.html'


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

