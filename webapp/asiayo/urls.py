"""
URL configuration for asiayo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator

from api.routers import v1_router


v1_schema = get_schema_view(
    openapi.Info(
        title="Asiayo take home quiz",
        default_version="v1",
    ),
    public=True,
    generator_class=OpenAPISchemaGenerator,
    patterns=[
        path("api/v1/", include(v1_router.urls))
    ]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/swagger', v1_schema.with_ui("swagger"), name="v1_swagger"),
    path('api/v1/', include((v1_router.urls, "api"), namespace="v1")),
]
