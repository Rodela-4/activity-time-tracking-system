from django.contrib import admin
from import_export.admin import ExportActionMixin

from .models import Apply, Activity, User, Additonal_hour, Plan


def change_apply_state(state, des):
    @admin.action(description=des)
    def change_state(modeladmin, request, queryset):
        queryset.update(state=state)
    change_state.__name__="change_apply_state_"+str(state)
    return change_state


class Additonal_hourInline(admin.TabularInline):
    model = Additonal_hour


class PlanInline(admin.TabularInline):
    model = Plan


class ApplyAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ('activity', 'state',)
    list_display = ('student_id', 'name', 'activity',
                    'state', 'completed_time',)
    search_fields = ('student_id', 'name',)
    actions = [change_apply_state(state,des) for state,des in Apply.APPLY_STATE]
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
