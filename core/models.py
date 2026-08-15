from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        DRIVER = "DRIVER", "Driver"
        ADMIN = "ADMIN", "Admin"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER
    )

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="customer_profile"
    )
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Driver(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="driver_profile"
    )
    phone = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)
    current_location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Vehicle(models.Model):
    class VehicleType(models.TextChoices):
        BIKE = "BIKE", "Bike"
        VAN = "VAN", "Van"
        TRUCK = "TRUCK", "Truck"
        REFRIGERATED = "REFRIGERATED", "Refrigerated"

    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(
        max_length=20,
        choices=VehicleType.choices
    )
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.vehicle_number

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ASSIGNED = "ASSIGNED", "Assigned"
        PICKED_UP = "PICKED_UP", "Picked Up"
        IN_TRANSIT = "IN_TRANSIT", "In Transit"
        OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY", "Out for Delivery"
        DELIVERED = "DELIVERED", "Delivered"
        CANCELLED = "CANCELLED", "Cancelled"

    class Priority(models.TextChoices):
        NORMAL = "NORMAL", "Normal"
        HIGH = "HIGH", "High"
        URGENT = "URGENT", "Urgent"

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="orders"
    )

    item_description = models.CharField(max_length=255)
    weight = models.PositiveIntegerField()
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.NORMAL
    )

    destination = models.CharField(max_length=255)

    status = models.CharField(
        max_length=25,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        valid_transitions = {
            self.Status.PENDING: [self.Status.ASSIGNED, self.Status.CANCELLED],
            self.Status.ASSIGNED: [self.Status.PICKED_UP, self.Status.CANCELLED],
            self.Status.PICKED_UP: [self.Status.IN_TRANSIT],
            self.Status.IN_TRANSIT: [self.Status.OUT_FOR_DELIVERY],
            self.Status.OUT_FOR_DELIVERY: [self.Status.DELIVERED],
            self.Status.DELIVERED: [],
            self.Status.CANCELLED: [],
        }

        if self.pk:
            old_status = Order.objects.get(pk=self.pk).status

            if self.status != old_status:
                allowed = valid_transitions.get(old_status, [])

                if self.status not in allowed:
                    raise ValidationError(
                        f"Invalid status transition: "
                        f"{old_status} → {self.status}"
                    )
    def __str__(self):
        return f"Order #{self.id}"

class Assignment(models.Model):
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="assignment"
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.PROTECT,
        related_name="assignments"
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name="assignments"
    )

    assigned_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.driver.is_available:
            raise ValidationError("Driver is not available.")

        if not self.vehicle.is_available:
            raise ValidationError("Vehicle is not available.")
    def save(self, *args, **kwargs):
        self.order.status = Order.Status.ASSIGNED
        self.order.save(update_fields=["status"])

        super().save(*args, **kwargs)

        self.driver.is_available = False
        self.driver.save(update_fields=["is_available"])

        self.vehicle.is_available = False
        self.vehicle.save(update_fields=["is_available"])

    def __str__(self):
        return f"Assignment - Order #{self.order.id}"
