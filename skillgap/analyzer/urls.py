from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),   # ✅ THIS LINE MUST MATCH
    path('ai/', views.ai_response, name='ai_response'),
]
