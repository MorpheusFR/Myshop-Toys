from django.db import models

# Create your models here.


class Article(models.Model): # Статья
    class Meta:
        db_table = 'article'

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0, editable=False) # editable - скрывает поле в админке


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = models.TextField(verbose_name='Комментарий')
    comments_article = models.ForeignKey(Article, editable=False) # Связь с таблицей статей

