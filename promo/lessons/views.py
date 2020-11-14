from django.shortcuts import render
from .models import Lessons
# from users.models import User, get_promo


def lessons_view(request):
    lessons = Lessons.objects.all()
    if request.user.promo == "1234":
        context = {'lessons': lessons}
        return render(request, 'lessons_promo.html', context)
    else:
        context = {'lessons': lessons}
        return render(request, 'lessons.html', context)

"""
<div>
    {% if user.is_authenticated %}
        {% if lessons.count > 0 %}
        <table>
            <tr><th>Название</th><th>Цена</th></tr>
            {% for prod in lessons %}
            <tr>
                <td>{{ prod.name }}</td>
                <td>{{ prod.get_sale }} Buck$</td>
            </tr>
            {% endfor %}
        {% endif %}
        </table>
    {% else %}
        {% if lessons.count > 0 %}
        <table>
            <tr><th>Название</th><th>Цена</th></tr>
            {% for prod in lessons %}
            <tr>
                <td>{{ prod.name }}</td>
                <td>{{ prod.price }} Buck$</td>
            </tr>
            {% endfor %}
        {% endif %}
        </table>
    {% endif %}
</div>"""
