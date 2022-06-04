from django.db import models

# Create your models here.

Bank_Name = {
    ('ABSA','ABSA'),
    ('STANDARD_BANK','STANDARD_BANK'),
    ('CAPITEC','CAPITEC'),
    ('NEDBANK','NEDBANK'),
    ('FNB','FNB'),
    ('Investec','Investec'),
}
Branch_Number = {
    ('632005','632005'),
    ('51001','51001'),
    ('470010','470010'),
    ('198765','198765'),
    ('250655','250655'),
    ('580105','580105'),
}
Bank_type = {
    ('CURRENT','1'),
    ('SAVING','2'),
    ('TRANSACTION','3'),    
}
class Contract_Model(models.Model):
    Contract_ID = models.CharField(max_length=12, null=True, blank=True)
    Initials = models.CharField(max_length=4, null=True, blank=True)
    ID_Number = models.CharField(max_length=13, null=True, blank=True)
    Surname = models.CharField(max_length=50, null=True, blank=True)
    Premium = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    Name_of_Bank = models.CharField(max_length=20, null=True, blank=True, choices=Bank_Name)
    Name_of_Branch = models.CharField(max_length=20, null=True, blank=True, choices=Branch_Number)
    Name_of_Type = models.CharField(max_length=20, null=True, blank=True, choices=Bank_type)

    def __str__(self):
        return self.Contract_ID

