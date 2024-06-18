# from django.contrib import admin
# from .models import Disaster, DisasterType, Province, City

# from import_export import resources
# from import_export.admin import ImportExportModelAdmin



# # Change Title in Admin Panel and change browswer tab title
# admin.site.site_header = 'Canadian Disaster Database'
# admin.site.site_title = 'CDD'


# @admin.register(DisasterType)
# class DisasterTypeAdmin(admin.ModelAdmin):
#     list_display = ['en_name', 'fr_name']

    

# @admin.register(Disaster)
# class DisasterAdmin(admin.ModelAdmin):
#     list_display = ('name', 'event_date', 'description_english', 'description_french', 'disaster_type', 'province', 'city',)
#     # list_display_links = []
#     # fields = (('name', 'event_date'), ('description_english', 'description_french'), 'disaster_type', 'province', 'city',)
#     # fieldsets = [('General Information', {'fields':('name', 'event_date')})]



# @admin.register(Province)
# class ProvinceAdmin(admin.ModelAdmin):
#     list_display = ['name']


# @admin.register(City)
# class CityAdmin(admin.ModelAdmin):
#     list_display = ['name']




from django.contrib import admin
from .models import Disaster, DisasterType, Province, City

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Change Title in Admin Panel and change browser tab title
admin.site.site_header = 'Canadian Disaster Database'
admin.site.site_title = 'CDD'


@admin.register(DisasterType)
class DisasterTypeAdmin(admin.ModelAdmin):
    list_display = ['en_name', 'fr_name']


# Create a resource class for the Disaster model
class DisasterResource(resources.ModelResource):
    class Meta:
        model = Disaster


@admin.register(Disaster)
class DisasterAdmin(ImportExportModelAdmin):
    resource_class = DisasterResource
    list_display = ('name', 'event_date', 'description_english', 'description_french', 'disaster_type', 'province', 'city',)
    # list_display_links = []
    # fields = (('name', 'event_date'), ('description_english', 'description_french'), 'disaster_type', 'province', 'city',)
    # fieldsets = [('General Information', {'fields':('name', 'event_date')})]


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
