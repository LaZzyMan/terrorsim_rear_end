from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rear_end_services import views

router = DefaultRouter()
router.root_view_name = 'API List'
router.register(r'tdgeneral', views.TDGeneralViewSet, base_name='tdgeneral')
router.register(r'tdinfo', views.TDInfoViewSet, base_name='tdinfo')
router.register(r'country', views.CountryViewSet, base_name='country')
router.register(r'region', views.RegionViewSet, base_name='region')
router.register(r'attack', views.AttackViewSet, base_name='attack')
router.register(r'weapon', views.WeaponViewSet, base_name='weapon')
router.register(r'target', views.TargetViewSet, base_name='target')

country_list = views.CountryViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    url(r'^', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
