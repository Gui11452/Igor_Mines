from django.contrib import admin
from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):
	list_display = ('id', 'usuario', 'validacao')
	list_display_links = ('id', 'usuario', 'validacao')
	list_filter = ('usuario', 'validacao')
	list_per_page = 10
	search_fields = ('usuario__username',)


admin.site.register(Perfil, PerfilAdmin)
