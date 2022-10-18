from django.contrib import admin
from .models import Item, CartItems, Reviews
from django.db import models

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Created By", {'fields': ["created_by"]}),
        ("Title", {'fields': ["title"]}),
        ("Image", {'fields': ["image"]}),
        ("Description", {'fields': ["description"]}),
        ("Price", {'fields': ["price"]}),
        ("Pieces", {'fields': ["pieces"]}),
        ("Instructions", {'fields': ["instructions"]}),
        ("Labels", {'fields': ["labels"]}),
        ("Label Colour", {'fields': ["label_colour"]}),
        ("Slug", {'fields': ["slug"]}),
    ]
    list_display = ('id','created_by','title','description','price','labels')
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'created_by':
            # setting the user from the request object 
            kwargs['initial'] = request.user.id 
            # making the field readonly 
            kwargs['disabled'] = True 
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
    def get_queryset(self, request): 
        qs = super(ItemAdmin, self).get_queryset(request) 
        if request.user.is_superuser: 
            return qs 
        return qs.filter(created_by=request.user)

    

class CartItemsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Order Status", {'fields' : ["status"]}),
        ("Delivery Date", {'fields' : ["delivery_date"]})

    ]
    list_display = ('id','user','item','quantity','ordered','ordered_date','delivery_date','status')
    list_filter = ('ordered','ordered_date','status') 
    def get_queryset(self, request): 
        qs = super(CartItemsAdmin, self).get_queryset(request) 
        print(qs)
        if request.user.is_superuser: 
            return qs 
        return qs.filter(item__created_by=request.user, ordered=True)
    

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user','item','review','posted_on')

admin.site.register(Item,ItemAdmin)
admin.site.register(CartItems,CartItemsAdmin)
admin.site.register(Reviews,ReviewsAdmin)
