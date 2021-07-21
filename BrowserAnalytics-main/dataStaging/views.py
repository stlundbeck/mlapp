from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http  import HttpResponse
from .models import flatfile
from .models import stagedflatfile

def upload_views(request):

    site="upload.html"
    data={}
    print(request.POST.keys(), "hello <--------------------")
    for i in request.POST.items():

        print(i, "hello <--------------------")

    # Navigates to the page where data can be displayed

    if request.method == "POST" and "staging" in request.POST.keys():
        post = stagedflatfile()

        post.a="1"
        post.b="2"
        post.c="3"
        post.save()

        print("--------------------", request.POST["staging"], "-------", request.POST.items(), "------------------------")

        site = "listofuploads.html"
        data = {}

        for i in flatfile.objects.all():
            print(i.id, i.fileName)
            data[str(i.id)] = i.fileName
        print(data)



    elif request.method == "POST" and "id" in request.POST.keys():
        #setting the page to be shown
        site = "staging.html"
        #requesting the data for the particular data to be staged
        obj = flatfile.objects.all()[int(request.POST["id"])-1]
        #printing to terminal the data just retrieved from the database
        print(obj.flatFile, obj.fileName)
        #defining the data just retrieved from the database to the model passed to the view
        data={request.POST["id"]:{"fileName":obj.fileName, "flatFile":obj.flatFile}}

    # Navigate to the staging page with a list over files that can be staged
    elif request.method=="POST":
        # creates a table called flatfile and opens a connection.
        post=flatfile()
        # assigning the upload file a reference
        uploaded_file=request.FILES["document"]
        # assigning the value to a column in the database
        post.fileName = uploaded_file.name
        # assigning the value to a column in the database
        post.flatFile = str(uploaded_file.read(), "utf-8")
        # saving/committing to the database
        post.save()
        # Defining a new view to be returned
        site="listofuploads.html"
        data={}

        for i in flatfile.objects.all():
            print(i.id, i.fileName)
            data[str(i.id)]=i.fileName
        print(data)
    # request must always be passed in the return, site defines the view template to return, last is the data available in the view
    return render(request, site, {"dictionary":data})
