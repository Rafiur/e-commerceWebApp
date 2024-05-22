from django.shortcuts import render, get_object_or_404

from .models import Item

def detail(request, pk):
    item = get_object_or_404(Item, pk = pk)
    
    related_items = Item.objects.filter(category = item.category, is_sold = False).exclude(pk = pk)[0:3]
    # to show related items we filter by same category and exclude the same item which is view by matching primary key
    # the 0:3 at the end represents the split of 3 items to be shown in the related items 
    
    return render(request, 'item/detail.html', {
        'item' : item,
        'related_items' : related_items
        
    })



# Create your views here.
