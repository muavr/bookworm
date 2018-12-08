from django.urls import path
from bookwormapp import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

app_name = 'bookworm'
urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('members/login/', LoginView.as_view(
        template_name='bookwormapp/login.html'), name='login'),
    path('members/logout/', LogoutView.as_view(), name='logout'),
    path('members/password_change/', PasswordChangeView.as_view(
        template_name='bookwormapp/password_change_form.html',
        success_url='/members/password_change_done/'), name='password_change'),
    path('members/password_change_done/', PasswordChangeDoneView.as_view(
        template_name='bookwormapp/password_change_done.html'),  name='password_change_done')

]
