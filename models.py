from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from myuser.models import User as user
from company.models import *
from worker.models import *


#information storing part
class export_store(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    company = models.ForeignKey(company, on_delete=models.CASCADE, null = True)
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#list of export stor
class idstore(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    grn_mintu = models.IntegerField(_('id number'),default=0)
    grn_3rd = models.IntegerField(_('id number'),default=0)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class client_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    company = models.ForeignKey(company, on_delete=models.CASCADE, null = True)
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class client_export(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    company = models.ForeignKey(company, on_delete=models.CASCADE, null = True)
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class provider_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    company = models.ForeignKey(company, on_delete=models.CASCADE, null = True)
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#mintu item reciving preform for mintu
class good_reciving_note(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    idnum = models.IntegerField(_('id number'),default=0)
    company = models.ForeignKey(company, on_delete=models.CASCADE, default='')
    export_store = models.ForeignKey(export_store, on_delete=models.CASCADE, default='')
    provider_mintu = models.ForeignKey(provider_mintu, on_delete=models.CASCADE, default='')
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)#provider
    platnum = models.CharField(_('Name'), default='', unique=False, max_length=100)#provider
    pleatnum2 = models.CharField(_('Name'), default='', unique=False, max_length=100)#provider
    remark = models.TextField(_('Info'), default='', null=True)
    date = models.DateField(_('Register Day'),null = True)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    rday = models.DateField(_('Register Day'), auto_now_add=True)
    activ = models.BooleanField(_('activ'), default=False)

    def __str__(self):
        return self.name

#mintu list of item
class item_name(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    company = models.ForeignKey(company, on_delete=models.CASCADE, null = True)
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#mintu list of item
class item_3rd_list(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    client_3rd = models.ForeignKey(client_3rd, on_delete=models.CASCADE, default='')
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class item_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    good_reciving_note = models.ForeignKey(good_reciving_note, on_delete=models.CASCADE, null = True)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    unit = models.ForeignKey(unit, on_delete=models.CASCADE, default='')
    bagqut = models.CharField(_('BAg Qut'), default='', unique=False, max_length=100)
    date = models.DateField(_('Register Day'),null = True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class item_mintu_correction(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)#provider
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    unit = models.ForeignKey(unit, on_delete=models.CASCADE, default='')
    bagqut = models.CharField(_('BAg Qut'), default='', unique=False, max_length=100)
    info = models.TextField(_('Info'), default='', null=True)
    date = models.DateField(_('Register Day'),null = True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)


class item_3rd_correction(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    client_3rd = models.ForeignKey(client_3rd, on_delete=models.CASCADE, default='')
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)#provider
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    unit = models.ForeignKey(unit, on_delete=models.CASCADE, default='')
    bagqut = models.CharField(_('BAg Qut'), default='', unique=False, max_length=100)
    info = models.TextField(_('Info'), default='', null=True)
    date = models.DateField(_('Register Day'),null = True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)


class good_reciving_note3(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    idnum = models.IntegerField(_('id number'),default=0)
    company = models.ForeignKey(company, on_delete=models.CASCADE, default='')
    export_store = models.ForeignKey(export_store, on_delete=models.CASCADE, default='')
    client_3rd = models.ForeignKey(client_3rd, on_delete=models.CASCADE, default='')
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)#provider
    platnum = models.CharField(_('Name'), default='', unique=False, max_length=100)#provider
    pleatnum2 = models.CharField(_('Name'), default='', unique=False, max_length=100)#provider
    info = models.TextField(_('Info'), default='', null=True)
    remark = models.TextField(_('Info'), default='', null=True)
    date = models.DateField(_('Register Day'),null = True)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    rday = models.DateField(_('Register Day'), auto_now_add=True)
    activ = models.BooleanField(_('activ'), default=False)

    def __str__(self):
        return self.name
#recived item from 3rd parety
class item_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    good_reciving_note = models.ForeignKey(good_reciving_note, on_delete=models.CASCADE, null = True)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    unit = models.ForeignKey(unit, on_delete=models.CASCADE, default='')
    bagqut = models.CharField(_('BAg Qut'), default='', unique=False, max_length=100)
    date = models.DateField(_('Register Day'),null = True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)
#---------------------------------------------------------- recive end -------------------------------------------------------------------------
#----------------------------------------------------------- production biggen -----------------------------------------------------------------
class expo_machine(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    company = models.ForeignKey(company, on_delete=models.CASCADE, null = True)
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class expo_machine_function(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    expo_machine = models.ForeignKey(expo_machine, on_delete=models.CASCADE, null = True)
    name = models.CharField(_('Application Name'), default='', unique=False, max_length=100)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class production_order_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    expo_machine_function = models.ManyToManyField(expo_machine_function)
    startt = models.DateTimeField(_('Starting Time'),)
    endd = models.DateTimeField(_('Ending time'),)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#recored how the packaginf is
class out_item_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    production_order_mintu = models.ForeignKey(production_order_mintu, on_delete=models.CASCADE, null = True)
    expo_machine_function = models.ForeignKey(expo_machine_function, on_delete=models.CASCADE, null = True)
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)
    info = models.TextField(_('Info'), default='', null=True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class rowmaterial_issue_voucher(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    idnum = models.IntegerField(_('id number'),default=0)
    production_order_mintu = models.ForeignKey(production_order_mintu, on_delete=models.CASCADE, null = True)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    date = models.DateField(_('Register Day'),null = True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)


class issue_item(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    rowmaterial_issue_voucher = models.ForeignKey(rowmaterial_issue_voucher, on_delete=models.CASCADE, null = True)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class production_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    production_order_mintu = models.ForeignKey(production_order_mintu, on_delete=models.CASCADE, null = True)
    startt = models.DateTimeField(_('Starting Time'), null=True)
    endd = models.DateTimeField(_('Ending time'), null=True)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#????????????????????????????????/ 3rd party production ???????????????????????????????????/////
class production_order_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    client_3rd = models.ForeignKey(client_3rd, on_delete=models.CASCADE, null = True)
    expo_machine_function = models.ManyToManyField(expo_machine_function)
    startt = models.DateTimeField(_('Starting Time'),)
    endd = models.DateTimeField(_('Ending time'),)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#recored how the packaginf is
class out_item_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    production_order_3rd = models.ForeignKey(production_order_3rd, on_delete=models.CASCADE, null = True)
    expo_machine_function = models.ForeignKey(expo_machine_function, on_delete=models.CASCADE, null = True)
    name = models.CharField(_('Name'), default='', unique=False, max_length=100)
    info = models.TextField(_('Info'), default='', null=True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class rowmaterial_issue_voucher_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    idnum = models.IntegerField(_('id number'),default=0)
    production_order_3rd = models.ForeignKey(production_order_3rd, on_delete=models.CASCADE, null = True)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    date = models.DateField(_('Register Day'),null = True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class issue_item_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    rowmaterial_issue_voucher_3rd = models.ForeignKey(rowmaterial_issue_voucher_3rd, on_delete=models.CASCADE, null = True)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class production_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    production_order_3rd = models.ForeignKey(production_order_3rd, on_delete=models.CASCADE, null = True)
    startt = models.DateTimeField(_('Starting Time'), null=True)
    endd = models.DateTimeField(_('Ending time'), null=True)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    rday = models.DateField(_('Register Day'), auto_now_add=True)
#????????????????????????????????????????????????????????????????????????????????????????????????//


class F_G_R_V_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    idnum = models.IntegerField(_('id number'),default=0)
    production_mintu = models.ForeignKey(production_mintu, on_delete=models.CASCADE, null = True)
    date = models.DateField(_('Ending time'), null=True)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class finshed_item_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    out_item_mintu = models.ForeignKey(out_item_mintu, on_delete=models.CASCADE, null = True)
    expo_machine_function = models.ForeignKey(expo_machine_function, on_delete=models.CASCADE, null = True)
    F_G_R_V_mintu = models.ForeignKey(F_G_R_V_mintu, on_delete=models.CASCADE, null = True)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class F_G_R_V_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    idnum = models.IntegerField(_('id number'),default=0)
    production_mintu = models.ForeignKey(production_mintu, on_delete=models.CASCADE, null = True)
    date = models.DateField(_('Ending time'), null=True)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class finshed_item_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    out_item_3rd = models.ForeignKey(out_item_3rd, on_delete=models.CASCADE, null = True)
    expo_machine_function = models.ForeignKey(expo_machine_function, on_delete=models.CASCADE, null = True)
    F_G_R_V_3rd = models.ForeignKey(F_G_R_V_3rd, on_delete=models.CASCADE, null = True)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#-------------------------------------------------- production end here ---------------------------------------------------------------------------
#----------------------------------------------------- stor out record----------------------------------------------------------
class export_delivery_note_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    idnum = models.IntegerField(_('id number'),default=0)
    client_export = models.ForeignKey(client_export, on_delete=models.CASCADE, null = True)
    date = models.DateField(_('Ending time'), null=True)
    vehicle_no = models.CharField(_('vehicle number'), default='', unique=False, max_length=100,null = True)
    transporter_no = models.CharField(_('Transporter nuber'), default='', unique=False, max_length=100,null = True)
    tin_no = models.CharField(_('TIN number'), default='', unique=False, max_length=100,null = True)
    fs_no = models.CharField(_('FS number'), default='', unique=False, max_length=100,null = True)
    order_no = models.CharField(_('Order number'), default='', unique=False, max_length=100,null = True)
    stor_no = models.CharField(_('Stor number'), default='', unique=False, max_length=100,null = True)
    info = models.TextField(_('Info'), default='', null=True)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class expo_delivery_item(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    export_delivery_note_mintu = models.ForeignKey(export_delivery_note_mintu, on_delete=models.CASCADE, null = True)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class stor_issue_voucher_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    idnum = models.IntegerField(_('id number'),default=0)
    client_3rd = models.ForeignKey(client_3rd, on_delete=models.CASCADE, null = True)
    date = models.DateField(_('Ending time'), null=True)
    vehicle_no = models.CharField(_('vehicle number'), default='', unique=False, max_length=100,null = True)
    transporter_no = models.CharField(_('Transporter nuber'), default='', unique=False, max_length=100,null = True)
    tin_no = models.CharField(_('TIN number'), default='', unique=False, max_length=100,null = True)
    fs_no = models.CharField(_('FS number'), default='', unique=False, max_length=100,null = True)
    order_no = models.CharField(_('Order number'), default='', unique=False, max_length=100,null = True)
    stor_no = models.CharField(_('Stor number'), default='', unique=False, max_length=100,null = True)
    info = models.TextField(_('Info'), default='', null=True)
    worker = models.ForeignKey(worker, on_delete=models.CASCADE, default='')
    rday = models.DateField(_('Register Day'), auto_now_add=True)

class stor_issue_item_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    stor_issue_voucher_3rd = models.ForeignKey(stor_issue_voucher_3rd, on_delete=models.CASCADE, null = True)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#----------------------------------------final product ---------------------------------------------------
#balnce recording filed for all the item_mintu
class row_balnce_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal filal product'), decimal_places=2, max_digits=50, default=0)

class row_balnce_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    client_3rd = models.ForeignKey(client_3rd, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal filal product'), decimal_places=2, max_digits=50, default=0)

class pro_balnce_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    expo_machine_function = models.ForeignKey(expo_machine_function, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal filal product'), decimal_places=2, max_digits=50, default=0)

class pro_balnce_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    client_3rd = models.ForeignKey(client_3rd, on_delete=models.CASCADE, null = True)
    expo_machine_function = models.ForeignKey(expo_machine_function, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal filal product'), decimal_places=2, max_digits=50, default=0)
#mintu final product bin card
class bincard_prow_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    out_item_mintu = models.ForeignKey(out_item_mintu, on_delete=models.CASCADE, null = True)
    expo_machine_function = models.ForeignKey(expo_machine_function, on_delete=models.CASCADE, null = True)
    finshed_item_mintu = models.ForeignKey(finshed_item_mintu, on_delete=models.CASCADE, null = True)
    expo_delivery_item = models.ForeignKey(expo_delivery_item, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal filal product'), decimal_places=2, max_digits=50, default=0)
    in_out = models.BooleanField(_('In(T)/out(F)'), default=True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#3rd party final product materail
class bincard_prow_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    out_item_3rd = models.ForeignKey(out_item_3rd, on_delete=models.CASCADE, null = True)
    expo_machine_function = models.ForeignKey(expo_machine_function, on_delete=models.CASCADE, null = True)
    client_3rd = models.ForeignKey(client_3rd, on_delete=models.CASCADE, null = True)
    finshed_item_3rd = models.ForeignKey(finshed_item_3rd, on_delete=models.CASCADE, null = True)
    stor_issue_item_3rd = models.ForeignKey(stor_issue_item_3rd, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal filal product'), decimal_places=2, max_digits=50, default=0)
    in_out = models.BooleanField(_('In(T)/out(F)'), default=True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#--------------------------------------------- row materal -----------------------------------------------------
#mintu row materail bin card
class bincard_row_mintu(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    item_mintu = models.ForeignKey(item_mintu, on_delete=models.CASCADE, null = True)
    issue_item = models.ForeignKey(issue_item, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    in_out = models.BooleanField(_('In(T)/out(F)'), default=True)
    active = models.BooleanField(_('active'), default=True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)

#3rd party row materail
class bincard_row_3rd(models.Model):

    id = models.AutoField(_('Id'), primary_key=True, unique=True, max_length=100)
    item_name = models.ForeignKey(item_name, on_delete=models.CASCADE, null = True)
    client_3rd = models.ForeignKey(client_3rd, on_delete=models.CASCADE, null = True)
    item_3rd = models.ForeignKey(item_3rd, on_delete=models.CASCADE, null = True)
    issue_item_3rd = models.ForeignKey(issue_item_3rd, on_delete=models.CASCADE, null = True)
    quntity = models.DecimalField(_('Totoal row material R'), decimal_places=2, max_digits=50, default=0)
    in_out = models.BooleanField(_('In(T)/out(F)'), default=True)
    active = models.BooleanField(_('active'), default=True)
    rday = models.DateField(_('Register Day'), auto_now_add=True)
