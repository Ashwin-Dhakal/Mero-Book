from django.contrib import admin
from .models import Details

class DetailsModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "Publisher", "Class",  "Your_District", "Ward_number", "Edition", "Status"]
    class Meta:
        model = Details

admin.site.register(Details, DetailsModelAdmin)




