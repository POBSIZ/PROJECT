from .modules import *

def Post_list(request):
    """
    글 목록 출력
    """
     # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    # subject__contains=kw 대신 subject__icontains=kw을 사용하면 대소문자를 가리지 않고 찾아 준다.
    post_list = Post.objects.order_by('-create_date')
    if kw:
        post_list =post_list.filter(
            Q(title__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(Comment__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # page = request.Get.get('page', '1')
    # Post_list = Post.objects.order_by('-create_date')
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)

    context = {'post_list': page_obj, 'page':page, 'kw':kw}
    return render(request, '', context)


def Post_detail(request, post_id):
    """
    질문 내용 출력
    """
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, '', context)
    

@login_required(login_url='account:login')
def Post_create(request):
    """ 
    board 글 등록
    """
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            # post.category = ""  # 카테고리 받아와서 넣기
            post.save()
            return redirect('main:index')
    else:
        form = PostForm()

    context = {'form' : form}
    return render(request, 'createpost.html', context)


@login_required(login_url='account:login')
def Post_modify(request, post_id):
    """
    게시판 글 수정
    """
    post = get_object_or_404(Post, pk=post_id)
    
    if request.user != Post.author:
        messages.error(request, "수정 권한이 없습니다")
        return redirect('board:post_detail', post_id=post.id)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.modify_date = timezone.now()
            post.save()
            return redirect('board:post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, '', context)


@login_required(login_url='account:login')
def Post_delete(request, post_id):
    """ 글 삭제 """
    post = get_object_or_404(Post, pk=post_id)
    
    if request.user != post.author:
        messages.error(request, "삭제 권한이 없습니다")
        return redirect('', post_id=post.id)
    post.delete()
    return redirect('board:post_delete')

