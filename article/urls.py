from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^1/', views.template_one),#'article.views.template_one'),  # ссылка на ф-цию в представлении
    url(r'^all/$', views.articles),
    url(r'^article/get/(?P<article_id>\d+)/$', views.articles), #


]
