from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/', views.template_one),  # 'article.views.template_one'),  # ссылка на ф-цию в представлении
    url(r'^all/$', views.articles), # Все статьи
    url(r'^get/(?P<article_id>\d+)/$', views.article),  # Статья по переходу
    url(r'^get/add_like/(?P<article_id>\d+)/$', views.add_like),
    url(r'^get/add_comment/(?P<article_id>\d+)/$', views.add_comment),

]
