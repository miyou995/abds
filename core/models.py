from django.db import models
from django.conf import settings
from .choices import CYL_CHOICES, SPHER_CHOICES
# Create your models here.

EYE_CHOICES = [
        ('OD', 'OD'),
        ('OG', 'OG'),
    ]

PROGRESSIF_CHOICES = [
        ('LOIN', 'LOIN'),
        ('PRES', 'PRES'),
    ]
MENTURE_CHOICES = [
    ('PLASTIQUE', 'PLASTIQUE'),
    ('METALIQUE', 'METALIQUE'),
    ('SOLAIRE', 'SOLAIRE'),
]


class GlassType(models.Model):
    name = models.CharField( max_length=150, blank=True, null=True)
    def __str__(self):
        return self.name
    
class LentilType(models.Model):
    name = models.CharField( max_length=150, blank=True, null=True)
    def __str__(self):
        return self.name

class Client(models.Model):
    name    = models.CharField( max_length=150)
    magasin = models.ForeignKey("business.Magasin", verbose_name="Magasin", on_delete=models.CASCADE, blank=True, null=True)
    age     = models.IntegerField(blank=True, null=True)
    prenom  = models.CharField( max_length=150, blank=True, null=True)
    phone   = models.CharField( max_length=150, blank=True, null=True)
    address = models.CharField( max_length=150, blank=True, null=True)
    note  = models.TextField(blank=True, null=True)
    doctor      = models.CharField( max_length=150, blank=True, null=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client              = models.ForeignKey(Client, related_name="orders", on_delete=models.CASCADE)
    date                = models.DateField(auto_now=False, auto_now_add=False)
    total               = models.IntegerField(default=0)
    versement           = models.IntegerField(default=0)
    rest                = models.IntegerField(default=0)
    emergency               = models.BooleanField(verbose_name='Commande urgente', default=False)
    paid               = models.BooleanField(verbose_name='Payé', default=False)
    ordonnance_return   = models.BooleanField(verbose_name='Ordonnance rendue', default=False)
    created             = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated             = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    def __str__(self):
        return str(self.client)
    @property
    def get_reste(self):
        return int(self.total) - int(self.versement)

    @property
    def get_not_paid(self):
        if self.versement == 0:
            return True 
        else:
            return False 
    @property
    def get_client_phone(self):
        return self.client.phone or "-"




class GlassDePres(models.Model):
    order      = models.ForeignKey(Order, verbose_name="de_pres_glasses", related_name='de_pres_glasses', on_delete=models.CASCADE)
    # vision  = models.CharField(verbose_name="vision", choices=PROGRESSIF_CHOICES, max_length=10 ,  blank=True, null=True)

    eye_choice  = models.CharField(verbose_name="OEUIL",choices=EYE_CHOICES, max_length=2)
    spheric_glass   = models.BooleanField(verbose_name='Verre Spherique', default=False)

    spher       = models.CharField(choices=SPHER_CHOICES, max_length=10, default="PLAN")
    cyl         = models.CharField(choices=CYL_CHOICES, max_length=10 ,  default= "+ 0.00")
    axe         = models.IntegerField(default=0)
    type_de_verre       =  models.ForeignKey(GlassType, verbose_name=" Type de verre", on_delete=models.CASCADE)

    note        = models.CharField( max_length=150, blank=True, null=True)

    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    @property
    def get_type_de_verre(self):
        return self.type_de_verre or "-"
class GlassDeLoin(models.Model):
    order        = models.ForeignKey(Order, related_name="de_loin_glasses", on_delete=models.CASCADE)
    eye_choice   = models.CharField(verbose_name="OEUIL",choices=EYE_CHOICES, max_length=2)
    spheric_glass   = models.BooleanField(verbose_name='Verre Spherique', default=False)

    spher        = models.CharField(choices=SPHER_CHOICES, max_length=10, default="PLAN")
    cyl          = models.CharField(choices=CYL_CHOICES, max_length=10 ,  default= "+ 0.00")
    axe          = models.IntegerField(default=0)
    type_de_verre= models.ForeignKey(GlassType, verbose_name=" Type de verre", on_delete=models.CASCADE)
    addition     = models.DecimalField(verbose_name="Addition",max_digits=10, decimal_places=2, blank=True, null=True)
    note         = models.CharField( max_length=150, blank=True, null=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    @property
    def get_type_de_verre(self):
        return self.type_de_verre or "-"

class ProgressifDeLoin(models.Model):
    order      = models.ForeignKey(Order, related_name="de_loin_progressifs", on_delete=models.CASCADE)
    # progressif  = models.CharField(choices=PROGRESSIF_CHOICES, max_length=10 ,  blank=True, null=True)
    eye_choice  = models.CharField(verbose_name="OEUIL",choices=EYE_CHOICES, max_length=2)
    spheric_glass   = models.BooleanField(verbose_name='Verre Spherique', default=False)

    spher       = models.CharField(choices=SPHER_CHOICES, max_length=10, default="PLAN")
    cyl         = models.CharField(choices=CYL_CHOICES, max_length=10 ,  default= "+ 0.00")
    axe         = models.IntegerField(default=0)
    type_de_verre = models.ForeignKey(GlassType, verbose_name=" Type de verre", on_delete=models.CASCADE)
    addition    = models.DecimalField(verbose_name="Addition",max_digits=10, decimal_places=2)
    date        = models.DateField(verbose_name='Date de Traitement',auto_now=False, auto_now_add=False, blank=True, null=True)
    note        = models.CharField( max_length=150, blank=True, null=True)
    created     = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated     = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    @property
    def get_type_de_verre(self):
        return self.type_de_verre or "-"
class ProgressifDePres(models.Model):
    order      = models.ForeignKey(Order, related_name="de_pres_progressifs", on_delete=models.CASCADE)
    # progressif  = models.CharField(choices=PROGRESSIF_CHOICES, max_length=10 ,  blank=True, null=True)
    eye_choice  = models.CharField(verbose_name="OEUIL",choices=EYE_CHOICES, max_length=2)
    spheric_glass   = models.BooleanField(verbose_name='Verre Spherique', default=False)

    spher       = models.CharField(choices=SPHER_CHOICES, max_length=10, default="PLAN")
    cyl         = models.CharField(choices=CYL_CHOICES, max_length=10 ,  default= "+ 0.00")
    axe         = models.IntegerField(default=0)
    type_de_verre =  models.ForeignKey(GlassType, verbose_name=" Type de verre", on_delete=models.CASCADE, blank=True, null=True)
    # date        = models.DateField(verbose_name='Date de Traitement',auto_now=False, auto_now_add=False, blank=True, null=True)
    note        = models.CharField( max_length=150, blank=True, null=True)
    created     = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated     = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    @property
    def get_type_de_verre(self):
        return self.type_de_verre or "-"



class Lentil(models.Model):
    order      = models.ForeignKey(Order, related_name="lentilles", on_delete=models.CASCADE)
    lentil_type = models.ForeignKey(LentilType, verbose_name="Type de lentille", on_delete=models.CASCADE)
    brand  = models.CharField(verbose_name="Marque", max_length=150)

    eye_choice  = models.CharField(verbose_name="OEUIL", choices=EYE_CHOICES, max_length=2)
    spheric_glass   = models.BooleanField(verbose_name='Lentille Spherique', default=False)

    spher       = models.CharField(choices=SPHER_CHOICES, max_length=10, default="PLAN")
    cyl         = models.CharField(choices=CYL_CHOICES, max_length=10 ,  default= "+ 0.00")
    rayon         = models.DecimalField(verbose_name="rayon",max_digits=10, decimal_places=2)
    diametre         = models.DecimalField(verbose_name="diametre",max_digits=10, decimal_places=2)
    axe         = models.IntegerField(default=0)
    note        = models.CharField( max_length=150, blank=True, null=True)

    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)



class PhotoClient(models.Model):
    order = models.ForeignKey(Order, related_name="photos", on_delete=models.CASCADE)
    fichier   = models.ImageField(upload_to='images/clients') 
    actif   = models.BooleanField(verbose_name='actif', default=True)


class Menture(models.Model):
    order      = models.ForeignKey(Order, verbose_name="Client", on_delete=models.CASCADE)
    matiere = models.CharField(verbose_name='Matiére',choices=MENTURE_CHOICES, max_length=15)
    name = models.CharField(verbose_name="Désignation",max_length=150, blank=True, null=True)
    price = models.DecimalField(verbose_name="Prix",max_digits=10, decimal_places=0)


