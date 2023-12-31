from django.urls import path
from main.views import create_product_flutter, show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user
from main.views import logout_user, add_amount_button, reduce_amount_button, remove_item_button, edit_product,get_item_json, add_item_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_amount_button/<int:item_id>/', add_amount_button, name='add_amount_button'),
    path('reduce_amount_button/<int:item_id>/', reduce_amount_button, name='reduce_amount_button'),
    path('remove_item_button/<int:item_id>/', remove_item_button, name='remove_item_button'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_item_json, name='get_item_json'),
    path('create-ajax/', add_item_ajax, name='add_item_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]