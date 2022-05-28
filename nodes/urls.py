from django.urls import path, include

from nodes.views import ExecuteFilterView, RetrieveFilterView

app_name = 'nodes'


urlpatterns = [
    path('filter/<int:filter_id>/', include([
        path('', RetrieveFilterView.as_view(), name='retrieve_filter'),
        path('execute/', ExecuteFilterView.as_view(), name='execute_filter'),
    ])),
]
