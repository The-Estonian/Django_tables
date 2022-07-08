from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.method == "POST":
        datastream = request.FILES["file"]
        for x in datastream:
            print(x.decode("utf-8"))
        datastream = [x.decode("utf-8") for x in datastream]
        context = {"datastream": datastream}
        return render(request, "tables/result.html", context)
        
    return render(request, "tables/index.html")


    
