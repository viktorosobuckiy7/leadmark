from django.contrib import admin
from .models import Service, Portfolio, AboutUs, Blog, UserReservation

admin.site.register(Service)
admin.site.register(AboutUs)
admin.site.register(Blog)
admin.site.register(UserReservation)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_filter = ('service',)