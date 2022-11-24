from django.urls import path,include
from . import views

urlpatterns = [
    path('console', views.consolefun, name='console'),
    path('new2', views.new2fun, name='new2'),
    path('dom', views.domfun, name='dom'),
    path('calculator', views.calfun, name='cal'),
    path('todo', views.todofun, name='todo'),
    path('todoInsertCellFun', views.tod_insertcellfun, name='todo2'),
    path('productList', views.productListfun, name='productList'),
    path('jquery', views.jqueryfun, name='jquery'),
    path('jquery2', views.jquery2fun, name='jquery2'),
    path('form', views.formfun, name='formValidation')
]