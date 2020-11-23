from rest_framework import serializers
from .models import Product, Images


class ProductSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username')
    sex_name = serializers.CharField(source='sex.name')
    watch_type_name = serializers.CharField(source='watch_type.name')
    brand_name = serializers.CharField(source='brand.name')
    condition_name = serializers.CharField(source='condition.name')
    equipment_name = serializers.CharField(source='equipment.name')
    meh_type_name = serializers.CharField(source='meh_type.name')
    corpus_material_name = serializers.CharField(source='corpus_material.name')
    bezel_material_name = serializers.CharField(source='bezel_material.name')
    glass_name = serializers.CharField(source='glass.name')
    waterproof_name = serializers.CharField(source='waterproof.name')
    dial_name = serializers.CharField(source='dial.name')
    numbers_name = serializers.CharField(source='numbers.name')
    bracer_name = serializers.CharField(source='bracer.name')
    bracer_colour_name = serializers.CharField(source='bracer_colour.name')
    zip_type_name = serializers.CharField(source='zip_type.name')
    zip_material_name = serializers.CharField(source='zip_material.name')


    class Meta:
        model = Product
        fields = [
            'user_username',
            'name',
            'id_number',
            'description',
            'price',
            'year',
            'diameter1',
            'diameter2',
            'sex_name',
            'watch_type_name',
            'brand_name',
            'condition_name',
            'equipment_name',
            'meh_type_name',

            # Калибр

            'caliber',
            'base_caliber',
            'cruising_range',
            'stones',
            'vibration',
            'jenev_mark',
            'chronometer',
            'master_chronometer',
            #'photo',

            # Корпус

            'corpus_material_name',
            'bezel_material_name',
            'thickness',
            'glass_name',
            'waterproof_name',
            'back_cap',

            # Циферблат и стрелки

            'dial_name',
            'numbers_name',
            'dial1',
            'dial2',
            'dial3',
            'numbers1',
            'numbers2',
            'numbers3',
            'numbers4',

            # Браслет

            'bracer_name',
            'bracer_colour_name',
            'zip_type_name',
            'zip_material_name',

            # Функции

            'moon_faze',
            'chronograf',
            'flyback',
            'the_striking_mechanism',
            'turbion',
            'day_in_week',
            'day_in_year',
            'calendar_on_4_years',
            'alarm_clock',
            'calendar_of_time',
            'tahimetr',
            'minute_repeater',
            'split_chronograf',
            'panoramic_date',
            'repeater',
            'date',
            'month_indicator',
            'year_calendar',
            'eternal_calendar',
            'gmt',
            'jump_hour',
        ]


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
