"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from myapp import views
from django.conf.urls import url



from myapp.views import UsersListAll

from myapp.views import stock6
from myapp.views import stock6x
from myapp.views import stock6getOne
from myapp.views import stock6getOneAdmin


from myapp.views import stock6TSE
from myapp.views import stock6OTC

from myapp.views import stock6Admin
from myapp.views import stock6xAdmin
from myapp.views import stock6AdminGL

#from myapp.views import stock6AdminTB


from myapp.views import stock6AdminTB1M
from myapp.views import stock6AdminTB1S
from myapp.views import stock6AdminTB1S1M

from myapp.views import stock6AdminTB2M
from myapp.views import stock6AdminTB1S2M



from myapp.views import stockprice

from myapp.views import stockPrice5y
#from myapp.views import stockPERseg
from myapp.views import stockPERsegx
from myapp.views import stockPERseg2
from myapp.views import stockPERseg2b
from myapp.views import stockPERseg3
from myapp.views import stockPERseg3b

from myapp.views import stockPERsegAdmin
from myapp.views import stockPERsegPEG

from myapp.views import stockPERsegStable
from myapp.views import stockPERsegStableAdmin

from myapp.views import index2
from myapp.views import login2
from myapp.views import logout2
from myapp.views import adduser
from myapp.views import signup

##############
from myapp.views import index
from myapp.views import login
from myapp.views import logout
from myapp.views import detail
from myapp.views import adminmain
from myapp.views import newsadd
from myapp.views import newsedit
from myapp.views import newsdelete
from myapp.views import detail

#from myapp.views import listone
#from myapp.views import listall
from myapp.views import usersmain



from myapp.views import listallscore
from myapp.views import listallseg
from myapp.views import listallsegscore

from myapp.views import Epsachiever
from myapp.views import EpsachieverAdmin

from myapp.views import listallEPS
from myapp.views import EPSachieve2020Q2listall

from myapp.views import StockCapGetter
from myapp.views import StockCapGetterAdmin
from myapp.views import listallCAP
from myapp.views import StockCapVar2020Q2listall



from myapp.views import EPSnProfitGetter
from myapp.views import EPSnProfitGetterAdmin

from myapp.views import EPSnProfitlistall2020Q1
from myapp.views import EPSnProfit2020Q2listall



from myapp.views import AREAdownloads

from myapp.views import stock6downloads
from myapp.views import stockPERsegdownloads
from myapp.views import stockEnterAlldownloads

from myapp.views import BigMoney


from myapp.views import stockPERsegDiv




urlpatterns = [
    
 	path('home/', views.home, name='home'),
	path('population-chart/', views.population_chart, name='population-chart'),
	path('pie-chart/', views.pie_chart, name='pie-chart'),

	path('stock6x_chart/', views.stock6x_chart, name='stock6x_chart'),
    
    path('admin/', admin.site.urls),
    #path('home/', home),
    path('', index),

    path('viewsGetUSBondYield/', views.viewsGetUSBondYield),
    path('viewsGetUSBondYieldAdmin/', views.viewsGetUSBondYieldAdmin),

    path('viewsGetMacroWaveAdmin/', views.viewsGetMacroWaveAdmin),
    path('viewsGetMacroWaveBdmin/', views.viewsGetMacroWaveBdmin),
    path('viewsGetMacroWaveCdmin/', views.viewsGetMacroWaveCdmin),

    path('UsersListAll/', UsersListAll),


    path('viewsISQuery/', views.viewsISQuery),
    path('viewsBSQuery/', views.viewsBSQuery),


    path('stock6/', views.stock6),
    path('stock6x/', views.stock6x),
    path('stock6xDB/', views.stock6xDB),
    path('stockKn/', views.stockKn),

    path('stock6xapp/', views.stock6xapp),


    
    path('stock6getOne/', stock6getOne),
    path('stock6getOneAdmin/', views.stock6getOneAdmin),
    path('stock6getOneH2VAdmin/', views.stock6getOneH2VAdmin),
    path('stock6getOneH2V2Admin/', views.stock6getOneH2V2Admin),

    path('stock6Admin/', stock6Admin),
    path('stock6xAdmin/', stock6xAdmin),     
    path('stock6AdminGL/', stock6AdminGL),



    path('stock6AdminTB1S/', stock6AdminTB1S),        
    path('stock6AdminTB1M/', stock6AdminTB1M),
    path('stock6AdminTB1S1M/', stock6AdminTB1S1M),


    path('stock6AdminTB2M/', stock6AdminTB2M),       
    path('stock6AdminTB1S2M/', stock6AdminTB1S2M),

    path('stock6TSE/', stock6TSE),
    path('stock6OTC/', stock6OTC),
    path('stock6SubCats/', views.stock6SubCats),
    path('stock6SubCatsAdmin/', views.stock6SubCatsAdmin),
    path('stock6Concepts/', views.stock6Concepts),
    

    
    path('stockprice/', stockprice),


    path('stockPrice5y/', stockPrice5y),
    path('stockPrice5yAdmin/', views.stockPrice5yAdmin),
    path('stockNetCapAdmin/', views.stockNetCapAdmin),    
 
    #path('stockPERseg/', views.stockPERseg),
    path('stockPERsegx/', views.stockPERsegx),
    path('stockPERsegxapp/', views.stockPERsegxapp),
    path('stockPERsegxMain/', views.stockPERsegxMain),   
    
    path('stockPERsegxDB/', views.stockPERsegxDB),

    path('stockPERseg2/', stockPERseg2),
    path('stockPERseg2xDB/', views.stockPERseg2xDB),    
    
    path('stockPERseg2b/', stockPERseg2b),
    path('stockPERseg2bxDB/', views.stockPERseg2bxDB),

    path('stockPERseg3/', stockPERseg3),
    path('stockPERseg3xDB/', views.stockPERseg3xDB),   
    
    
    path('stockPERseg3b/', stockPERseg3b),
    path('stockPERsegAdmin/', stockPERsegAdmin), 
    path('stockPERsegPEG/', views.stockPERsegPEG),
    path('stockPERsegPEGMain/', views.stockPERsegPEGMain),
    path('stockPERsegPEGxDB/', views.stockPERsegPEGxDB),    
    
    
    path('stockPERsegStable/', stockPERsegStable),
    path('stockPERsegStableAdmin/', stockPERsegStableAdmin),
    
    path('index2/', index2),
    path('login2/', login2),
    path('logout2/', logout2),
    path('adduser/', adduser),
    path('signup/', signup),

    path('login3/', views.login3),    
    path('logout3/', views.logout3),


    path('listallscore/', listallscore),    
    path('listallseg/', listallseg), 
    path('listallsegscore/', listallsegscore), 
   
    path('index_sns/', views.index_sns),
    
    path('index/', index),
    path('login/', login),
    path('logout/', logout),
  
    
    re_path(r'^detail/(\d+)/$', views.detail),
    re_path(r'^adminmain/$', views.adminmain),
	re_path(r'^adminmain/(\d+)/$', views.adminmain),
 	re_path(r'^newsadd/$', views.newsadd),
	re_path(r'^newsedit/(\d+)/$', views.newsedit),
	re_path(r'^newsedit/(\d+)/(\d+)/$', views.newsedit),
	re_path(r'^newsdelete/(\d+)/$', views.newsdelete),
	re_path(r'^newsdelete/(\d+)/(\d+)/$', views.newsdelete),

    
    re_path(r'^usersmain/$', views.usersmain),
	re_path(r'^usersmain/(\d+)/$', views.usersmain),

    re_path(r'^usersmain_app/$', views.usersmain_app),
	re_path(r'^usersmain_app/(\d+)/$', views.usersmain_app),


    #re_path(r'^usersmain_test168/$', views.usersmain_test168),
	#re_path(r'^usersmain_test168/(\d+)/$', views.usersmain_test168),
    
    path('usersmain_test168/', views.usersmain_test168),
	path('usersmain_test168/<str:pageindex>/', views.usersmain_test168),    

    path('usersmain_common/', views.usersmain_common),
    path('usersmain_common/<str:username>/', views.usersmain_common),
	path('usersmain_common/<str:username>/<str:pageindex>/', views.usersmain_common),

	#re_path(r'^newsdelete_test168/(\d+)/$', views.newsdelete_test168),
	#re_path(r'^newsdelete_test168/(\d+)/(\d+)/$', views.newsdelete_test168),    
    
	path('newsdelete_common/<str:username>/', views.newsdelete_common),
	path('newsdelete_common/<str:username>/<str:newsid>/', views.newsdelete_common),        
	path('newsdelete_common/<str:username>/<str:newsid>/<str:deletetype>/', views.newsdelete_common),
    #path('test168_enterStockFav/', views.test168_enterStockFav),
    path('common_enterStockFavAdmin/<str:username>/', views.common_enterStockFavAdmin),  
 
    path('common_StoFavlistall/', views.common_StoFavlistall),
    path('common_StoFavlistall/<str:username>/', views.common_StoFavlistall),    
    #path('test168_enterStockFavAdmin/', views.test168_enterStockFavAdmin),  
    #path('test168_StoFavlistall/', views.test168_StoFavlistall),

    path('ListallStockFavDB/<str:mess>/', views.ListallStockFavDB),
    path('ListallStockFavDB/', views.ListallStockFavDB),


    
    path('Epsachiever/', Epsachiever),
    path('EpsachieverAdmin/', EpsachieverAdmin),
    path('listallEPS/', listallEPS), 
    
    path('StockCapGetter/', StockCapGetter),
    path('StockCapGetterAdmin/', StockCapGetterAdmin),
    path('listallCAP/', listallCAP), 
    
    
    
    path('EPSnProfitGetter/', EPSnProfitGetter),
    path('EPSnProfitGetterAdmin/', EPSnProfitGetterAdmin),

    ####六大指標    

    path('stock6listall202401/', views.stock6listall202401),
    path('stock6listall202401score/', views.stock6listall202401score),
    path('stock6listall202402/', views.stock6listall202402),
    path('stock6listall202402score/', views.stock6listall202402score),   
    path('stock6listall202403/', views.stock6listall202403),
    path('stock6listall202403score/', views.stock6listall202403score),   
     path('stock6listall202404/', views.stock6listall202404),
    path('stock6listall202404score/', views.stock6listall202404score),        
    
    


###########################################################################################
    
 
    path('stock6listalltse/<str:mess>/', views.stock6listalltse),


    #path('stock6listall202102otc/<str:mess>/', views.stock6listall202102otc),     
    path('stock6listallotc/<str:mess>/', views.stock6listallotc),     

    #path('stock6listall202102Concepts/<str:mess>/', views.stock6listall202102Concepts)
    path('stock6listallConcepts/<str:mess>/', views.stock6listallConcepts),
    #path('stock6listall202102SubCats/<str:mess>/', views.stock6listall202102SubCats),     
    path('stock6listallSubCats/<str:mess>/', views.stock6listallSubCats),     


    #path('stock6listall202102SubCatsAdmin/<str:mess>/', views.stock6listall202102SubCatsAdmin),
    path('stock6listallSubCatsAdmin/<str:mess>/<str:mess_db1>/<str:mess_db2>/', views.stock6listallSubCatsAdmin),
 
###############################################################################################    
    
    
    ####本益比區間



    path('stockPERseglistall202401/', views.stockPERseglistall202401),
    path('stockPERseglistall202401score/', views.stockPERseglistall202401score),
    path('stockPERseglistall202402/', views.stockPERseglistall202402),
    path('stockPERseglistall202402score/', views.stockPERseglistall202402score),
    path('stockPERseglistall202403/', views.stockPERseglistall202403),
    path('stockPERseglistall202403score/', views.stockPERseglistall202403score),

    path('stockPERseglistall202404/', views.stockPERseglistall202404),
    path('stockPERseglistall202404score/', views.stockPERseglistall202404score),


###############################################
 
    #path('EPSnProfit2023Q1listall/', views.EPSnProfit2023Q1listall),
    #path('EPSnProfit2023Q2listall/', views.EPSnProfit2023Q2listall),
    #path('EPSnProfit2023Q3listall/', views.EPSnProfit2023Q3listall),


    #path('stockPERsegStablelistall2021Q2/', views.stockPERsegStablelistall2021Q2), 
    #path('stockPERsegStablelistall2021Q3/', views.stockPERsegStablelistall2021Q3), 
    #path('stockPERsegStablelistall2021Q4/', views.stockPERsegStablelistall2021Q4),
    #path('stockPERsegStablelistall2022Q1/', views.stockPERsegStablelistall2022Q1),

    #path('StockCapVar2022Q3listall/', views.StockCapVar2022Q3listall),
    #path('StockCapVar2023Q1listall/', views.StockCapVar2023Q1listall),
    #path('StockCapVar2023Q2listall/', views.StockCapVar2023Q2listall),    
    #path('StockCapVar2023Q3listall/', views.StockCapVar2023Q3listall),     
            
  
    #path('EPSachieve2023Q1listall/', views.EPSachieve2023Q1listall), 
    #path('EPSachieve2023Q2listall/', views.EPSachieve2023Q2listall),
    #path('EPSachieve2023Q3listall/', views.EPSachieve2023Q3listall),


    path('DC_Prof/', views.DC_Prof),
    path('DC_Rev/', views.DC_Rev),
    path('DC_NetInc/', views.DC_NetInc),    
    path('DC_EPS/', views.DC_EPS),
    path('DC_InvTO/', views.DC_InvTO),
    path('DC_Cashflow/', views.DC_Cashflow),
    path('DC_Stock6Admin/', views.DC_Stock6Admin),
    
    path('AREAdownloads/', views.AREAdownloads), 

    path('stock6downloads/', views.stock6downloads), 
    path('stockPERsegdownloads/', views.stockPERsegdownloads), 
    path('stockEnterAlldownloads/', views.stockEnterAlldownloads),     

    path('BigMoney/', views.BigMoney),
    path('stockPERsegDiv/', views.stockPERsegDiv),
    
    
    path('DB_stock6sign/', views.DB_stock6sign),
    path('DB_stockPERseg/', views.DB_stockPERseg),

    path('DB_DCstock6sign/', views.DB_DCstock6sign),
    path('DB_stockPERsegStable/', views.DB_stockPERsegStable),    

    path('DB_EPSachiever/', views.DB_EPSachiever),

    path('DB_StockCapGetter/', views.DB_StockCapGetter),
    
    path('DB_EPSnProfitGetter/', views.DB_EPSnProfitGetter),
]