# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Equipment(models.Model):

    #__Equipment_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    inventory_number = models.CharField(max_length=255, null=True, blank=True)
    pc_number = models.CharField(max_length=255, null=True, blank=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    qr_token = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    model = models.CharField(max_length=255, null=True, blank=True)
    specs = models.TextField(max_length=255, null=True, blank=True)
    commissioning_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)

    #__Equipment_FIELDS__END

    class Meta:
        verbose_name        = _("Equipment")
        verbose_name_plural = _("Equipment")


class Organization(models.Model):

    #__Organization_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Organization_FIELDS__END

    class Meta:
        verbose_name        = _("Organization")
        verbose_name_plural = _("Organization")


class Department(models.Model):

    #__Department_FIELDS__
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Department_FIELDS__END

    class Meta:
        verbose_name        = _("Department")
        verbose_name_plural = _("Department")


class Employee(models.Model):

    #__Employee_FIELDS__
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField()

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class Equipmenttype(models.Model):

    #__Equipmenttype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Equipmenttype_FIELDS__END

    class Meta:
        verbose_name        = _("Equipmenttype")
        verbose_name_plural = _("Equipmenttype")


class Equipmentevent(models.Model):

    #__Equipmentevent_FIELDS__
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    from_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    to_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    old_status = models.CharField(max_length=255, null=True, blank=True)
    new_status = models.CharField(max_length=255, null=True, blank=True)
    document_number = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(max_length=255, null=True, blank=True)

    #__Equipmentevent_FIELDS__END

    class Meta:
        verbose_name        = _("Equipmentevent")
        verbose_name_plural = _("Equipmentevent")



#__MODELS__END
