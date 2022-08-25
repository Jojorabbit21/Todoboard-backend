from django.urls import path, include

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    # password/reset
    # password/reset/confirm
    # login
    # logout
    # user
    # password/change
    # token/verify
    # token/refresh
    path('registration/', include('dj_rest_auth.registration.urls')),
]
