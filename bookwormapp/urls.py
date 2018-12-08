from django.urls import path
from bookwormapp import views

app_name = 'bookworm'
urlpatterns = [
    path('', views.home_page, name='bookworm-home_page')
]
