from django.db import models
from django.utils import timezone
from django import forms
import datetime

class NormalUser(models.Model):
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __unicode__(self):
        return self.user_id

    def is_existed(self):
        return self.user_id

    def _get_id(self):
        return self.user_id

    def _get_pw(self):
        return self.user_pw;

    def _set_pw(self, passwd):
        self.user_pw= hashlib.sha256(passwd.encode('utf-8')).hexdigest()

class Devices(models.Model):
    name = models.CharField(max_length=30, blank=True)
    serial_num = models.CharField(max_length=30, blank=True)
    ip_addr = models.CharField(max_length=30, blank=True)
    author = models.ForeignKey('auth.User')
    enable = models.BooleanField()

    def __str__(self):
        return  self.serial_num

    def _get_name(self):
        return self.name

    def _get_serial_num(self):
        return self.serial_num

    def _get_ip_addr(self):
        return self.ip_addr
    def _get_author(self):
        return self.author

    def _get_enable(self):
        return self.enable


class EditLog(models.Model):
    writer = models.CharField(max_length=20)
    serial = models.CharField(max_length=30)
    update_date = models.DateTimeField(
                default=timezone.now)

    def __str__(self):
        return self.writer


