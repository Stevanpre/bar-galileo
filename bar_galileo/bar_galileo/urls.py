from django.contrib import admin
from django.urls import path  # puedes añadir include si activas los submódulos
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),  # Ruta del panel de administración

    # Público
    path("", views.index, name="index"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("menu/", views.menu, name="menu"),

    # Reservas
    path("reservas/eventos/", views.reserva_eventos, name="reserva_eventos"),
    path("reservas/grupal/", views.reserva_grupal, name="reserva_grupal"),

    # Autenticación
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),

    # Si luego activas submódulos:
    # path("oper/", include("app.urls_oper")),
    # path("inv/", include("app.urls_inv")),
    # path("fin/", include("app.urls_fin")),
]
