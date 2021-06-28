from django.shortcuts import render

posts = [
    {
        'author' : 'Kalyan',
        'title'  : 'Foto Editor'
    },
        {
            'author' : 'Kalyan',
            'title'  : 'Foto Editor'
        },
            {
                'author' : 'Kalyan',
                'title'  : 'Foto Editor'
            },
                {
                    'author' : 'Kalyan',
                    'title'  : 'Foto Editor'
                }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'FotoEditor/editPage.html', context)

def editPage(request):
    return render(request, 'FotoEditor/editPage.html')
