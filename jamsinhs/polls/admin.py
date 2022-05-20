from django.contrib import admin
from import_export.admin import ExportActionMixin

from .models import Apply, Activity, User, Additonal_hour, Plan


@admin.action(description="취소")
def apply_cancel(modeladmin, request, queryset):
    queryset.update(state=2)


@admin.action(description="승인")
def apply_confirm(modeladmin, request, queryset):
    queryset.update(state=3)


@admin.action(description="이수")
def apply_complete(modeladmin, request, queryset):
    queryset.update(state=4)


class Additonal_hourInline(admin.TabularInline):
    model = Additonal_hour


class PlanInline(admin.TabularInline):
    model = Plan


class ApplyAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ('activity', 'state',)
    list_display = ('student_id', 'name', 'activity',
                    'state', 'completed_time',)
    search_fields = ('student_id', 'name',)
    actions = (apply_cancel, apply_confirm, apply_complete,)
    inlines = [Additonal_hourInline]


class UserAdmin(admin.ModelAdmin):
    list_display = ('studentid', 'name', 'password', 'completed_time',)
    search_fields = ('studentid', 'name',)


class ActivityAdmin(admin.ModelAdmin):
    inlines = [PlanInline]


class PlanAdmin(admin.ModelAdmin):
    list_display = ('activity', 'title', 'due_date')


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Apply, ApplyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Additonal_hour)
admin.site.register(Plan, PlanAdmin)
