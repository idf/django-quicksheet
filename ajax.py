from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from decorators import json_only

__author__ = 'Daniel'


class AjaxView(View):
  @method_decorator(json_only)
  @method_decorator(csrf_exempt)
  def dispatch(self, *args, **kwargs):
    return super(AjaxView, self).dispatch(*args, **kwargs)
