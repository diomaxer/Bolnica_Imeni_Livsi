from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'id_number',
            'description',
            'year',
            'diameter1',
            'diameter2',
            'sex',
            'watch_type',
            'brand',
            'condition',
            'equipment',
            'meh_type',

            # Калибр

            'caliber',
            'base_caliber',
            'cruising_range',
            'stones',
            'vibration',
            'jenev_mark',
            'chronometer',
            'master_chronometer',
            'photo',

            # Корпус

            'corpus_material',
            'bezel_material',
            'thickness',
            'waterproof',
            'back_cap',

            # Циферблат и стрелки

            'dial',
            'numbers',
            'dial1',
            'dial2',
            'dial3',
            'numbers1',
            'numbers2',
            'numbers3',
            'numbers4',

            # Браслет

            'bracer',
            'bracer_colour',
            'zip_type',
            'zip_material',

            # Функции

            'func1',
            'func2',
            'func3',
            'func4',
            'func5',
            'func6',
            'func7',
            'func8',
            'func9',
            'func10',
            'func11',
            'func12',
            'func13',
            'func14',
            'func15',
            'func16',
            'func17',
            'func18',
            'func19',
            'func20',
            'func21',







        ]