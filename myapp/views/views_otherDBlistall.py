# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:00:35 2023

@author: PCUSER
"""


from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.conf import settings
#from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from module import func0
from module import func
from module import func2
from module import func2x
from module import func2t
from module import func3
from module import func3x
from module import func4
from module import func4x
from module import func5
from module import func5x2
from module import func6
from module import func7
from module import func8, func_usbond
##################函式位置改寫，一個函式一個檔案，棄用func
from module_PERseg import Price5yDB, Price5y, PERseg, PERsegPEG, PERsegPEGxDB, PERsegStable, PERsegx, PERsegxDB, NetCapDB, PERseg3
from module_Kn import KnQuery, Kn8yPrice

#################
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

from myapp.models import Stock6Sign
from myapp.models import StockPERseg

from myapp.models import DCStock6Sign202011
from myapp.models import DCStock6Sign2020Q4
from myapp.models import DCStock6Sign202101
from myapp.models import DCStock6Sign202102
from myapp.models import DCStock6Sign202103
from myapp.models import DCStock6Sign202104
from myapp.models import DCStock6Sign202105
from myapp.models import DCStock6Sign202106
from myapp.models import DCStock6Sign202107
from myapp.models import DCStock6Sign202108
from myapp.models import DCStock6Sign202109
from myapp.models import DCStock6Sign202110
from myapp.models import DCStock6Sign202111
from myapp.models import DCStock6Sign202112


from myapp.models import Stock6Sign202005
from myapp.models import Stock6Sign202006

from myapp.models import Stock6Sign2020Q2
from myapp.models import Stock6Sign202008
from myapp.models import Stock6Sign202009
from myapp.models import Stock6Sign2020Q3
from myapp.models import Stock6Sign202011
from myapp.models import Stock6Sign2020Q4
from myapp.models import Stock6Sign202101
from myapp.models import Stock6Sign202102
from myapp.models import Stock6Sign202103
from myapp.models import Stock6Sign202104
from myapp.models import Stock6Sign202105
from myapp.models import Stock6Sign202106
from myapp.models import Stock6Sign202107
from myapp.models import Stock6Sign202108
from myapp.models import Stock6Sign202109
from myapp.models import Stock6Sign202110
from myapp.models import Stock6Sign202111
from myapp.models import Stock6Sign202112
from myapp.models import Stock6Sign202201
from myapp.models import Stock6Sign202202
from myapp.models import Stock6Sign202203
from myapp.models import Stock6Sign202204
from myapp.models import Stock6Sign202205
from myapp.models import Stock6Sign202206
from myapp.models import Stock6Sign202207
from myapp.models import Stock6Sign202208
from myapp.models import Stock6Sign202209
from myapp.models import Stock6Sign202210
from myapp.models import Stock6Sign202211
from myapp.models import Stock6Sign202212

from myapp.models import Stock6Sign202301
from myapp.models import Stock6Sign202302
from myapp.models import Stock6Sign202303
from myapp.models import Stock6Sign202304
from myapp.models import Stock6Sign202305
from myapp.models import Stock6Sign202306
from myapp.models import Stock6Sign202307
from myapp.models import Stock6Sign202308
from myapp.models import Stock6Sign202309
from myapp.models import Stock6Sign202310
from myapp.models import Stock6Sign202311
from myapp.models import Stock6Sign202312

#from myapp.models import Stock6sta2021
#from myapp.models import Stock6Sign202109
#from myapp.models import Stock6Sign202110
#from myapp.models import Stock6Sign202111
#from myapp.models import Stock6Sign202112



from myapp.models import StockPERseg202005
from myapp.models import StockPERseg202006
from myapp.models import StockPERseg2020Q2
from myapp.models import StockPERseg202008
from myapp.models import StockPERseg202009
from myapp.models import StockPERseg2020Q3
from myapp.models import StockPERseg202011
from myapp.models import StockPERseg2020Q4
from myapp.models import StockPERseg202101
from myapp.models import StockPERseg202102
from myapp.models import StockPERseg202103
from myapp.models import StockPERseg202104
from myapp.models import StockPERseg202105
from myapp.models import StockPERseg202106
from myapp.models import StockPERseg202107
from myapp.models import StockPERseg202108
from myapp.models import StockPERseg202109
from myapp.models import StockPERseg202110
from myapp.models import StockPERseg202111
from myapp.models import StockPERseg202112
from myapp.models import StockPERseg202201
from myapp.models import StockPERseg202202
from myapp.models import StockPERseg202203
from myapp.models import StockPERseg202204
from myapp.models import StockPERseg202205
from myapp.models import StockPERseg202206
from myapp.models import StockPERseg202207
from myapp.models import StockPERseg202208
from myapp.models import StockPERseg202209
from myapp.models import StockPERseg202210
from myapp.models import StockPERseg202211
from myapp.models import StockPERseg202212

from myapp.models import StockPERseg202301
from myapp.models import StockPERseg202302
from myapp.models import StockPERseg202303
from myapp.models import StockPERseg202304
from myapp.models import StockPERseg202305
from myapp.models import StockPERseg202306
from myapp.models import StockPERseg202307
from myapp.models import StockPERseg202308
from myapp.models import StockPERseg202309
from myapp.models import StockPERseg202310
from myapp.models import StockPERseg202311
from myapp.models import StockPERseg202312



from myapp.models import EpsProfit2020Q1
from myapp.models import EpsProfit2020Q2
from myapp.models import EpsProfit2020Q3
from myapp.models import EpsProfit2020Q4
from myapp.models import EpsProfit2021Q1
from myapp.models import EpsProfit2021Q2
from myapp.models import EpsProfit2021Q3
from myapp.models import EpsProfit2021Q4
from myapp.models import EpsProfit2022Q1
from myapp.models import EpsProfit2022Q3
from myapp.models import EpsProfit2023Q1
from myapp.models import EpsProfit2023Q2
from myapp.models import EpsProfit2023Q3

from myapp.models import StockPERsegStable2020
from myapp.models import StockPERsegStable2020Q2
from myapp.models import StockPERsegStable2020Q3
from myapp.models import StockPERsegStable2020Q3x
from myapp.models import StockPERsegStable2020Q4
from myapp.models import StockPERsegStable2021Q1
from myapp.models import StockPERsegStable2021Q2
from myapp.models import StockPERsegStable2021Q3
from myapp.models import StockPERsegStable2021Q4
from myapp.models import StockPERsegStable2022Q1
from myapp.models import StockPERsegStable2022Q3
from myapp.models import StockPERsegStable2023Q1
from myapp.models import StockPERsegStable2023Q2
from myapp.models import StockPERsegStable2023Q3

from myapp.models import EPSachieve
from myapp.models import EPSachieve2020Q2
from myapp.models import EPSachieve2020Q3
from myapp.models import EPSachieve2021Q1
from myapp.models import EPSachieve2021Q2
from myapp.models import EPSachieve2021Q3
from myapp.models import EPSachieve2022Q1
from myapp.models import EPSachieve2022Q3
from myapp.models import EPSachieve2023Q1
from myapp.models import EPSachieve2023Q2
from myapp.models import EPSachieve2023Q3

from myapp.models import StockCapVar
from myapp.models import StockCapVar2020Q2
from myapp.models import StockCapVar2020Q3
from myapp.models import StockCapVar2020Q4
from myapp.models import StockCapVar2021Q1
from myapp.models import StockCapVar2021Q2
from myapp.models import StockCapVar2021Q3
from myapp.models import StockCapVar2021Q4
from myapp.models import StockCapVar2022Q1
from myapp.models import StockCapVar2022Q3
from myapp.models import StockCapVar2023Q1
from myapp.models import StockCapVar2023Q2
from myapp.models import StockCapVar2023Q3



from myapp.models import StockFavs_test168
from myapp.models import StockFavDB

from myapp.models import PriEPSPER_DB

#from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse

from myapp.models import City

###########################EPS達成率區##################################################
@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2020Q2listall(request):
    alleps = EPSachieve2020Q2.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2020Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2020Q3listall(request):
    alleps = EPSachieve2020Q3.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2020Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2021Q1listall(request):
    alleps = EPSachieve2021Q1.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2021Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2021Q2listall(request):
    alleps = EPSachieve2021Q2.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2021Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2021Q3listall(request):
    alleps = EPSachieve2021Q3.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2021Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2022Q1listall(request):
    alleps = EPSachieve2022Q1.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2022Q1listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2022Q3listall(request):
    alleps = EPSachieve2022Q3.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2022Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2023Q1listall(request):
    alleps = EPSachieve2023Q1.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2023Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2023Q2listall(request):
    alleps = EPSachieve2023Q2.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2023Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2023Q3listall(request):
    alleps = EPSachieve2023Q3.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2023Q3listall.html", locals())
########################股本變動率############################################################




@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2020Q2listall(request):
    caps = StockCapVar2020Q2.objects.all().order_by('id')
    return render(request, "StockCapVar2020Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2020Q3listall(request):
    caps = StockCapVar2020Q3.objects.all().order_by('id')
    return render(request, "StockCapVar2020Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2020Q4listall(request):
    caps = StockCapVar2020Q4.objects.all().order_by('id')
    return render(request, "StockCapVar2020Q4listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2021Q1listall(request):
    caps = StockCapVar2021Q1.objects.all().order_by('id')
    return render(request, "StockCapVar2021Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2021Q2listall(request):
    caps = StockCapVar2021Q2.objects.all().order_by('id')
    return render(request, "StockCapVar2021Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2021Q3listall(request):
    caps = StockCapVar2021Q3.objects.all().order_by('id')
    return render(request, "StockCapVar2021Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2021Q4listall(request):
    caps = StockCapVar2021Q4.objects.all().order_by('id')
    return render(request, "StockCapVar2021Q4listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2022Q1listall(request):
    caps = StockCapVar2022Q1.objects.all().order_by('id')
    return render(request, "StockCapVar2022Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2022Q3listall(request):
    caps = StockCapVar2022Q3.objects.all().order_by('id')
    return render(request, "StockCapVar2022Q3listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2022Q4listall(request):
    caps = StockCapVar2022Q3.objects.all().order_by('id')
    return render(request, "StockCapVar2022Q4listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2023Q1listall(request):
    caps = StockCapVar2023Q1.objects.all().order_by('id')
    return render(request, "StockCapVar2023Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2023Q2listall(request):
    caps = StockCapVar2023Q2.objects.all().order_by('id')
    return render(request, "StockCapVar2023Q2listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2023Q3listall(request):
    caps = StockCapVar2023Q3.objects.all().order_by('id')
    return render(request, "StockCapVar2023Q3listall.html", locals())
#######################EPS和營益率創八季新高###############################################



@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfitlistall2020Q1(request):
    allepsprof = EpsProfit2020Q1.objects.all().order_by('id')
    return render(request, "EPSnProfitlistall2020Q1.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2020Q2listall(request):
    allepsprof = EpsProfit2020Q2.objects.all().order_by('id')
    return render(request, "EPSnProfit2020Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2020Q3listall(request):
    allepsprof = EpsProfit2020Q3.objects.all().order_by('id')
    return render(request, "EPSnProfit2020Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2020Q4listall(request):
    allepsprof = EpsProfit2020Q4.objects.all().order_by('id')
    return render(request, "EPSnProfit2020Q4listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2021Q1listall(request):
    allepsprof = EpsProfit2021Q1.objects.all().order_by('id')
    return render(request, "EPSnProfit2021Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2021Q2listall(request):
    allepsprof = EpsProfit2021Q2.objects.all().order_by('id')
    return render(request, "EPSnProfit2021Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2021Q3listall(request):
    allepsprof = EpsProfit2021Q3.objects.all().order_by('id')
    return render(request, "EPSnProfit2021Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2021Q4listall(request):
    allepsprof = EpsProfit2021Q4.objects.all().order_by('id')
    return render(request, "EPSnProfit2021Q4listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2022Q1listall(request):
    allepsprof = EpsProfit2022Q1.objects.all().order_by('id')
    return render(request, "EPSnProfit2022Q1listall.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def EPSnProfit2022Q3listall(request):
    allepsprof = EpsProfit2022Q3.objects.all().order_by('id')
    return render(request, "EPSnProfit2022Q3listall.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def EPSnProfit2022Q4listall(request):
    allepsprof = EpsProfit2022Q4.objects.all().order_by('id')
    return render(request, "EPSnProfit2022Q4listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2023Q1listall(request):
    allepsprof = EpsProfit2023Q1.objects.all().order_by('id')
    return render(request, "EPSnProfit2023Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2023Q2listall(request):
    allepsprof = EpsProfit2023Q2.objects.all().order_by('id')
    return render(request, "EPSnProfit2023Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2023Q3listall(request):
    allepsprof = EpsProfit2023Q3.objects.all().order_by('id')
    return render(request, "EPSnProfit2023Q3listall.html", locals())
##############################################################

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2020(request):
    stas = StockPERsegStable2020.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2020.html", locals())



@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2020Q2(request):
    stas = StockPERsegStable2020Q2.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2020Q2.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2020Q3(request):
    stas = StockPERsegStable2020Q3.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2020Q3.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2020Q4(request):
    stas = StockPERsegStable2020Q4.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2020Q4.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2021Q1(request):
    stas = StockPERsegStable2021Q1.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2021Q1.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2021Q2(request):
    stas = StockPERsegStable2021Q2.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2021Q2.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2021Q3(request):
    stas = StockPERsegStable2021Q3.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2021Q3.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2021Q4(request):
    stas = StockPERsegStable2021Q4.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2021Q4.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2022Q1(request):
    stas = StockPERsegStable2022Q1.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2022Q1.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2022Q3(request):
    stas = StockPERsegStable2022Q3.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2022Q3.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2022Q4(request):
    stas = StockPERsegStable2022Q4.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2022Q4.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2023Q1(request):
    stas = StockPERsegStable2023Q1.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2023Q1.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2023Q2(request):
    stas = StockPERsegStable2023Q2.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2023Q2.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2023Q3(request):
    stas = StockPERsegStable2023Q3.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2023Q3.html", locals())



'''

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2020Q2(request):
    stas = StockPERsegStable2020Q2.objects.all().order_by('cStockID')
    return render(request, "StockPERsegStable2020Q2.html", locals())
'''
######################################################################




##################################範例
@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202009test(request):
    
    tse1 = ['2330','3034']
    signs = Stock6Sign202009.objects.filter(cStockID__in = tse1).order_by('cStockID')
    return render(request, "stock6listall202009test.html", locals())

################################################################






#子產業趨勢平均總表
@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202011(request):
    subs = SubCats202011.objects.all().order_by('id')
    return render(request, "SubCatslistall202011.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202102(request):
    subs = SubCats202102.objects.all().order_by('id')
    return render(request, "SubCatslistall202102.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202103(request):
    subs = SubCats202103.objects.all().order_by('id')
    return render(request, "SubCatslistall202103.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202104(request):
    subs = SubCats202104.objects.all().order_by('id')
    return render(request, "SubCatslistall202104.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202105(request):
    subs = SubCats202105.objects.all().order_by('id')
    return render(request, "SubCatslistall202105.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202106(request):
    subs = SubCats202106.objects.all().order_by('id')
    return render(request, "SubCatslistall202106.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202107(request):
    subs = SubCats202107.objects.all().order_by('id')
    return render(request, "SubCatslistall202107.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202108(request):
    subs = SubCats202108.objects.all().order_by('id')
    return render(request, "SubCatslistall202108.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202109(request):
    subs = SubCats202109.objects.all().order_by('id')
    return render(request, "SubCatslistall202109.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202110(request):
    subs = SubCats202110.objects.all().order_by('id')
    return render(request, "SubCatslistall202110.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202111(request):
    subs = SubCats202111.objects.all().order_by('id')
    return render(request, "SubCatslistall202111.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202112(request):
    subs = SubCats202112.objects.all().order_by('id')
    return render(request, "SubCatslistall202112.html", locals())
###################################################














    #url_pool = ['http://dj.mybank.com.tw','http://jdata.yuanta.com.tw','http://jsjustweb.jihsun.com.tw','http://stockchannel.sinotrade.com.tw','http://www.emega.com.tw','http://djfubonholdingfund.fbs.com.tw','http://stocks.ftsi.com.tw','http://www.esunsec.com.tw','http://tcfhcsec.moneydj.com','http://kgieworld.moneydj.com','http://pscnetinvest.moneydj.com','http://web.tcsc.com.tw','http://just.honsec.com.tw','http://ycsc.moneydj.com','http://easyfun.concords.com.tw','http://just2.entrust.com.tw','http://newjust.masterlink.com.tw','http://jsinfo.wls.com.tw','http://stock.capital.com.tw']

    #url_chosen = random.choice(url_pool)
#######################################################################################################

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202011(request):

    
    signs = DCStock6Sign202011.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202011.html", locals())



@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall2020Q4(request):

    
    signs = DCStock6Sign2020Q4.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall2020Q4.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202101(request):

    
    signs = DCStock6Sign202101.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202101.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202102(request):
    '''    
    TSEAll = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958']
    OTCAll = ['1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']
    Allcompany = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958','1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']

    threeCategLength = 0
    twoCategLength = 0
    oneCategLength = 0
    zeroCategLength = 0
    
    gainCategLength = 0
    lossCategLength = 0 
    tieCategLength = 0 

    for c in Allcompany:
        try:
            sign = models.Stock6Sign202011.objects.get(cStockID = c)
            if (float(sign.cAverageScore) >= 3):
                threeCategLength += 1
            elif (3 > float(sign.cAverageScore) >= 2):
                twoCategLength += 1
            elif (2 > float(sign.cAverageScore) >= 1):
                oneCategLength += 1
            elif (1 > float(sign.cAverageScore) >= 0):
                zeroCategLength += 1
                
        except:
            pass

    for c in Allcompany:
        try:
            sign = models.Stock6Sign202011.objects.get(cStockID = c)
            if (float(sign.cLossGain) > 0):
                gainCategLength += 1
            elif (float(sign.cLossGain) < 0):
                lossCategLength += 1
            elif (float(sign.cLossGain) == 0):
                tieCategLength += 1

                
        except:
            pass
    '''
    
    signs = DCStock6Sign202102.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202102.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202103(request):

    
    signs = DCStock6Sign202103.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202103.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202104(request):

    
    signs = DCStock6Sign202104.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202104.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202105(request):

    
    signs = DCStock6Sign202105.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202105.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202106(request):

    
    signs = DCStock6Sign202106.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202106.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202107(request):

    
    signs = DCStock6Sign202107.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202107.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202108(request):

    
    signs = DCStock6Sign202108.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202108.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202109(request):

    
    signs = DCStock6Sign202109.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202109.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202110(request):

    
    signs = DCStock6Sign202110.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202110.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202111(request):

    
    signs = DCStock6Sign202111.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202111.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202112(request):

    
    signs = DCStock6Sign202112.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202112.html", locals())