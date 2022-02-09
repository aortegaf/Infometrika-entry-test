from django.urls import path, include
from .router import router
from library_api import views

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name="home"),
    path("update/", views.update, name="update"),
    path('test/', views.test, name="test")
]
