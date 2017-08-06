from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/', views.template_one),  # 'article.views.template_one'),  # ссылка на ф-цию в представлении
    url(r'^all/$', views.articles),
    url(r'^get/(?P<article_id>\d+)/$', views.article),  #

]
