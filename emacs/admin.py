from django.contrib import admin

# Register your models here.
from .models import Code


class CodeAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'added_by',
                    'modified',
                    'created')

    list_filter = ('name',)

    fieldsets = (
        ('Basic Info', {'fields': ('name', 'added_by')}),
        ('More Info', {'fields': ('description', 'gist_url', 'download_count')}),
        ('Code', {'fields': ('code',)}),
        ('Screenshot', {'fields': ('screenshot',)}),
        ('TimeStamp', {'fields': ('created', 'modified')}),
    )
    readonly_fields = ('created', 'modified')

admin.site.register(Code, CodeAdmin)
