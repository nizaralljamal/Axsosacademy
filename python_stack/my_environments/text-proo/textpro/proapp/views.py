from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        language = request.POST.get('language')
        comment = request.POST.get('comment')
        context = {
            'name': name,
            'location': location,
            'language': language,
            'comment': comment
        }
        return render(request, 'submit.html', context)
    return redirect('/')

def test(request):
    return render(request, 'index.html')