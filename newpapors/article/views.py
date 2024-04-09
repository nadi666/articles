from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def article_list(request):
    articles = Article.objects.all().order_by('title')
    return render(request, 'article/index.html', {'articles': articles})

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article:article_list')
    else:
        form = ArticleForm()
    return render(request, 'article/form.html', {'form': form})

def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('article:article_list')
    return render(request, 'article/form.html', context)

def article_delete(pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article:article_list')

def article_filter(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        article_title = request.POST.get('article_title')
        if article_title:
            articles = articles.filter(title__icontains=article_title)
    for article in articles:
        article.comments = article.comment_set.all()

    return render(request, 'article/filter.html', {'articles': articles})

def comment_list(request):
    comments = Comment.objects.all().order_by('autor_name')
    return render(request, 'article/index.html', {'comments': comments})

def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article:article_list')
    else:
        form = CommentForm()
    return render(request, 'article/form_comment.html', {'form': form})