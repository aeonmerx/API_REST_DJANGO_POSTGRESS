from django.shortcuts import render

# En api/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Animal, Planta, Vehiculo
import json

@csrf_exempt
def animal_list(request):
    if request.method == 'GET':
        animales = Animal.objects.all()
        data = [{'nombre': animal.nombre, 'edad': animal.edad} for animal in animales]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        animal = Animal.objects.create(nombre=data['nombre'], edad=data['edad'])
        return JsonResponse({'nombre': animal.nombre, 'edad': animal.edad}, status=201)

@csrf_exempt
def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)

    if request.method == 'GET':
        data = {'nombre': animal.nombre, 'edad': animal.edad}
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        animal.nombre = data['nombre']
        animal.edad = data['edad']
        animal.save()
        return JsonResponse({'nombre': animal.nombre, 'edad': animal.edad})

    elif request.method == 'DELETE':
        animal.delete()
        return HttpResponse(status=204)

# Funciones CRUD para Planta
@csrf_exempt
def planta_list(request):
    if request.method == 'GET':
        plantas = Planta.objects.all()
        data = [{'nombre': planta.nombre, 'tipo': planta.tipo} for planta in plantas]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        planta = Planta.objects.create(nombre=data['nombre'], tipo=data['tipo'])
        return JsonResponse({'nombre': planta.nombre, 'tipo': planta.tipo}, status=201)

@csrf_exempt
def planta_detail(request, pk):
    planta = get_object_or_404(Planta, pk=pk)

    if request.method == 'GET':
        data = {'nombre': planta.nombre, 'tipo': planta.tipo}
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        planta.nombre = data['nombre']
        planta.tipo = data['tipo']
        planta.save()
        return JsonResponse({'nombre': planta.nombre, 'tipo': planta.tipo})

    elif request.method == 'DELETE':
        planta.delete()
        return HttpResponse(status=204)

# Funciones CRUD para Vehiculo
@csrf_exempt
def vehiculo_list(request):
    if request.method == 'GET':
        vehiculos = Vehiculo.objects.all()
        data = [{'marca': vehiculo.marca, 'modelo': vehiculo.modelo} for vehiculo in vehiculos]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        vehiculo = Vehiculo.objects.create(marca=data['marca'], modelo=data['modelo'])
        return JsonResponse({'marca': vehiculo.marca, 'modelo': vehiculo.modelo}, status=201)

@csrf_exempt
def vehiculo_detail(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)

    if request.method == 'GET':
        data = {'marca': vehiculo.marca, 'modelo': vehiculo.modelo}
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        vehiculo.marca = data['marca']
        vehiculo.modelo = data['modelo']
        vehiculo.save()
        return JsonResponse({'marca': vehiculo.marca, 'modelo': vehiculo.modelo})

    elif request.method == 'DELETE':
        vehiculo.delete()
        return HttpResponse(status=204)