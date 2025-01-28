from django.shortcuts import render, redirect,get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.


# read list all items
def item_list(request):
    items = Item.objects.all().order_by('-created_at') # yangi qo'shilgan ma'lumotlar tepada chiqadi
    return render(request, 'item_list.html', {'items': items})


# Create add a new item
def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
        return render(request,'item_form.html',{'form':form})
    

# Update: edit and existing item
def item_update(request,pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method =='POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
         form = ItemForm(instance=item)
    return render(request,'item_form.html',{'form':form})

# delete item
def delete_item(request,pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request,'item_delete.html', {'item':item})