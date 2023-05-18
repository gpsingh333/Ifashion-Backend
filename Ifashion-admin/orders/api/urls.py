from django.urls import path

from .views import *

urlpatterns = [

	path('deliver_address' ,DeliveryAddressAPIView.as_view(), name="add_getall_address"),
	path('deliver_address/<int:addr_id>' ,ActionOnDeliveryAddressAPIView.as_view(), name="edit_delete_address"),

	path('places_order' ,MakeOrderAPIView.as_view(), name="place_order"),

	# path('orders_history' ,OrderHistoryAPIView.as_view(), name="orders_history"),

	path('orders_history' ,AllOrderProductHistoryAPIView.as_view(), name="orders_history"),
	path('orders_history/<int:id>' ,OrderedProductHistoryAPIView.as_view(), name="ordered_product_history"),
	path('rate_a_product' ,ProductRateAPIView.as_view(), name="rate_a_product"),
	path('cancel_order' ,CancelOrderAPIView.as_view(), name="cancel_order"),
	path('return_order' ,ReturnOrderAPIView.as_view(), name="return_order"),
	path('exchange_order' ,ExchangeOrderAPIView.as_view(), name="exchange_order"),
	path('change_order_status' ,ChangeOrderStatusOrderAPIView.as_view(), name="change_order_status"),


]




