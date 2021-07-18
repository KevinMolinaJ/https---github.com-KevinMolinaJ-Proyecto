
from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns=[
    url(r'^api/noticias/$', views.NoticiasViewSet.as_view()),
    url(r'^api/noticiacrear/$', views.NoticiasCreateViewSet.as_view()),
    url(r'^api/noticia/(?P<titulo>.+)/$', views.NoticiasBuscarViewSet.as_view()),
]

urlpatterns= format_suffix_patterns(urlpatterns)


#urlpatterns= format_suffix_patterns(urlpatterns)
