from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_view, name='resume'),
    path('blog-grid/', views.blog_grid, name='blog-grid'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('portfolio-detail/', views.portfolio_detail, name='portfolio-detail'),
]
