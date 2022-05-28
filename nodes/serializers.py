from rest_framework import serializers

from nodes.models import Filter, FilterNode


class UrlSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    req_fields = serializers.SerializerMethodField()
    res_fields = serializers.SerializerMethodField()

    @staticmethod
    def get_node(obj):  # todo
        return obj.node

    def get_url(self, obj):
        return self.get_node(obj).get_full_url()

    def get_req_fields(self, obj):
        return set(self.get_node(obj).req_fields.split(','))

    def get_res_fields(self, obj):
        return set(self.get_node(obj).res_fields.split(','))

    class Meta:
        model = FilterNode
        fields = ('id', 'url', 'default_json_params', 'req_fields', 'res_fields', 'node')


class UrlListSerializer(serializers.ModelSerializer):
    urls = UrlSerializer(source='get_ordered_filter_nodes', many=True)

    class Meta:
        model = Filter
        fields = ('urls',)


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = ('name', 'description')