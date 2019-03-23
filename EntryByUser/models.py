from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class DataEntry(models.Model):
    EmpId = models.IntegerField(name="EmpId",unique=False)
    Name = models.CharField(max_length=100 ,help_text="Enter your name",unique=False,name="Name")
    Town = models.CharField(max_length=200,null=True,name="Town")
    Area = models.CharField(max_length=100,null=True,name="Area")
    TC   = models.IntegerField(default=0,name="TotalCalls")
    pc   =  models.IntegerField(default=0,name="PC")
    SecOrderValue = models.IntegerField(name="SecondaryOrderValue")
    SecCollection = models.IntegerField(name="SecondaryCollectionValue")
    CumSecSales = models.IntegerField(name="CumSecondarySales")
    CumSecCollection = models.IntegerField(name="CumSecondaryCollectionValue")
    GTOnly =  models.IntegerField(name="GTOnly")
    HACumPromoterStores =  models.IntegerField(name="HAPromoterStores")
    MTStores =  models.IntegerField(name="MTStores")
    CummCollection = models.IntegerField(name="CummCollection")
    NewStoresToday =  models.IntegerField(name="NewStoresToday")
    NewStoresComm =  models.IntegerField(name="NewStoresComm")
    date = models.DateField(null=False)
    remarks = models.TextField(max_length=4000,help_text="Fill Your Remarks",name="remarks")
    last_updated = models.DateTimeField(auto_now_add=True)



    def __repr__(self):
        return self.id #str(self.date) + ',' + str(self.Name) + ',' + str(self.Town.name) + ',' + str(self.Area) + ',' +str(self.TotalCalls) + ',' + str(self.PC) + ',' + str(self.SecondaryOrderValue)
        #+ ',' + str(self.SecondaryCollectionValue) +','+ str(self.CumSecondarySales) + ',' + str(self.CumSecondaryCollectionValue) + ',' + str(self.GTOnly) + ',' + str(self.HAPromoterStores) +', '+ str(self.MTStores) + ',' + str(self.CummCollection)
    #    + ',' + str(self.NewStoresToday) + ',' + str(self.NewStoresComm)



    def __str__(self):
        return str(self.EmpId)
