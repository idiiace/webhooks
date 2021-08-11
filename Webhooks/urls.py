"""Webhooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hooks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xGrSGK7N1FeRWb4LkWu8roQBzBPwoYblgP0pk9UPyEHWnT0y2',api),
]
'''{
    "id": 768570754,
    "status": "paid",
    "status_detail": null,
    "date_created": "2013-05-27T10:01:50.000-04:00",
    "date_closed": "2013-05-27T10:04:07.000-04:00",
    "order_items": [{
        "item": {
            "id": "MLB12345678",
            "title": "Samsung Galaxy",
            "variation_id": null,
            "variation_attributes": []
        },
        "quantity": 1,
        "unit_price": 499,
        "currency_id": "BRL"
    }],
    "total_amount": 499,
    "currency_id": "BRL",
    "buyer": {
        "id": "123456789",
        "nickname": "COMPRADORTESTE",
        "email": "b@b.com",
        "first_name": "Comprador de testes",
        "last_name": "da Silva",
    },
    "seller": {
        "id": "123456789",
        "nickname": "VENDEDORTESTES",
        "email": "a@a.com",
        "first_name": "Vendedor de Testes",
        "last_name": "testes de documentacao"
    },
    "payments": [{
        "id": "596707837",
        "transaction_amount": 499,
        "currency_id": "BRL",
        "status": "approved",
        "date_created": null,
        "date_last_modified": null
    }],
    "feedback": {
        "purchase": null,
        "sale": null
    },
    "shipping": {
        "id": 20676482441
    },
    "tags": [
        "paid",
        "not_delivered"
    ]
}'''