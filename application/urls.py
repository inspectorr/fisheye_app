from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from application import settings


class SPAView(TemplateView):
    template_name = 'spa.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('nodes/', include('nodes.urls')),
    ])),
    re_path(r'^', SPAView.as_view()),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
