
from django.contrib import admin
from django.urls import path
from loja.views import ProdutoListCreateView, ProdutoRetrieveUpdateDeleteView,ClienteListCreateView,ClienteRetrieveUpdateDeleteView,PedidoListCreateView,PedidoRetrieveUpdateDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('produto/', ProdutoListCreateView.as_view(), name='produto-list-create'),#POST
    path('produto/<int:pk>/', ProdutoRetrieveUpdateDeleteView.as_view(), name='produto-retrieve-update-delete'),#get pat delete


    path('Cliente/', ClienteListCreateView.as_view(), name='Cliente-list-create'),#POST
    path('Cliente/<int:pk>/', ClienteRetrieveUpdateDeleteView.as_view(), name='Cliente-retrieve-update-delete'),#get pat delete

    path('Pedido/', PedidoListCreateView.as_view(), name='Pedido-list-create'),#POST
    path('Pedido/<int:pk>/', PedidoRetrieveUpdateDeleteView.as_view(), name='Pedido-retrieve-update-delete'),#get pat delete
]
