from django.contrib import admin
from import_export.admin import ExportActionMixin

# Register your models here.
from .models import Apply, Activity, User, Additonal_hour, Plan

class Additonal_hourInline(admin.TabularInline):
    model = Additonal_hour

class PlanInline(admin.TabularInline):
    model = Plan

class ApplyAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ('activity','student_id',)
    list_display = ('student_id', 'name', 'activity', 'state', 'completed_time',)
    inlines = [Additonal_hourInline]

class UserAdmin(admin.ModelAdmin):
    list_display = ('studentid', 'name', 'password', 'completed_time',)

class ActivityAdmin(admin.ModelAdmin):
    inlines = [PlanInline]

class PlanAdmin(admin.ModelAdmin):
    list_display = ('activity', 'title', 'due_date')

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Apply, ApplyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Additonal_hour)
admin.site.register(Plan, PlanAdmin)
