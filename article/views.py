from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

# Create your views here.

#def basic_article_one(request):
    #view = "basic_article_one"
    #html = "<html><body>This is %s view</body></html>" % view

    #return HttpResponse(html)

def template_one(request):
    view = "Name"
    return render_to_response('articles/article/article_view.html', {'name': view})

    # view = "basic_article_Template"
    # t = get_template('articles/article/article_view.html')
    # html = t.render(Context({'name': view}))
    # return HttpResponse(html)
#l', {'cart': cart})