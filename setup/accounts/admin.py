from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Student, Teacher, Admin , Image
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('username','email', 'password', 'phone_number', 'is_student', 'is_teacher','is_admin', 'created_date')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

class MyAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'add')
    search_fields = ('user', 'add')
    list_filter = ('user', 'add')
    list_display_links = ('user', 'add')
class MyStudent(admin.ModelAdmin):
    
    list_display = ('user', 'standard', 'add')
    search_fields = ('user','standard', 'add')
    list_filter = ('user','standard', 'add')
    list_display_links = ('user','standard', 'add')
class MyTeacher(admin.ModelAdmin):
    
    list_display = ('user', 'subject', 'add')
    search_fields = ('user', 'subject', 'add')
    list_filter = ('user', 'subject', 'add')
    list_display_links = ('user', 'subject','add')
class Myphoto(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src= "{}" width= "49" />'.format(object.photo.url))
    list_display = ('user', 'myphoto', 'date')            
    list_display_links = ('user',  'date')            
    search_fields = ('user',  'date')      
    list_filter = ('user',  'date')            
          
admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(Student, MyStudent)
admin.site.register(Teacher, MyTeacher)
admin.site.register(Admin, MyAdmin)
admin.site.register(Image, Myphoto)
