from django.contrib import admin

from Dashboard.models import tipoDiscapacidad,sectorEconomico,rubro,categoriaOcupacional,detalleEstadisticoDiscapacitado,rangoEdades

# Register your models here.

# class ArticulosAdmin(admin.ModelAdmin):
#     list_filter=("rubro",) maneras de agregar filtros cuando desde el panel

# class ArticulosAdmin(admin.ModelAdmin):
#     list_filter=("fecha",)
#     date_hierarchy="fecha"corresponde al nombre del campo

admin.site.register(tipoDiscapacidad)
admin.site.register(sectorEconomico)
admin.site.register(rubro)
admin.site.register(categoriaOcupacional)
admin.site.register(detalleEstadisticoDiscapacitado)
admin.site.register(rangoEdades)