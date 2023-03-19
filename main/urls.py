from django.urls import path

from .views import IndexView, LoginView, LogoutView, other_page


app_name = 'main'

urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('', IndexView.as_view(), name='index'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
