from django.shortcuts import render

def buku(request):
    judul = "Belajar Django"
    penulis = "Akbar Pradana"
    
    konteks = {
        'title': judul,
        'penulis': penulis
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return HttpResponse('<h1>Halaman Penerbit</h1>')
