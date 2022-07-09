from django.shortcuts import render, redirect
from .models import Sales
import datetime
# Create your views here.

def index(request):
    if request.method == "POST":
        datastream = request.FILES["file"]
        datastream = [x.decode("utf-8") for x in datastream]
        for x in datastream:
            x = x.split(",")
            order_date_date = x[5].split("/")
            ship_date_date = x[7].split("/")
            Sales(Region=x[0],
                  Country=x[1],
                  Item_type=x[2],
                  Sales_channel=x[3],
                  Order_priority=x[4],
                  Order_date=datetime.date(int(order_date_date[2]), int(order_date_date[0]), int(order_date_date[1])),
                  Order_id=x[6],
                  Ship_date=datetime.date(int(ship_date_date[2]), int(ship_date_date[0]), int(ship_date_date[1])),
                  Units_sold=x[8],
                  Unit_price=x[9],
                  Unit_cost=x[10],
                  Total_revenue=x[11],
                  Total_cost=x[12],
                  Total_profit=x[13]).save()
        
        
    return render(request, "tables/index.html")

last_filter = None
def results(request, filter):
    global last_filter
    if last_filter == filter:
        filter = "-" + filter
    last_filter = filter
    print(last_filter)
    sales = Sales.objects.order_by(filter)
    context = {"Sales": sales}
    return render(request, "tables/result.html", context)
    
