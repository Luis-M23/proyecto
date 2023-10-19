from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from Dashboard.DahsboardFunctions import GetShartTiposDiscapacidad, GetShartCategorias, GetShartEdades, GetShartRubros, GetShartSectorEconomico
from Dashboard.models import categoriaOcupacional,tipoDiscapacidad,sectorEconomico,rubro,censo,rangoEdades,detalleEstadisticoDiscapacitado
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'dashboards/home.html')

def eliminarEntidad(request, option, idCenso, idEntidad):

    if option == "1":
        discapacidad = tipoDiscapacidad.objects.get(id=idEntidad)
        discapacidad.delete()
    elif option == "2":
        categoria = categoriaOcupacional.objects.get(id=idEntidad)
        categoria.delete()
    elif option == "3":
        edad = rangoEdades.objects.get(id=idEntidad)
        edad.delete()
    elif option == "4":
        rubro = rubro.objects.get(id=idEntidad)
        rubro.delete()
    elif option == "5":
        sector = sectorEconomico.objects.get(id=idEntidad)
        sector.delete()
    
    return redirect(reverse('eliminar', args=(idCenso,)))

def login(request):
    return render(request, 'dashboards/login.html')



def categoria(request):
    return render(request, 'dashboards/FormCategoriaOcupacional.html')

def eliminar(request, idCenso):
    anio = request.GET.get('anio')
    censoCreado = censo.objects.get(idCenso=idCenso)

    lista = []
    option=""

    if request.method == 'POST':
        option = request.POST.get('seleccion')

        if option == "1":
            lista = tipoDiscapacidad.objects.filter(censo=censoCreado)
        elif option == "2":
            lista = categoriaOcupacional.objects.filter(censo=censoCreado)
        elif option == "3":
            lista = rangoEdades.objects.filter(censo=censoCreado)
        elif option == "4":
            lista = rubro.objects.filter(censo=censoCreado)
        elif option == "5":
            lista = sectorEconomico.objects.filter(censo=censoCreado)

    return render(request, 'dashboards/eliminar.html', {'anio': anio, "lista": lista, 'idCenso': idCenso, 'option': option})

@login_required
def vistaCenso(request):
    anio = 0

    if request.method =='POST':
        anio = request.POST['anio']
    
    censoCreado, creado = censo.objects.get_or_create(anio=anio)

    return render(request, 'dashboards/censo.html', {'anioSeleccionado' : anio, 'idCenso': censoCreado.idCenso})

def lista_Categoria(request, idCenso):

    anio = request.GET.get('anio')

    if request.method =='POST':
        nombre = request.POST['categoria']
        canHombre = request.POST['canHombres']
        canMujeres = request.POST['canMujeres']
   
        censoCreado = censo.objects.get(idCenso=idCenso)
        
        detalle = detalleEstadisticoDiscapacitado.objects.create(
            cantidadHombre=canHombre,
            cantidadMujeres=canMujeres
        )

        categoriaOcupacional.objects.create(
            nombre=nombre,
            detalle=detalle,
            censo=censoCreado
        )

    return render(request,'dashboards/FormCategoriaOcupacional.html', {'anio': anio})

def lista_Discapacidad(request, idCenso):
    anio = request.GET.get('anio')

    if request.method =='POST':
        nombre = request.POST['tipoDis']
        canHombre = request.POST['canHombres']
        canMujeres = request.POST['canMujeres']

        censoCreado = censo.objects.get(idCenso=idCenso)

        detalle = detalleEstadisticoDiscapacitado.objects.create(
            cantidadHombre=canHombre,
            cantidadMujeres=canMujeres
        )

        tipoDiscapacidad.objects.create(
            nombre=nombre,
            detalle=detalle,
            censo=censoCreado
        )
    
    return render(request,'dashboards/FormTipoDiscapacidad.html', {'anio': anio})

def lista_SectorEconomico(request, idCenso):
    
    anio = request.GET.get('anio')
      
    if request.method =='POST':
        nombre = request.POST['tipoSecE']
        canHombre = request.POST['canHombres']
        canMujeres = request.POST['canMujeres']
   
        censoCreado = censo.objects.get(idCenso=idCenso)

        detalle = detalleEstadisticoDiscapacitado.objects.create(
            cantidadHombre=canHombre,
            cantidadMujeres=canMujeres
        )

        sectorEconomico.objects.create(
            nombre=nombre,
            detalle=detalle,
            censo=censoCreado
        )

    return render(request,'dashboards/FormSectorEconomico.html', {'anio': anio})

def lista_Rubro(request,idCenso):
     
    anio = request.GET.get('anio')
    
    if request.method =='POST':
        nombre = request.POST['rubro']
        canHombre = request.POST['canHombres']
        canMujeres = request.POST['canMujeres']
   
        censoCreado = censo.objects.get(idCenso=idCenso)

        detalle = detalleEstadisticoDiscapacitado.objects.create(
            cantidadHombre=canHombre,
            cantidadMujeres=canMujeres
        )

        rubro.objects.create(
            nombre=nombre,
            detalle=detalle,
            censo=censoCreado
        )

    return render(request,'dashboards/FormRubro.html', {'anio': anio})

def lista_RangoEdad(request, idCenso):
    anio = request.GET.get('anio')

    if request.method =='POST':
        nombre = request.POST['edad']
        canHombre = request.POST['canHombres']
        canMujeres = request.POST['canMujeres']
   
        censoCreado = censo.objects.get(idCenso=idCenso)

        detalle = detalleEstadisticoDiscapacitado.objects.create(
            cantidadHombre=canHombre,
            cantidadMujeres=canMujeres
        )

        rangoEdades.objects.create(
            nombre=nombre,
            detalle=detalle,
            censo=censoCreado
        )

    return render(request,'dashboards/FormRangoEdad.html', {'anio': anio})

def detail(request):
    censos = censo.objects.all()

    censoUse, create = censo.objects.get_or_create(idCenso=1, anio=0)

    if request.method =='POST':
        censoId = request.POST['censo']
        censoUse = censo.objects.get(idCenso=int(censoId))

    graphDiscapacidades = GetShartTiposDiscapacidad(censoUse)
    graphCategories = GetShartCategorias(censoUse)
    graphEdades = GetShartEdades(censoUse)
    graphRubros = GetShartRubros(censoUse)
    graphSectores = GetShartSectorEconomico(censoUse)

    return render(request, 'dashboards/dashboard.html', {'lista': censos,'disc': graphDiscapacidades, 'cats': graphCategories, 'edades': graphEdades, 'rubros': graphRubros, 'sectores': graphSectores})