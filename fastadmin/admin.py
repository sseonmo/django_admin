from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.utils.safestring import mark_safe
from .models import Employees, Departments, Cat

# Register your models here.


class DisplayEmployee(admin.ModelAdmin):
	# 보여줄 field 목록
	list_display = (
		"emp_no",
		"first_name",
		"last_name",
		"birth_date",
		"gender",
		"hire_date",
	)
	# 검색기능
	search_fields = ("first_name",)
	# 필터기능
	list_filter = (
		# "first_name",
		"gender",
		("birth_date", DateRangeFilter),
		("hire_date", DateTimeRangeFilter),
	)
	# sorting
	ordering = ("last_name", "hire_date")
	# read only
	readonly_fields = ["emp_no", "first_name"]

	# 추가 기능 disable
	def has_add_permission(self, request):
		return False

	# 삭제 기능 disable
	def has_delete_permission(self, request, obj=None):
		return False

class DisplayDepartment(admin.ModelAdmin):
	list_display = ("dept_no", "dept_name")

class DisplayCat(admin.ModelAdmin):
	fields = ('name', 'age', 'photo')
	list_display = ('name', 'age', 'photo', 'get_image')

	@staticmethod
	def get_image(obj):
		return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
			# url=obj.photo.url, width=obj.photo.width, height=obj.photo.height)
			url=obj.photo.url, width=200, height=200)
		)

admin.site.register(Employees, DisplayEmployee)
admin.site.register(Departments, DisplayDepartment)
admin.site.register(Cat, DisplayCat)
