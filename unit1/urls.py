from django.urls import path
from . import views
urlpatterns=[
    path('unit1/',views.unit1),
    path('unit1/unit2/',views.unit2),
    path('unit1/unit2/unit3/',views.unit3),
    path('unit1/unit2/unit3/unit4/',views.unit4),
    path('unit1/unit2/unit3/unit4/unit5/',views.unit5),
]
