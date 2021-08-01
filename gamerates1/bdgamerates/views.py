from django.shortcuts import render

# Create your views here.
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'bdgamerates/about.html',
        {
            'title':'Получить ключ.',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )