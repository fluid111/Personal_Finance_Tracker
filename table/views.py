import matplotlib
matplotlib.use('Agg') 

from django.shortcuts import render

from django.db import models  # Add this line

import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
import base64
from api.models import Data
# import urllib, base64

# Create your views here.
def list(request):
    return render(request, 'table/index.html')

def category_chart_view(request):
  try:
    # Fetch and aggregate data by category
    category_data = Data.objects.values('category').annotate(total_amount=models.Sum('amount'))

    print("Category Data:", category_data)

    categories = [entry['category'] for entry in category_data]
    # amounts = [entry['total_amount'] for entry in category_data]
    amounts = [entry['total_amount'] for entry in category_data]


    # Create a bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(categories, amounts, color='blue')
    plt.title('Total Amount by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')

    plt.yticks(range(0, int(max(amounts) + 10), 10))
    
    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    # Encode to base64
    image_png = buffer.getvalue()
    graphic = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'table/chart.html', {'graphic':graphic})
    # return HttpResponse(f'<img src="data:image/png;base64,{graphic}"/>')
  except Exception as e:
    print("Error occurred:", e)  # Print error for debugging
    return HttpResponse("An error occurred while generating the chart.")


def searchTable(request):        
    if request.method == 'GET':   
        searchBasis=  request.GET.get('searchInput') # do some research what it does       
        if searchBasis:
            try:
              searchedItems = Data.objects.filter(category__icontains=searchBasis) # filter returns a list so you might consider skip except part
              return render(request,"table/search.html",{"searchedItems":searchedItems})
            except Exception as e:  # Catch any exceptions that might occur
            # Handle the exception or log it
              print("error")
              return render(request, "table/search.html", {})
        else: 
            print("no result found")
            return render(request, "table/search.html", {})
    else:
        return render(request,'table/search.html',{"searchedItems":searchedItems})