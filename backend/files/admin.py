from django.contrib import admin
from .models import Membership, Program, Trainer, Contact, FitnessProfile, Consultation

admin.site.register(Membership)
admin.site.register(Program)
admin.site.register(Trainer)
admin.site.register(Contact)
admin.site.register(FitnessProfile)

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at")
    search_fields = ("name", "phone")
    list_filter = ("created_at",)
