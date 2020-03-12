

from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import Permission

from managecar.models import Car, Promo


# Register your models here.


class CarAdmin(admin.ModelAdmin):

    list_display = ['id','name','years','color','image_tag',]
    list_per_number = 15
    list_filter = ['name', 'color', 'years']
    search_fields = ['name']    

    def image_tag(self, obj):
        return format_html('<img src="/media/{}" style="width:30%; margin-left: 20%;" />'.format(obj.pic_url))

    image_tag.short_description = 'Image'


    

class PromoAdmin(admin.ModelAdmin):
    list_display = ['id','name','desc','promotion_code','discount_percent','minimum_cost','expire_day']
    list_per_number = 15
    list_filter = ['name', 'discount_percent', 'expire_day']
    search_fields = ['name']

admin.site.register(Car, CarAdmin)

admin.site.register(Permission)

admin.site.register(Promo, PromoAdmin)
