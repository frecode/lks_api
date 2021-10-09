from django.urls import path
from app01 import views

urlpatterns = [
    path('web', views.ApiWeb.as_view()),
    path('web_version', views.ApiWebVersion.as_view()),
    path('db_content', views.TestMail.as_view()),
]
