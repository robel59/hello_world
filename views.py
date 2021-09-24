from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
import base64
from django.contrib.auth.decorators import login_required
from myuser.forms import *
from myuser.models import User as user
from decimal import Decimal
import string
import random
import requests
from datetime import date, timedelta
from datetime import datetime
from seal.models import *
from company.models import *
from django.db.models import Avg, Count, Min, Sum
from export.templatetags.mat import *


@login_required
def homestoreexport(request, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = company.objects.get(id = id)
            context['comp'] = ho
            return render(request, 'expoproduction/homestore.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)


@login_required
def client_provider_stor(request, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = company.objects.get(id = id)
            cl3 = client_3rd.objects.filter(company = ho)
            clexp = client_export.objects.filter(company = ho)
            prov = provider_mintu.objects.filter(company = ho)
            sto = export_store.objects.filter(company = ho)
            item = item_name.objects.filter(company = ho)
            context['comp'] = ho
            context['cl3'] = cl3
            context['clexp'] = clexp
            context['prov'] = prov
            context['sto'] = sto
            context['item'] = item
            return render(request, 'expoproduction/client_provider.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)

    if request.method == 'POST' :
        num = request.POST['num']
        name = request.POST['name']
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            ho = company.objects.get(id = id)
            if num == 'a':
                cl3 = client_3rd.objects.create(company = ho, name = name)
            elif num == 'b':
                clexp = client_export.objects.create(company = ho, name = name)
            elif num == 'c':
                prov = provider_mintu.objects.create(company = ho, name = name)
            elif num == 'd':
                sto = export_store.objects.create(company = ho, name = name)
            elif num == 'e':
                sto = item_name.objects.create(company = ho, name = name)
            return redirect('account:client_provider_stor', id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)


@login_required
def remove_client_provider_stor(request):
    if request.method == 'POST' :
        id = request.POST['coid']
        num = request.POST['num']
        rmid = request.POST['id']
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            if num == 'a':
                cl3 = client_3rd.objects.get(id = rmid)
                cl3.delete()
            elif num == 'b':
                cl3 = client_export.objects.get(id = rmid)
                cl3.delete()
            elif num == 'c':
                cl3 = provider_mintu.objects.get(id = rmid)
                cl3.delete()
            elif num == 'd':
                cl3 = export_store.objects..get(id = rmid)
                cl3.delete()
            elif num == 'e':
                cl3 = item_name.objects..get(id = rmid)
                cl3.delete()
            return redirect('account:client_provider_stor', id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)


@login_required
def recive_rowmat(request, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = company.objects.get(id = id)
            grnmintu= good_reciving_note.objects.all()
            grn3 = good_reciving_note3.objects.all()
            storex = export_store.objects.filter(company = ho)
            provmintu = provider_mintu.objects.filter(company = ho)
            cli3rd = client_3rd.objects.filter(company = ho)
            context['comp'] = ho
            context['grnmintu'] = grnmintu
            context['grn3'] = grn3
            context['storex'] = storex
            context['provmintu'] = provmintu
            context['cli3rd'] = cli3rd
            return render(request, 'expoproduction/good_reciving_home.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)


    if request.method == 'POST' :
        num = request.POST['num']
        name = request.POST['name']
        stoid = request.POST['stoid']
        pnum = request.POST['pnum']
        pnum1 = request.POST['pnum1']
        remark = request.POST['info']
        date = request.POST['date']
        clid = request.POST['clid']
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            ho = company.objects.get(id = id)
            idstor = idstore.objects.get(id = 1)
            ing = export_store.objects.get(id = stoid)
            if num == 'mintu':
                cl3 = provider_mintu.objects.get(id = clid)
                grn = good_reciving_note.object.create(name = name,
                company = ho,platnum = pnum,platnum2 = pnum1,
                export_store = ing,remark = remark,date = date,
                provider_mintu = cl3
                )
                grn.idnum = idstor.grn_mintu + grn.id
                grn.save()
                return redirect('account:grn_item_mintu', grn.id)

            elif num == '3rd':
                clexp = client_3rd.objects.get(id = clid)
                grn = good_reciving_note3.object.create(name = name,
                company = ho,platnum = pnum,platnum2 = pnum1,
                export_store = ing,remark = remark,date = date,
                client_3rd = clexp
                )
                return redirect('account:grn_item_3rd', id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)


@login_required
def grn_item_mintu(request, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = good_reciving_note.objects.get(id = id)
            context['item'] = item_mintu.objects.filter(good_reciving_note = ho)
            context['grn'] = ho
            context['item_stor'] = item_name.objects.all()
            return render(request, 'expoproduction/grn_item_mintu.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)

    if request.method == 'POST' :
        rmid = request.POST['id']
        qunt = request.POST['qunt']
        numbag = request.POST['numbag']
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            ho = good_reciving_note.objects.get(id = id)
            itemin = item_mintu.objects.get(id = rmid)
            reit = item_mintu(good_reciving_note = ho,item_name = itemin, quntity = qunt, bagqut = numbag, date = ho.date)
            reit.save()
            return redirect('account:grn_item_mintu', id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)

@login_required
def grn_item_3rd(request, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = good_reciving_note3.objects.get(id = id)
            context['item'] = item_3rd.objects.filter(good_reciving_note3 = ho)
            context['grn'] = ho
            context['item_stor'] = item_name.objects.all()
            return render(request, 'expoproduction/grn_item_3rd.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)

    if request.method == 'POST' :
        rmid = request.POST['id']
        qunt = request.POST['qunt']
        numbag = request.POST['numbag']
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            ho = good_reciving_note3.objects.get(id = id)
            itemin = item_mintu.objects.get(id = rmid)
            reit = item_3rd(good_reciving_note3 = ho,item_name = itemin, quntity = qunt, bagqut = numbag, date = ho.date)
            reit.save()
            return redirect('account:grn_item_3rd', id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)


@login_required
def print_grn_mintu(request, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = good_reciving_note.objects.get(id = id)
            context['grn'] = ho
            return render(request, 'expoproduction/print_grn_mintu.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)

    if request.method == 'POST' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            ho = good_reciving_note.objects.get(id = id)
            item = item_mintu.objects.filter(good_reciving_note = ho)
            for i in item:
                try:
                    op = bincard_row_mintu.objects.get(item_mintu = i, active = True)
                except bincard_row_mintu.DoesNotExist:
                    op = bincard_row_mintu(item_name = i.item_name, item_mintu = i, quntity = i.quntity)
                    op.save()

                    try:
                        op = row_balnce_mintu.objects.get(item_name = i.item_name)
                        op.quntity = op.quntity + i.quntity
                        op.save()
                    except row_balnce_mintu.DoesNotExist:
                        op = row_balnce_mintu(item_name = i.item_name, quntity = i.quntity)
                        op.save()
            ho.active = True
            ho.save()
            return redirect('account:grn_item_mintu', id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)

@login_required
def print_grn_3rd(request, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = good_reciving_note3.objects.get(id = id)
            context['grn'] = ho
            return render(request, 'expoproduction/print_grn_3rd.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)

    if request.method == 'POST' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            ho = good_reciving_note3.objects.get(id = id)

            item = item_3rd.objects.filter(good_reciving_note3 = ho)
            for i in item:
                try:
                    op = bincard_row_3rd.objects.get(item_3rd = i, active = True)
                except bincard_row_3rd.DoesNotExist:
                    op = bincard_row_3rd(item_name = i.item_name, item_3rd = i, quntity = i.quntity)
                    op.save()

                    try:
                        op = row_balnce_3rd.objects.get(item_3rd = i.item_3rd, client_3rd = ho.client_3rd)
                        op.quntity = op.quntity + i.quntity
                        op.save()
                    except row_balnce_3rd.DoesNotExist:
                        op = row_balnce_3rd(item_3rd = i.item_3rd,client_3rd = ho.client_3rd, quntity = i.quntity)
                        op.save()

            ho.active = True
            ho.save()
            return redirect('account:grn_item_mintu', id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)

#blance adding to store
#mintu export
@login_required
def correction_store(request, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = company.objects.get(id = id)
            cl3 = client_3rd.objects.filter(company = ho)
            item = item_name.objects.filter(company = ho)
            context['comp'] = ho
            context['cl3'] = cl3
            context['item'] = item
            return render(request, 'expoproduction/correct_stor_data.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)

    if request.method == 'POST' :
        num = request.POST['num']
        name = request.POST['name']
        itmid = request.POST['itmid']
        qunt = request.POST['qunt']
        bagqut = request.POST['bagqut']
        info = request.POST['info']
        date = request.POST['date']
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            ho = item_name.objects.get(id = itmid)
            if num == 'a':
                cl3 = item_mintu_correction.objects.create(item_name = ho, name = name, quntity = qunt, bagqut = bagqut, info = info, date = date)
            elif num == 'b':
                clid = request.POST['clid']
                bcf = client_3rd.objects.get(id = clid)
                cl3 = item_3rd_correction.objects.create(client_3rd = clid, item_name = ho, name = name, quntity = qunt, bagqut = bagqut, info = info, date = date)
            return redirect('account:correction_store', id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)

#production order start here
@login_required
def mahshin_reg(request, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = company.objects.get(id = id)
            context['item'] = expo_machine.objects.filter(company = ho)
            context['grn'] = ho
            return render(request, 'expoproduction/excpo_mlist.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)

    if request.method == 'POST' :
        num = request.POST['num']
        name = request.POST['name']
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            if num == 'a':
                ho = company.objects.get(id = id)
                reit = expo_machine(company = ho,name = name)
                reit.save()
            elif num == 'b':
                ho = expo_machine.objects.get(id = id)
                reit = expo_machine_function(expo_machine = ho,name = name)
                reit.save()

            return redirect('account:mahshin_reg', id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)

@login_required
def production_main(request, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = company.objects.get(id = id)
            context['promintu'] = production_order_mintu.objects.filter(company = ho)
            context['pro3'] = production_order_3rd.objects.filter(company = ho)
            context['grn'] = ho
            return render(request, 'expoproduction/excpo_mlist.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)

    if request.method == 'POST' :
        num = request.POST['num']
        name = request.POST['name']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        ite = request.POST['ite']
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            ho = item_name.objects.get(id = ite)
            if num == 'a':
                reit = production_order_mintu(item_name = ho,startt = sdate,endd = edate, worker = wor)
                reit.save()
                return redirect('account:production_dital', 'mintu', reit.id)
            elif num == 'b':
                reit = production_order_3rd(item_name = ho,startt = sdate,endd = edate, worker = wor)
                reit.save()

                return redirect('account:production_dital', '3rd', reit.id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)


@login_required
def production_dital(request,wh, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            if wh == 'mintu':
                ho = production_order_mintu.objects.get(id = id)
                context['grn'] = ho
                context['typ'] = 'mintu'
                return render(request, 'expoproduction/production_ditel.html', context)
            elif wh == '3rd':
                ho = production_order_3rd.objects.get(id = id)
                context['grn'] = ho
                context['typ'] = '3rd'
                return render(request, 'expoproduction/production_ditel.html', context)
        else:
            #not alloued
            return render(request, 'error.html', context)

    if request.method == 'POST' :
        num = request.POST['num']
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "admin":
                k = True
            elif i.worktype.name == "finace":
                k = True
            elif i.worktype.name == "storeexp":
                k = True
        if k:
            ho = item_name.objects.get(id = ite)
            if num == 'a':
                pass
            elif num == 'b':
                pass

            return redirect('account:production_dital', id)
        else:
            #you are not aloued to seal itemm
            return render(request, 'error.html', context)

# store views
@login_required
def storeview(request,id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            ho = company.objects.get(id = id)
            context['grn'] = ho
            context['cli3rd'] =  client_3rd.objects.filter(company = ho)
            context['item']  = item_name.object.filter(company = ho)
            #using this data we wil filter balnce for ecah client and mintu item on template sied
            return render(request, 'expoproduction/stor_main.html', context)#template not created
        else:
            #not alloued
            return render(request, 'error.html', context)

@login_required
def storeview_ditel_item(request,wh, id):
    if request.method == 'GET' :
        wor = worker.objects.get(user = request.user)
        context = {}
        jop = jobassgin.objects.filter(worker = wor)
        k = False
        for i in jop:
            if i.worktype.name == "storeexp":
                k = True
        if k and wor.active:
            if wh == 'mintu':
                ho = item_name.objects.get(id = id)
                typ = out_item_mintu.objects.filter(item_name = ho)
                uo = []
                for i in typ:
                    uo.append(i.expo_machine_function)
                context['grn'] = ho
                context['fistyp'] = uo
                context['row'] = bincard_row_mintu.objects.filter(item_name = ho)
                #using this data we wil filter balnce for ecah client and mintu item on template sied
                return render(request, 'expoproduction/stor_main_one.html', context)#template not created
            elif wh == '3rd':
                ho = client_3rd.objects.get(id = id)
                item = item_3rd_list.objects.filter(client_3rd = ho)
                kl = []
                for i in item:
                    kl.append(i.item_name)
                context['grn'] = ho
                context['item'] =  kl #using client information and item we can list all the info on template sied
                return render(request, 'expoproduction/stor_main_3rd_one.html', context)#template not created
        else:
            #not alloued
            return render(request, 'error.html', context)
