from django.shortcuts import render, redirect # type: ignore
from .models import Fertilizer, SoilCropDetail, Inventory, Order
from .forms import FarmerForm, OrderForm
from .models import Order
from .forms import FarmerRegistrationForm

def register_farmer(request):
    if request.method == "POST":
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after successful registration
    else:
        form = FarmerRegistrationForm()

    return render(request, 'register_farmer.html', {'form': form})



def recommend_fertilizer(request):
    if request.method == "POST":
        soil_type = request.POST.get('soil_type')
        crop_name = request.POST.get('crop_name')

        recommended_fertilizers = Fertilizer.objects.filter(recommended_usage__icontains=soil_type)
        return render(request, 'fertilizer_app/recommend.html', {'fertilizers': recommended_fertilizers})

    return render(request, 'fertilizer_app/recommend.html')

def order_fertilizer(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            inventory = Inventory.objects.get(fertilizer=order.fertilizer)
            if inventory.stock_level >= order.quantity:
                inventory.stock_level -= order.quantity
                inventory.save()
                return redirect('order_success')
            else:
                return render(request, 'fertilizer_app/orders.html', {'form': form, 'error': "Not enough stock!"})

    else:
        form = OrderForm()
    return render(request, 'fertilizer_app/orders.html', {'form': form})

def home(request):
    return render(request, 'fertilizer_app/home.html')
def recommend_fertilizer(request):
    fertilizers = None
    if request.method == 'POST':
        soil_type = request.POST.get('soil_type')
        crop_name = request.POST.get('crop_name')

        # Query fertilizers matching the soil type and crop name
        fertilizers = Fertilizer.objects.filter(soil_type__iexact=soil_type, crop_name__iexact=crop_name)

    return render(request, 'recommend_fertilizer.html', {'fertilizers': fertilizers})
def order_fertilizer(request):
    return render(request, 'orders.html')  # Ensure 'orders.html' exists in templates
def recommend_fertilizer(request):
    soil_type = request.GET.get('soil', '').lower()  # Get soil input
    crop = request.GET.get('crop', '').lower()  # Get crop input

    # Define fertilizer recommendations based on soil type and crop
    fertilizer_data = {
        'clay': {
            'wheat': ['Urea', 'DAP', 'Compost'],
            'rice': ['Potash', 'Manure', 'NPK (20-20-20)'],
        },
        'sandy': {
            'tomato': ['NPK (15-15-15)', 'Organic Fertilizer'],
            'carrot': ['Compost', 'Potash'],
        },
        'loamy': {
            'corn': ['Urea', 'Phosphorus', 'Organic Manure'],
            'potato': ['Potash', 'NPK (10-26-26)'],
        }
    }

    # Check if the entered soil and crop exist in the data
    recommended = fertilizer_data.get(soil_type, {}).get(crop, ['No recommendation found'])

    return render(request, 'recommend_fertilizer.html', {'fertilizers': recommended})


def order_fertilizer(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # Save order to database
            return redirect('order_success')  # Redirect to success page
        else:
            return render(request, 'orders.html', {'form': form, 'error': "Invalid data!"})
    else:
        form = OrderForm()
    return render(request, 'orders.html', {'form': form})

def order_success(request):
    return render(request, 'order_success.html')
