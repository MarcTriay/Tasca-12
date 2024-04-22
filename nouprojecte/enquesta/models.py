from django.db import models
class Pregunta(models.Model):
	text_pregunta = models.CharField(max_length=200)
	data_publicacio = models.DateTimeField("data publicació")
class Opcio(models.Model):
	pregunta=models.ForeignKey(Pregunta, on_delete= models.CASCADE)
	text_opcio = models.CharField(max_length=200)
	vots = models.IntegerField(default=0)
