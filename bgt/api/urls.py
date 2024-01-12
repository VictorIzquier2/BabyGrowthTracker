from django.urls import path, include

urlpatterns = [
    path('bebes/', include('bebes.urls')),
    path('desarrollos/', include('desarrollos.urls')),
    path('aseos/', include('aseos.urls')),
    path('suenhos/', include('suenhos.urls')),
    path('comidas/', include('comidas.urls')),
    path('citas/', include('citas.urls')),
    path('vacunas/', include('vacunas.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]