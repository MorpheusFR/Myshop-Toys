from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from .forms import CommentForm
from django.template.context_processors import csrf


# Create your views here.


def template_one(request):
    view = "Article title"
    return render_to_response('articles/article/article_view.html', {'name': view})


def articles(request):
    return render_to_response('articles/article/articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))  # Проверка данных
    args['articles'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    return render_to_response('articles/article/article.html', args)


# def article(request, article_id=1):
#     return render_to_response('articles/article/article.html', {
#         'article': Article.objects.get(id=article_id),
#         'comments': Comments.objects.filter(comments_article_id=article_id)})

def add_like(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.article_likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/articles/all')


def add_comment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST) #CommentForm
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article_id = Article.objects.get(id=article_id)
            form.save()

    return redirect('/articles/get/%s' % article_id)
