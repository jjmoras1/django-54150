from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template,Context,loader
from datetime import datetime
import random
from inicio.models import Auto



def inicio(request):
    # return HttpResponse('Bienvenidos a mi inicio')
    return render(request,'inicio/index.html')
def template1(request,nombre,apellido):
    fecha=datetime.now()
    return HttpResponse(f'<h1>Mi template fecha</h1>  {fecha}, hola {nombre} {apellido}')






def template2(request,nombre,apellido):
    archivo_abierto=open(r'C:\Users\jjmor\OneDrive\Documentos\Cursos Data\coderhouse\Python\mi-proyecto\templates\template2.html')
    
    template=Template(archivo_abierto.read())
    
    archivo_abierto.close()
    fecha=datetime.now()
    datos={'fecha':fecha,'nombre':nombre,'apellido':apellido}
    contexto=Context(datos)
    template_renderizado=template.render(contexto)
    return HttpResponse(template_renderizado)


def template3(request,nombre,apellido):
    template=loader.get_template('template2.html')
    fecha=datetime.now()
    datos={'fecha':fecha,'nombre':nombre,'apellido':apellido}
    
    template_renderizado=template.render(datos)
    return HttpResponse(template_renderizado)

def template4(request,nombre,apellido):
    
    fecha=datetime.now()
    datos={'fecha':fecha,'nombre':nombre,'apellido':apellido}
    
    
    return render(request,'template2.html',datos)

def probando(request):
    lista=list(range(500))
    numeros=random.choices(lista,k=50)
    print(numeros)
    return render(request,"probando_if_for.html",{'numeros':numeros})

def crear_auto(request,marca,modelo):
    auto=Auto(marca=marca,modelo=modelo)
    auto.save()
    return render(request,'auto_templates\creacion.html',{'auto':auto})