from .modules import *

@login_required(login_url='account:login')
def Comment_create(request, post_id):
    """ board 답변등록"""
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('board:post_detail', post_id = post.id)
    else:
        form = CommentForm()
    context = {'post' : post, 'form' : form}
    return render(request, '', context)


@login_required(login_url='account:login')
def Comment_modify(request, comment_id):
    """
    게시판 댓글 수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.author:
        messages.error(request, "수정 권한이 없습니다")
        return redirect('board:post_detail', post_id=comment.post.id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            # Post.modify_date = timezone.now()
            comment.save()
            return redirect('board:post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, '', context)


@login_required(login_url='account:login')
def Comment_delete(request, comment_id):
    """ 글 삭제 """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.author:
        messages.error(request, "삭제 권한이 없습니다")
        return redirect('board:post_detail', comment_id=comment.id)
    comment.delete()
    return redirect('board:post_detail', comment.post.id)
