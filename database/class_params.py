from django.db import models
# taulua params vastaava luokka:
class Params(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=250, null=False)
    valid_from = models.DateField(null=False)
    valid_to = models.DateField(null=True)
    year = models.IntegerField(null=True)
    value = models.DecimalField(null=False) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id, self.name, self.description, self.valid_from, self.valid_to, self.year, self.value, self.created, self.updated)  


