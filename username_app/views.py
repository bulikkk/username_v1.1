from django.shortcuts import render
from django.views import View

# Create your views here.


class MainView(View):
    def get(self, request):
        ctx = {}
        return render(request, 'username_app/main.html', ctx)
