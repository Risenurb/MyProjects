from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import FoodSuggestion
from .models import Price
import pandas as pd
from .serializers import FoodSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import FoodsuggestionForm



def menu(request):
    objectsFood = FoodSuggestion.objects.all()
    objectsPrice = Price.objects.all()
    return render(request,'food.html',{"objectsFood":objectsFood,"objectsPrice":objectsPrice})

def addFood(request):
    form = FoodsuggestionForm()
    if request.method == "POST":
        form = FoodsuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    context1 = {'form':form}
    return render(request,'food-form.html',context1)

def result(request):
    objectsFood = FoodSuggestion.objects.all()
    objectsPrice = Price.objects.all()
    try:
        value1 = request.POST['foodlist1']
        value2 = request.POST['foodlist2']
        value3 = request.POST['foodlist0']
    except Exception:
        print("ohhh sorryyyyy")
    for j in range(len(objectsPrice)):
        counter = False

        if value3 == objectsPrice[j].price_range1:
            return render(request, 'foodresult.html',
                { "objectsPrice": objectsPrice,
                "objectsPrice1": objectsPrice[j]})


    for i in range(len(objectsFood)):
        counter = True
        print(counter)
        print("Checked 1 condition")
        if value1 == objectsFood[i].ingredient2 and value2 == objectsFood[i].ingredient3:
            print("passed first condition")
            return render(request, 'foodresult.html',
                        {"objectsFood":objectsFood,"objectsFood1":objectsFood[i],"objectsPrice":objectsPrice,"objectsPrice1":objectsPrice[j],"counter": counter})

        elif value2 == objectsFood[i].ingredient2 and value1 == objectsFood[i].ingredient3 :
            print("passed 2 condition")
            return render(request, 'foodresult.html',{"objectsFood":objectsFood,"objectsFood1":objectsFood[i],"objectsPrice":objectsPrice,"objectsPrice1":objectsPrice[j],"counter": counter})
        elif value2 == objectsFood[i].ingredient2 or value1 == objectsFood[i].ingredient2 or value1 == objectsFood[i].ingredient3 or value1 == objectsFood[i].ingredient4 or value2 == objectsFood[i].ingredient4:
            print("passed 3 condition")
            return render(request, 'foodresult.html',
                        {"objectsFood":objectsFood,"objectsFood1":objectsFood[i],"objectsPrice":objectsPrice,"objectsPrice1":objectsPrice[j],"counter": counter})

    return render(request, 'foodexception.html')


@api_view(["GET","POST"])
def foodList(request):
    #get all food igredients
    #serialize them
    #return json
    if request.method == "GET":
        fooditems = FoodSuggestion.objects.all()
        serializer = FoodSerializer(fooditems,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == "POST":
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(["GET","PUT","DELETE"])
def fooditem(request,id):
    try:
        fooditems = FoodSuggestion.objects.get(pk=id)
    except fooditems.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#
    if request.method == "GET":
        serializer = FoodSerializer(fooditems)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer =FoodSerializer(fooditems, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors(),status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        fooditems.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






