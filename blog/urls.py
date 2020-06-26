from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('post/new/', views.BlogCreateView.as_view(), name='create'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('', views.BlogListView.as_view(), name='home'),
]
