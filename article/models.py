from django.db import models

# Create your models here.


class Article(models.Model): # Статья
    class Meta:
        db_table = 'article'

    article_title = models.CharField(verbose_name='Название статьи', max_length=200)
    article_text = models.CharField(verbose_name='Текст статьи', max_length=800)
    article_date = models.DateTimeField(verbose_name='Добавлена')
    article_likes = models.IntegerField(default=0, editable=False) # editable - скрывает поле в админке


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = models.CharField(verbose_name='Комментарий', max_length=400)
    comments_article = models.ForeignKey(Article, editable=False) # Связь с таблицей статей

