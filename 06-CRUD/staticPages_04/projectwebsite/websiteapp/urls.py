

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name="home"),
    path('websiteapp/<int:pk>', views.ArticleDetailView.as_view(), name="page_detail"),
    path('websiteapp/new/', views.CreateArticleView.as_view(), name='new_article'),
    path('websiteapp/<int:pk>/edit', views.CreateUpdateView.as_view(), name='article_edit'),
    path('websiteapp/<int:pk>/delete', views.CreateDeleteView.as_view(), name='article_delete'),
]
