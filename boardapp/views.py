from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.db.models import Q
from hitcount.views import HitCountDetailView

from boardapp.decorators import post_ownership_required, admin_ownership_required
from boardapp.forms import PostCreationForm, CategoryCreateForm
from boardapp.models import Post, Category
from commentapp.forms import CommentCreationForm


@login_required(login_url='accountapp:login')
def Post_create(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.title = request.POST['title']
            category = get_object_or_404(Category, name=request.POST['category'])
            post.category = category
            post.save()
            return redirect('boardapp:list')
    else:
        form = PostCreationForm()
        categories = Category.objects.all()

    context = {'form': form, 'category': categories}
    return render(request, 'boardapp/create.html', context)


def Post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentCreationForm()
    context = {'target_post': post, 'form': form}

    response = render(request, 'boardapp/detail.html', context)

    expire_time = 600
    cookie_value = request.COOKIES.get('hitboard', '_')

    if f'_{pk}_' not in cookie_value:
        cookie_value += f'{pk}_'
        response.set_cookie('hitboard', value=cookie_value, max_age=expire_time, httponly=True)

        post.watches += 1
        post.save()

    return response

#
# class PostDetailView(HitCountDetailView, FormMixin, ):
#     model = Post
#     form_class = CommentCreationForm
#     count_hit = True
#     context_object_name = 'target_post'
#     template_name = 'boardapp/detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         request = self.request
#
#         # 쿠키 만료 시간 10분
#         expire_time = 600
#         cookie_value = request.COOKIES.get('hitboard', '_')
#
#         if f'_{self.object.pk}_' not in cookie_value:
#             cookie_value += f'{self.object.pk}_'
#             response.
#
#         return context


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


# @method_decorator(admin_ownership_required, 'get')
# @method_decorator(admin_ownership_required, 'post')
# class CategoryCreateView(CreateView):
#     model = Category
#     form_class = CategoryCreateForm
#     template_name = 'boardapp/catecreate.html'
#
#     def get_success_url(self):
#         return reverse('accountapp:detail', kwargs={'pk': self.user.pk})

def Category_Create(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('accountapp:detail', pk=request.user.pk)
    else:
        form = CategoryCreateForm()

    context = {'form': form}
    return render(request, 'boardapp/catecreate.html', context)