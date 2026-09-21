from django.db import models

class Customer(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    serial_number = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colour = models.CharField(max_length=50)
    year = models.IntegerField()
    car_for_sale = models.BooleanField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Salesperson(model.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Parts(models.Model):
    part_number = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.part_number} - {self.description}"
    
class Mechanic(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ServiceTicket(models.Model):
    service_ticket_number = models.CharField(max_length=50)
    date_received = models.DateField()
    comments = models.TextField()
    date_returned_to_customer = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Service Ticket {self.service_ticket_number}"
    
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.service_name} {self.hourly_rate}"
    
class PartsUsed(models.Model):
    number_used = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.number_used} × {self.part.part_number}"
    
class ServiceMechanic(models.Model):
    
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Mechanic {self.mechanic} on Service {self.service}"
    
class Invoice(models.Model):

    invoice_number = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return f"Invoice {self.invoice_number}"