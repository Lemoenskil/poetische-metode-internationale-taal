from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog



def get_blogs(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'blogs.html' template
    """
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogs.html", {'blogs': blogs})


def blog_detail(request, pk):
#     """
#     Create a view that returns a single
#     Post object based on the post ID (pk) and
#     render it to the 'postdetail.html' template.
#     Or return a 404 error if the post is
#     not found
#     """
    blog = get_object_or_404(Blog, pk=pk)
#     post.views += 1
#     post.save()
    return render(request, "blog-detail.html", {'blog': blog})


# def create_or_edit_post(request, pk=None):
#     """
#     Create a view that allows us to create
#     or edit a post depending if the Post ID
#     is null or not
#     """
#     post = get_object_or_404(Post, pk=pk) if pk else None
#     if request.method == "POST":
#         form = BlogPostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             return redirect(post_detail, post.pk)
#     else:
#         form = BlogPostForm(instance=post)
#     return render(request, 'blogpostform.html', {'form': form})
