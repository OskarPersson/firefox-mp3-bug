import os

from django.http.response import HttpResponse

def index(r):
    path = 'output.mp3'
    content_type = 'audio/mpeg'

    file_obj = open(path)
    response = HttpResponse(file_obj.read(), content_type=content_type)
    response['Content-Disposition'] = 'inline; filename=%s' % os.path.basename(file_obj.name)
    return response
