from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views



from personal.views import (
    home_screen_view,
    travel_view,
    contact_view,
    )
from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('travel/', travel_view, name="travel"),
    path('contact/', contact_view, name="contact"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name="password_change"),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
