from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, DataSerializer , DataCreateSerializer

from .models import User,Data

# Create your views here.
def apiOverview(request):
    # return JsonResponse("This is API base point", safe=False)
    return render(request, 'index.html')

@api_view(['GET'])
def userlist(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userdetail(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def usercreate(request):
    serializer = UserSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def userupdate(request, pk):
    users  = User.objects.get(id=pk)
    serializer = UserSerializer(instance=users, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
 
@api_view(['DELETE'])
def userdelete(request, pk):
    users  = User.objects.get(id=pk)
    users.delete()
    return Response("successfully delete")



    Data
@api_view(['GET'])
def datalist(request):
    data = Data.objects.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def datadetail(request, pk):
    data = Data.objects.get(id=pk)
    serializer = DataSerializer(data, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def datacreate(request):
    print("Received data:", request.data)
    serializer = DataCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.data, status=400)

@api_view(['POST'])
def dataupdate(request, pk):
    data = Data.objects.get(id=pk)
    serializer = UserSerializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.data)
 
@api_view(['DELETE'])
def datadelete(request, pk):
    data  = Data.objects.get(id=pk)
    data.delete()
    return Response("successfully delete")
    
# def dataCreate(request):
#     return JsonResponse("Enter data",safe=False)