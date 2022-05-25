from django.contrib import admin

from nodes.models import Node


class NodeAdmin(admin.ModelAdmin):
    list_fields = ('name', 'url')


admin.site.register(Node, NodeAdmin)
