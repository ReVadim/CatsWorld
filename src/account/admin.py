from django.contrib import admin
from .models import CatsUser


class CatsUserAdmin(admin.ModelAdmin):
    """ Supportive class
    """
    list_display = ('__str__', 'is_activated', 'join_date')
    search_fields = ('username', 'email', 'city')
    fields = ('password', 'username', 'avatar', 'email', ('city', 'country'), ('is_active', 'is_activated'))
    readonly_fields = ('join_date',)


admin.site.register(CatsUser, CatsUserAdmin)
