from django.urls import path

from .views import IndexView, LoginView, LogoutView, other_page, profile, ChangeUserInfoView, BBPasswordChangeView, RegisterDoneView, RegisterUserView

app_name = 'main'

urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('', IndexView.as_view(), name='index'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
]
