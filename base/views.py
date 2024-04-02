from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

my_dict = {
    '1': 'one',
    '2': 'two',
}


def test(request):
    description = list(my_dict)
    res = ''
    for x in description:
        redirect_path = reverse('1', args=(x,))  # Передача іменованого шляху '1'
        res += f'<li> <a href="{redirect_path}"> {x} </a> </li>'
    return HttpResponse(res)


def add_test(request, new_path):
    description = my_dict.get(new_path)
    ren = {
        'description_test': description,
        'practise': {'name': 'Vovik', 'age': '1'},
        'title': new_path,
    }
    return render(request, 'base/info.html', context=ren)
