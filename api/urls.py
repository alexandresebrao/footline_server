"""footline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from api.v1.views import auth
from api.admin import register


urlpatterns = [
    url(r'^admin/registertoken/$', register.RegisterTokenAPIView.as_view()),
    url(r'^admin/registertoken/(?P<pk>[0-9]+)/$',
        register.RegisterTokenDetail.as_view()),
    url(r'^v1/auth/registertoken/(?P<token>\w+)/$',
        auth.VerifyToken.as_view()),
    url(r'^v1/auth/register/', auth.RegisterUserAPI.as_view()),
    url(r'^v1/auth/login/', auth.LoginAPI.as_view()),
]
