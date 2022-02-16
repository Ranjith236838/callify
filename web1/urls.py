from django.urls import path, include

from . import views
app_name = 'web1'

urlpatterns = [
	path('transactions/<str:dt>', views.tranc_date),
	path('balance/<str:dt>', views.balance),
	path('details/<int:id>', views.details_id),
	path('add', views.add_trans),
]