from django.urls import path

from .views import BBLoginView, BBLogoutView, IndexView, other_page

app_name = 'main'

urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('', IndexView.as_view(), name='index'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
]
