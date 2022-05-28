from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from nodes.helpers import UrlListRunner, NodeRequestException
from nodes.models import Filter
from nodes.serializers import UrlListSerializer


class ExecuteFilterView(APIView):
    def post(self, *args, **kwargs):
        the_filter = get_object_or_404(Filter, id=kwargs.get('filter_id'))
        urls = UrlListSerializer(the_filter).data['urls']
        try:
            result = UrlListRunner(serialized_urls=urls).run(initial_data=self.request.data)
            return Response(result)
        except NodeRequestException as e:
            return Response(e.to_dict())
