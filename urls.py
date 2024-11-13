from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('present-simple',views.present_simple,name='present simple'),
    path('present-perfect',views.present_perfect,name='present perfect'),
    path('present-continuous',views.present_continuous,name='present continuous'),
    path('past-simple',views.past_simple,name='past simple'),
    path('past-perfect',views.past_perfect,name='past perfect'),
    path('past-continuous',views.past_continuous,name='past continuous'),
    path('future-simple',views.future_simple,name='future simple'),
    path('exercises',views.exercices,name='exercises'),
    path('check',views.check,name='check'),
    

]