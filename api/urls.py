from django.conf.urls import url
from api.v1.views import auth, news
from api.admin import register


urlpatterns = [
    url(r'^admin/registertoken/$', register.RegisterTokenAPIView.as_view()),
    url(r'^admin/registertoken/(?P<pk>[0-9]+)/$',
        register.RegisterTokenDetail.as_view()),
    url(r'^v1/auth/registertoken/(?P<token>\w+)/$',
        auth.VerifyToken.as_view()),
    url(r'^v1/auth/register/', auth.RegisterUserAPI.as_view()),
    url(r'^v1/auth/', auth.LoginAPI.as_view()),
    url(r'^v1/news/', news.NewsAPIView.as_view()),
]
