from django.contrib import admin
from travel.models import ContactAdd
from travel.models import PackagesAdd,tranding_package,Devloper_info,PackagaesCountry,PackagaesState,special_package
# Register your models here.


class PackagaesStateAdmin(admin.ModelAdmin):
    fields = ['State','slug','Country']

class PackagesAddAdmin(admin.ModelAdmin):
    fields = ['State','package_place','slug','package_Day','package_Night','package_price','dis']



admin.site.register(PackagesAdd,PackagesAddAdmin)
admin.site.register(ContactAdd)
admin.site.register(tranding_package)
admin.site.register(special_package)
admin.site.register(Devloper_info)
admin.site.register(PackagaesCountry)
admin.site.register(PackagaesState,PackagaesStateAdmin)
