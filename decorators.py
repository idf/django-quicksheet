import re
from django.http import HttpResponse

def json_only(func):
  def ret(*args, **kwargs):
    request = args[0]
    if (request.is_ajax() and
            re.match(r"application/json", request.META["CONTENT_TYPE"])):
      return func(*args, **kwargs)
    else:
      return HttpResponse("Accepts application/json only")
  return ret
