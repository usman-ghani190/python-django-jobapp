from django.contrib import admin

from app.models import Author, JobPost, Location, Skill

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date')
    list_filter= ('date', 'salary', 'expiry')
    search_fields= ('title',)
    fieldsets = (
        ('Basic Information', {
            "fields": (
             'title', 'description'   
            ),
        }),
        ('More Information', {
            "fields": (
                'expiry', 'salary', 'slug'
            )
        })
    )
    

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)