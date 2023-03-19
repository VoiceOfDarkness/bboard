from django.urls import path
from .views import profile, ChangeUserInfoView, BBPasswordChangeView, RegisterDoneView, RegisterUserView, user_activate

app_name = 'user'

urlpatterns = [
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/activate/', user_activate, name='register_activate'),
]
