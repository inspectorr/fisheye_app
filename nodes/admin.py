from django.contrib import admin

from nodes.models import Node, Filter, FilterNode, Microservice


class MicroserviceAdmin(admin.ModelAdmin):
    list_fields = ('url',)


class NodeAdmin(admin.ModelAdmin):
    list_fields = ('name',)


class FilterNodeInline(admin.TabularInline):
    model = FilterNode


class FilterAdmin(admin.ModelAdmin):
    list_fields = ('name', 'description')
    inlines = [FilterNodeInline]


class FilterNodeAdmin(admin.ModelAdmin):
    list_fields = ('index',)
    list_select_related = ('filter', 'node',)


admin.site.register(Microservice, MicroserviceAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Filter, FilterAdmin)
admin.site.register(FilterNode, FilterNodeAdmin)

