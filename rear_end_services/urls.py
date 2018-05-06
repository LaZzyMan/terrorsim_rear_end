from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rear_end_services import views

router = DefaultRouter()
router.root_view_name = 'API List'
router.register(r'tdinfo', views.TDInfoViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'region', views.RegionViewSet)
router.register(r'attack', views.AttackViewSet)
router.register(r'weapon', views.WeaponViewSet)
router.register(r'target', views.TargetViewSet)

country_list = views.CountryViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    url(r'^', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
