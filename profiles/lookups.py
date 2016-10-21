from ajax_select import register, LookupChannel
from .models import *
from django.utils.six import text_type
from django.utils.html import escape

@register('homeCourse')
class CourseLookup(LookupChannel):

    model = Profile

    def get_query(self, q, request):
        return HomeCourse.objects.filter(code__icontains=q).order_by('code')

    def get_result(self, obj):
        return text_type(obj.name)

    def format_match(self, obj):
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        return "<span class="">%s, %s </span>" % (escape(obj.code), escape(obj.name))