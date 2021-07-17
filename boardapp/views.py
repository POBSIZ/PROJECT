from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.db.models import Q

from boardapp.decorators import post_ownership_required
from boardapp.forms import PostCreationForm
from boardapp.models import Post, Category
from commentapp.forms import CommentCreationForm


@login_required(login_url='accountapp:login')
def Post_create(request):
    """
    글 등록
    """

    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.title = request.POST['title']
            category = Category.objects.get(name=request.POST['category'])
            post.category = category
            post.save()
            return redirect('boardapp:list')
    else:
        form = PostCreationForm()
        categories = Category.objects.all()

    context = {'form': form , 'category': categories}
    return render(request, 'boardapp/create.html', context)


class PostDetailView(DetailView, FormMixin):
    model = Post
    form_class = CommentCreationForm
    context_object_name = 'target_post'
    template_name = 'boardapp/detail.html'


@method_decorator(post_ownership_required, 'get')
@method_decorator(post_ownership_required, 'post')
class PostUpdateView(UpdateView):
    model = Post
    context_object_name = 'target_post'
    form_class = PostCreationForm
    template_name = 'boardapp/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['category'] = categories

        return context

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(post_ownership_required, 'get')
@method_decorator(post_ownership_required, 'post')
class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'target_post'
    success_url = reverse_lazy('boardapp:list')
    template_name = 'boardapp/delete.html'


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'boardapp/list.html'

    paginate_by = 5

    ordering = ['-pk']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        
        page = request.GET.get('page', '1')  # 페이지
        kw = request.GET.get('kw', '')  # 검색어
        
        post_list = Post.objects.order_by('-pk')
        if kw:
            post_list = post_list.filter(
                Q(title__icontains=kw) |  # 제목검색
                Q(content__icontains=kw) |  # 내용검색
                Q(writer__username__icontains=kw) |  # 질문 글쓴이검색
                Q(comment__writer__username__icontains=kw) |  # 답변 글쓴이검색
                Q(category__name__icontains=kw)
            ).distinct()
        
        context['post_list'] = post_list
        context['kw'] = kw
        context['page'] = page
        
        return context



