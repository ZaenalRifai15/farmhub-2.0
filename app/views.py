from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/beranda.html')

def deskripsi(request):
    return render(request, 'app/deskripsi-produk.html')

def profile(request):
    return render(request, 'app/profile.html')

def riwayat(request):
    return render(request, 'app/riwayat.html')