from django.contrib import admin

from nodes.models import Node, Filter, FilterNode, Microservice


class MicroserviceAdmin(admin.ModelAdmin):
    list_fields = ('url',)


class NodeAdmin(admin.ModelAdmin):
    list_fields = ('base_url', 'name')


class FilterAdmin(admin.ModelAdmin):
    list_fields = ('name', 'description')
    # todo display nodes


class FilterNodeAdmin(admin.ModelAdmin):
    list_select_related = ('filter', 'node_value', 'next_filter_node')


admin.site.register(Microservice, MicroserviceAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Filter, FilterAdmin)
admin.site.register(FilterNode, FilterNodeAdmin)

