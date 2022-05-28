from django.urls import path, include

from nodes.views import ExecuteFilterView

app_name = 'nodes'


urlpatterns = [
    path('filter/<int:filter_id>/', include([
        path('execute/', ExecuteFilterView.as_view(), name='execute_filter'),
    ])),
]
