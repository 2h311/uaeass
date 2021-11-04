from django.contrib import admin
from main.models import Assignment, Review, Sample, SampleMultipleFile

# Register your models here.
admin.site.register(Assignment)
admin.site.register(Review)


class MultipleFileInline(admin.TabularInline):
	model = SampleMultipleFile


class SampleAdmin(admin.ModelAdmin):
	inlines = [ MultipleFileInline ]
	prepopulated_fields = {'slug': ('heading',)}

admin.site.register(Sample, SampleAdmin)