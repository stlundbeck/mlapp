from django.shortcuts import render
from django.views import View
# Create your views here.



class MainView(View):

    def get(self, request):

        links = ["https://www.youtube.com/watch?v=Z4D3M-NSN58&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9",
                 "https://www.dj4e.com/"]

        context = {
            "links": links
        }

        return render(request, "home/home.html", context)

def home_view(request):
    return render(request, "home/home.html")