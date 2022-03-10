from django.urls import path 
from .views import ArticleDetails , ArticleAPIView

urlpatterns = [
    path('article/'  ,ArticleAPIView.as_view()  ),
    path('details/<int:id>/'  ,ArticleDetails.as_view()),
]
