import logging

from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from nodes.exceptions import NodeRequestException
from nodes.helpers import UrlListRunner, FilterBenchmarkRunner
from nodes.models import Filter
from nodes.serializers import UrlListSerializer, FilterSerializer, FilterBenchmarkSerializer


class ExecuteFilterView(APIView):
    def post(self, *args, **kwargs):
        filter_id = kwargs.get('filter_id')
        the_filter = get_object_or_404(Filter, id=filter_id)
        urls = UrlListSerializer(the_filter).data['urls']
        benchmark = FilterBenchmarkRunner(filter_id, request_json=self.request.data)
        try:
            result = UrlListRunner(serialized_urls=urls).run(initial_data=self.request.data)
            return Response({
                'data': result,
                'benchmark': FilterBenchmarkSerializer(benchmark.end(response_json=result)).data,
            })
        except NodeRequestException as e:
            logging.exception(e)
            return Response(e.to_dict())
        except Exception as e:
            logging.exception(e)
            return Response({
                'error': 'Unexpected error',
                'details': str(e)
            })


class RetrieveFilterView(APIView):
    def get(self, *args, **kwargs):
        the_filter = get_object_or_404(Filter, id=kwargs.get('filter_id'))
        return Response(FilterSerializer(the_filter).data)


class ListFilterView(ListAPIView):
    queryset = Filter.objects.filter(enabled=True)
    serializer_class = FilterSerializer
