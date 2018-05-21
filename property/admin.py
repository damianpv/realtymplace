from django.contrib import admin

from .models import Type, Status, Feature, Basic, BasicImages

class TypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'url_slug', 'created_at', 'updated_at',)
    prepopulated_fields = {'url_slug': ('title',)}

admin.site.register(Type, TypeAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'url_slug', 'created_at', 'updated_at', )
    prepopulated_fields = {'url_slug': ('title',)}

admin.site.register(Status, StatusAdmin)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'url_slug', 'created_at', 'updated_at', )
    prepopulated_fields = {'url_slug': ('title',)}

admin.site.register(Feature, FeatureAdmin)

class BasicAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'price', 'state', 'country', 'created_at', 'updated_at', )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Basic, BasicAdmin)
admin.site.register(BasicImages)


'''
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('bedroom', 'bathroom', 'area', 'garage', 'allow_rating', )

admin.site.register(Summary, SummaryAdmin)
'''
