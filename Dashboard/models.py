from django.db import models

# Create your models here.

class censo(models.Model):
    idCenso=models.AutoField(primary_key=True)
    anio=models.IntegerField(verbose_name="Anio Censo")
    
    def __str__(self):
        return self.rangoEdad
    
class detalleEstadisticoDiscapacitado(models.Model):
    cantidadHombre=models.IntegerField()
    cantidadMujeres=models.IntegerField()

    def __str__(self):
        return f"Hombres: {self.cantidadHombre} Mujeres: {self.cantidadMujeres}"

class tipoDiscapacidad(models.Model):
    id= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30,verbose_name="Nombre Discapacidad")
    detalle=models.ForeignKey(detalleEstadisticoDiscapacitado, null=True, blank=True, on_delete=models.CASCADE)
    censo=models.ForeignKey(censo, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
	    return self.nombre
    
    
class sectorEconomico(models.Model):
    
    nombre=models.CharField(max_length=30,verbose_name="Nombre Sector")
    detalle=models.ForeignKey(detalleEstadisticoDiscapacitado, null=True, blank=True, on_delete=models.CASCADE)
    censo=models.ForeignKey(censo, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class rubro(models.Model):
    nombre=models.CharField(max_length=30,verbose_name="Nombre Rubro")
    detalle=models.ForeignKey(detalleEstadisticoDiscapacitado, null=True, blank=True, on_delete=models.CASCADE)
    censo=models.ForeignKey(censo, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class categoriaOcupacional(models.Model):
   
    nombre=models.CharField(max_length=30,verbose_name="Nombre Categoria")
    detalle=models.ForeignKey(detalleEstadisticoDiscapacitado, null=True, blank=True, on_delete=models.CASCADE)
    censo=models.ForeignKey(censo, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class rangoEdades(models.Model):
    nombre=models.CharField(max_length=5,verbose_name="Rango Edad")
    detalle=models.ForeignKey(detalleEstadisticoDiscapacitado, null=True, blank=True, on_delete=models.CASCADE)
    censo=models.ForeignKey(censo, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre