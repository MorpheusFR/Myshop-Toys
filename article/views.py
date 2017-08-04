from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from article.models import Article, Comments


# Create your views here.



def template_one(request):
    view = "Article title"
    return render_to_response('articles/article/article_view.html', {'name': view})


# def template_two(request):
#     view = "basic_article_two"
#     html = "<html><body>This is %s view</body></html>" % view
#     return HttpResponse(html)
#
# def template_tree(request):
#     view = "basic_article_Template"
#     t = get_template('articles/article/article_view.html')
#     html = t.render(Context({'name': view}))
#     return HttpResponse(html)

def articles(request):
    return render_to_response('articles/article/articles.html', {'articles': Article.objects.all()})


def comments(request, article_id=1):
    return render_to_response('articles/article/article.html', {
        'article': Article.objects.get(id=article_id),
        'comments': Comments.objects.filter(comments_article_id=article_id)
    })
