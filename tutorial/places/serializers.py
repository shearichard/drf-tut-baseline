from rest_framework import serializers

from places.models import Country

class CountrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Country
        fields = ['iso_country_names_en', 'alpha_2_code', 'alpha_3_code', 'numeric_code', 'iso_3166_2']
