from django.contrib import admin, messages
from .models import *
from django.http import HttpResponse
from django.contrib.admin.helpers import ActionForm
from django import forms
from datetime import timedelta
from durationwidget.widgets import TimeDurationWidget as tdw
# Register your models here.
admin.site.register(Dept)
admin.site.register(Review)
admin.site.register(Profs)
admin.site.register(Courses)


def delete_reported_reviews(modeladmin, request, queryset):
    for report in queryset:
        report.review.delete()
    messages.success(request, f"{str(len(queryset))} reviews have been warned")


def send_warning_to_user(modeladmin, request, queryset):
    for report in queryset:
        user = report.reported_user
        warn = Warnings(user=user)
        warn.message = f"You have been warned for the following comment on Prof. {report.review.prof.name} for the course {report.review.course}\n\n[{report.review.comment}]\n\nIf u do this again u might be banned form posting anything on this system by the administrators"
        warn.save()
    messages.success(request, f"{str(len(queryset))} users have been warned")


def send_warning_and_delete(modeladmin, request, queryset):
    send_warning_to_user(modeladmin, request, queryset)
    delete_reported_reviews(modeladmin, request, queryset)


def ban_users(modeladmin, request, queryset):
    # print(request.POST)
    post = request.POST
    ban_perm = False
    duration = None
    if(request.POST['permanent_ban']):
        ban_perm = True
    else:
        duration = timedelta(days=int(post['duration_0']), hours=int(post['duration_1']), minutes=int(post['duration_2']), seconds=int(post['duration_3']))

    for report in queryset:
        user = report.reported_user
        for prev_ban in user.banned_set.all():
            prev_ban.delete()
        ban = Banned(user=user)
        if ban_perm:
            ban.permanent_ban = True
        else:
            ban.ban_duration = duration
        ban.save()
    if(not ban_perm):
        messages.success(request, f"{str(len(queryset))} Users have(has) been banned for {str(duration)}")
    else:
        messages.success(request, f"{str(len(queryset))} Users have(has) been banned Permanently")


send_warning_to_user.short_description = "Send warning to the reported user"
delete_reported_reviews.short_description = "Delete the corresponding reviews"
send_warning_and_delete.short_description = "Send warning and delete the selected"
ban_users.short_description = "Ban all the users who posted these reviews"

class BanDurationForm(ActionForm):
    duration = forms.DurationField(widget=tdw(), required=False, initial=timedelta(days=10), help_text="Enter the duration to ban all the selected users", label="Ban Duration")
    permanent_ban = forms.BooleanField(label="Ban Permanently?", initial=False)


@admin.register(ReportReview)
class ReportReviewAdmin(admin.ModelAdmin):
    action_form = BanDurationForm
    list_display = ['category', 'reporting_user', 'reported_user', 'review']
    actions = [delete_reported_reviews, send_warning_to_user,send_warning_and_delete, ban_users]


@admin.register(Banned)
class BannedAdmin(admin.ModelAdmin):
    list_display = ['user', 'ban_date', 'ban_relieve','ban_duration', 'time_to_relieve']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user','category','timestamp','log']
