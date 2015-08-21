def json_only(func):
  def ret(*args):
    request = args[0]
    if (request.is_ajax() and
            re.match(r"application/json", request.META["CONTENT_TYPE"])):
      return func(*args)
    else:
      return HttpResponse("Accepts application/json only")
  return ret
