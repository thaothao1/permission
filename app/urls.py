from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("web.urls")),
    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
]
