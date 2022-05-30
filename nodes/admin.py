from django.contrib import admin

from nodes.models import Node, Filter, FilterNode, Microservice, StaticImage, FilterBenchmark


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
    list_fields = ('index', 'enabled')
    list_select_related = ('filter', 'node')


class StaticImageAdmin(admin.ModelAdmin):
    list_fields = ('image',)


class FilterBenchmarkAdmin(admin.ModelAdmin):
    list_fields = ('ms',)
    list_select_related = ('filter',)


admin.site.register(Microservice, MicroserviceAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Filter, FilterAdmin)
admin.site.register(FilterNode, FilterNodeAdmin)
admin.site.register(StaticImage, StaticImageAdmin)
admin.site.register(FilterBenchmark, FilterBenchmarkAdmin)

