from django.db import models
# taulua documents vastaava luokka:
class Documents(models.Model):
    DOC_TYPE_CHOICES = [
        ('tax card', 'Tax Card'),
        ('contract', 'Contract'),
        ('accepted contract', 'Accepted Contract'),
        ('invoice', 'Invoice'),
        ('payroll', 'Payroll'),
        ('other appendix', 'Other Appendix'),
    ]

    doc_type = models.CharField(max_length=20, choices=DOC_TYPE_CHOICES, null=False)
    doc_date = models.DateField(null=False)
    # Foreign Keys: 
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    contract_id = models.ForeignKey('Contract', on_delete=models.SET_NULL, null=True, blank=True)
    invoice_id = models.ForeignKey('Invoice', on_delete=models.SET_NULL, null=True, blank=True)
    payroll_id = models.ForeignKey('Payroll', on_delete=models.SET_NULL, null=True, blank=True)
    docname = models.CharField(max_length=250, null=False)
    filepath = models.CharField(max_length=250, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id, 
                self.doc_type, 
                self.doc_date, 
                self.user_id, 
                self.contract_id, 
                self.invoice_id, 
                self.payroll_id, 
                self.docname, 
                self.filepath, 
                self.created, 
                self.updated)  


