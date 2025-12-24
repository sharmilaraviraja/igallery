from django.shortcuts import render

def gallery_view(request):
    images = [
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
    ]
    return render(request, 'gallery/gallery.html', {'images': images})

