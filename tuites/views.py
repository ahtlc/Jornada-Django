from django.shortcuts import render

def post_tuite(request):
    context = {}
    if request.method == 'POST':
        print('Enviando o form.')
        content = request.POST.get('content', None)
        print(content)
        if content == '' or content.isspace():
            context['error'] = 'Tuite não pode estar vazio!'
    return render(request, 'post_tuite.html', context)
