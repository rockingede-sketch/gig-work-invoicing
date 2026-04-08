from django.db import models
# taulua users vastaava luokka:
class Users(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=250, null=False)
    confirmed = models.BooleanField(default=False)
    valid_from = models.DateField(null=False)
    valid_to = models.DateField(null=True)
    disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id, 
                self.username, 
                self.password, 
                self.confirmed, 
                self.valid_from, 
                self.valid_to, 
                self.disabled, 
                self.created, 
                self.updated)


