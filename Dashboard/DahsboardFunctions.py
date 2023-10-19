from Dashboard.models import categoriaOcupacional,tipoDiscapacidad,sectorEconomico,rubro,rangoEdades
import plotly.graph_objs as go

def GetShartTiposDiscapacidad(censo):
    discapacidades = list(tipoDiscapacidad.objects.filter(censo=censo).values_list('nombre', flat=True))
    lista_hombres = list(tipoDiscapacidad.objects.filter(censo=censo).values_list('detalle__cantidadHombre', flat=True))
    lista_mujeres = list(tipoDiscapacidad.objects.filter(censo=censo).values_list('detalle__cantidadMujeres', flat=True))
    
    if len(discapacidades) == 0:
        return None

    # Crear los objetos de datos para las dos barras
    data = [
        go.Bar(
            x=discapacidades,
            y=lista_hombres,
            name='Hombres'
        ),
        go.Bar(
            x=discapacidades,
            y=lista_mujeres,
            name='Mujeres'
        )
    ]

    # Crear el objeto de diseño del gráfico
    layout = go.Layout(
        title='Gráfico de Tipos de Discapacida',
        xaxis=dict(title='Tipo Discapacidad'),
        yaxis=dict(title='Cantidad de Discapacitados')
    )

    fig = go.Figure(data=data, layout=layout)
    graph = fig.to_html(full_html=False, default_width='100%', default_height='500px')

    return graph

def GetShartSectorEconomico(censo):
    sectores = list(sectorEconomico.objects.filter(censo=censo).values_list('nombre', flat=True))
    lista_hombres = list(sectorEconomico.objects.filter(censo=censo).values_list('detalle__cantidadHombre', flat=True))
    lista_mujeres = list(sectorEconomico.objects.filter(censo=censo).values_list('detalle__cantidadMujeres', flat=True))
    
    if len(sectores) == 0:
        return None

    # Crear los objetos de datos para las dos barras
    data = [
        go.Bar(
            x=sectores,
            y=lista_hombres,
            name='Hombres'
        ),
        go.Bar(
            x=sectores,
            y=lista_mujeres,
            name='Mujeres'
        )
    ]

    # Crear el objeto de diseño del gráfico
    layout = go.Layout(
        title='Gráfico por Sector Economico',
        xaxis=dict(title='Sector Economico'),
        yaxis=dict(title='Cantidad de Discapacitados')
    )

    fig = go.Figure(data=data, layout=layout)
    graph = fig.to_html(full_html=False, default_width='100%', default_height='500px')

    return graph

def GetShartRubros(censo):
    rubros = list(rubro.objects.filter(censo=censo).values_list('nombre', flat=True))
    lista_hombres = list(rubro.objects.filter(censo=censo).values_list('detalle__cantidadHombre', flat=True))
    lista_mujeres = list(rubro.objects.filter(censo=censo).values_list('detalle__cantidadMujeres', flat=True))
    
    if len(rubros) == 0: return None

    # Crear los objetos de datos para las dos barras
    data = [
        go.Bar(
            x=rubros,
            y=lista_hombres,
            name='Hombres'
        ),
        go.Bar(
            x=rubros,
            y=lista_mujeres,
            name='Mujeres'
        )
    ]

    # Crear el objeto de diseño del gráfico
    layout = go.Layout(
        title='Gráfico de Rubros',
        xaxis=dict(title='Rubro'),
        yaxis=dict(title='Cantidad de Discapacitados')
    )

    fig = go.Figure(data=data, layout=layout)
    graph = fig.to_html(full_html=False, default_width='100%', default_height='500px')

    return graph

def GetShartEdades(censo):
    edades = list(rangoEdades.objects.filter(censo=censo).values_list('nombre', flat=True))
    lista_hombres = list(rangoEdades.objects.filter(censo=censo).values_list('detalle__cantidadHombre', flat=True))
    lista_mujeres = list(rangoEdades.objects.filter(censo=censo).values_list('detalle__cantidadMujeres', flat=True))
    
    if len(edades) == 0: return None

    edades = [str(edad) for edad in edades]

    # Crear los objetos de datos para las dos barras
    data = [
        go.Bar(
            x=edades,
            y=lista_hombres,
            name='Hombres'
        ),
        go.Bar(
            x=edades,
            y=lista_mujeres,
            name='Mujeres'
        )
    ]

    # Crear el objeto de diseño del gráfico
    layout = go.Layout(
        title='Gráfico de Rangos de Edades',
        xaxis=dict(title='Rangos de Edad',  type='category'),
        yaxis=dict(title='Cantidad de Discapacitados')
    )

    fig = go.Figure(data=data, layout=layout)
    graph = fig.to_html(full_html=False, default_width='100%', default_height='500px')

    return graph

def GetShartCategorias(censo):
    categorias = list(categoriaOcupacional.objects.filter(censo=censo).values_list('nombre', flat=True))
    lista_hombres = list(categoriaOcupacional.objects.filter(censo=censo).values_list('detalle__cantidadHombre', flat=True))
    lista_mujeres = list(categoriaOcupacional.objects.filter(censo=censo).values_list('detalle__cantidadMujeres', flat=True))
    
    if len(categorias) == 0: return None

    # Crear los objetos de datos para las dos barras
    data = [
        go.Bar(
            x=categorias,
            y=lista_hombres,
            name='Hombres'
        ),
        go.Bar(
            x=categorias,
            y=lista_mujeres,
            name='Mujeres'
        )
    ]

    # Crear el objeto de diseño del gráfico
    layout = go.Layout(
        title='Gráfico de Categorias Ocupacionales',
        xaxis=dict(title='Categoria Ocupacional'),
        yaxis=dict(title='Cantidad de Discapacitados')
    )

    fig = go.Figure(data=data, layout=layout)
    graph = fig.to_html(full_html=False, default_width='100%', default_height='500px')

    return graph
    