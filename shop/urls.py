from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home, name='home'),
    # path('register/',views.Register, name='register'),
    # path('login/',views.login_page, name='login'),
    # path('logout/',views.logout_page, name='logout'),
    path('category/',views.category, name='category'),
    path('product/',views.product, name='product'),
    path('product/<int:id>/', views.productDetails, name='product_details'),
    path('cart/', views.cart, name='cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)