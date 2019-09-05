from django.contrib import admin

from .models import Contribution

# class ContributionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'description', 'post_date')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'post_date')
#     list_per_page = 25

admin.site.register(Contribution)

