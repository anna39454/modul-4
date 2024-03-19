from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()

#Параметр декоратора takes_context=True сообщает Django, что для работы тега требуется передать контекст.
# Именно тот контекст, который мы редактировали.

#context['request'].GET.copy() нам позволяет скопировать все параметры текущего запроса.