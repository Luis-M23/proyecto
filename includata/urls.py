from django.contrib import admin
from django.urls import path, include
from Dashboard.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('includata/dashboard/', detail, name='dashboard'),
    path('admin/', admin.site.urls),
    path('includata/dashboards/censo/', vistaCenso, name="vista_censos"),
    path('includata/dashboards/<int:idCenso>/FormCategoriaOcupacional/', lista_Categoria, name='lista_Categoria'),
    path('includata/dashboards/<int:idCenso>/FormTipoDiscapacidad/', lista_Discapacidad, name='lista_Discapacidad'),
    path('includata/dashboards/<int:idCenso>/FormSectorEconomico/', lista_SectorEconomico, name='lista_SectorEconomico'),
    path('includata/dashboards/<int:idCenso>/FormRubro/', lista_Rubro, name='lista_Rubro'),
    path('includata/dashboards/<int:idCenso>/FormRangoEdad/', lista_RangoEdad, name='lista_RangoEdad'),
    path('includata/dashboards/<int:idCenso>/eliminar', eliminar, name='eliminar'),
    path('includata/dashboards/<int:idCenso>/eliminar-entidad/<int:idEntidad>/tipo/<str:option>', eliminarEntidad, name='eliminar_entidad'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/login/', LoginView.as_view(), name='login'),
]
