from django.shortcuts import HttpResponse
from django.views.generic.base import View

class like_verse_api(View):
    def post(self, request, **kwargs):
        is_active = request.POST.get('is_active')
        verseid = request.POST.get('verseid')
        print(is_active, verseid)