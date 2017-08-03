from django.conf.urls import url
from article import views
from . import views

urlpatterns = [
    url(r'^1/', views.template_one),#'article.views.template_one'),  # ссылка на ф-цию в представлении
]
