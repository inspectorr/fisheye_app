from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from application import settings


class SPAView(TemplateView):
    template_name = 'spa.html'


urlpatterns = [
    path('', SPAView.as_view()),
    path('admin/', admin.site.urls),
    path('nodes/', include('nodes.urls')),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
