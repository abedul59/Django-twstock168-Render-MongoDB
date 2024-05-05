from django.contrib import admin

from myapp.models import Stock6Sign202401
from myapp.models import Stock6Sign202402
from myapp.models import Stock6Sign202403
from myapp.models import Stock6Sign202404
from myapp.models import Stock6Sign202405
from myapp.models import Stock6Sign202406





from myapp.models import StockFavs_test168




from myapp.models import StockFavDB
#from myapp.models import Person
#from myapp.models import NewsUnit
from myapp import models

#admin.site.register(NewsUnit)
admin.site.register(models.NewsUnit)
admin.site.register(models.Person)
admin.site.register(models.MacroWaveA)
admin.site.register(models.MacroWaveB)
admin.site.register(models.MacroWaveC)
admin.site.register(models.USBondYieldDB)
#admin.site.register(models.Stock6Sign)
class StockFavs_test168Admin(admin.ModelAdmin):
    list_display=('id','cStockID','cStockName','cDBURL','cScore1st','cScore2nd','cScore3rd','cTodayClose','cPredict_EPS','cPredict_high_price','cPredict_low_price','cNew_up_profit','cNew_down_loss','cRisk_reward','cPredict_high_price_down30','cPredict_low_price_down30','cNew_up_profit_down30','cNew_down_loss_down30','cRisk_reward_down30','cEPSach','cStCap','cEPSnPrf','cPERstab','pubtime')
admin.site.register(StockFavs_test168,StockFavs_test168Admin)










class StockFavDBAdmin(admin.ModelAdmin):
    list_display=('id','cStockID','cStockName','cYearDate','cTodayClose','cPredict_EPS','cPredict_high_price','cPredict_low_price','cNew_up_profit','cNew_down_loss','cRisk_reward','pubtime')
admin.site.register(StockFavDB,StockFavDBAdmin)





class Stock6Sign202401Admin(admin.ModelAdmin):
    list_display=('id','cStockID','cStockName','cNewestSeason','cNewestRev','cSign1','cSign2','cSign3','cSign4','cSign5','cSign6','cAverageScore','cLossGain','pubtime')
admin.site.register(Stock6Sign202401,Stock6Sign202401Admin)

class Stock6Sign202402Admin(admin.ModelAdmin):
    list_display=('id','cStockID','cStockName','cNewestSeason','cNewestRev','cSign1','cSign2','cSign3','cSign4','cSign5','cSign6','cAverageScore','cLossGain','pubtime')
admin.site.register(Stock6Sign202402,Stock6Sign202402Admin)

class Stock6Sign202403Admin(admin.ModelAdmin):
    list_display=('id','cStockID','cStockName','cNewestSeason','cNewestRev','cSign1','cSign2','cSign3','cSign4','cSign5','cSign6','cAverageScore','cLossGain','pubtime')
admin.site.register(Stock6Sign202403,Stock6Sign202403Admin)

class Stock6Sign202404Admin(admin.ModelAdmin):
    list_display=('id','cStockID','cStockName','cNewestSeason','cNewestRev','cSign1','cSign2','cSign3','cSign4','cSign5','cSign6','cAverageScore','cLossGain','pubtime')
admin.site.register(Stock6Sign202404,Stock6Sign202404Admin)

class Stock6Sign202405Admin(admin.ModelAdmin):
    list_display=('id','cStockID','cStockName','cNewestSeason','cNewestRev','cSign1','cSign2','cSign3','cSign4','cSign5','cSign6','cAverageScore','cLossGain','pubtime')
admin.site.register(Stock6Sign202405,Stock6Sign202405Admin)


class Stock6Sign202406Admin(admin.ModelAdmin):
    list_display=('id','cStockID','cStockName','cNewestSeason','cNewestRev','cSign1','cSign2','cSign3','cSign4','cSign5','cSign6','cAverageScore','cLossGain','pubtime')
admin.site.register(Stock6Sign202406,Stock6Sign202406Admin)

#####################################################

