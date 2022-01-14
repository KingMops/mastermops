from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField

# Register your models here.







class ToyAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='toy'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)







class ConsoleAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='console'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class GamepadAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='gamepad'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)






class VideogameAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='videogame'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Gamepad, GamepadAdmin)
admin.site.register(Toy, ToyAdmin)
admin.site.register(Videogame, VideogameAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(CartProduct)

