from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class RearEndServicesConfig(AppConfig):
    name = 'rear_end_services'
    verbose_name = '恐怖袭击数据'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

    menu = (
        ParentItem('应用', children=[
            ChildItem('恐怖袭击数据', url='rear_end_services'),
        ], icon='fa fa-leaf'),
        ParentItem('用户组', children=[
            ChildItem('用户', model='auth.user'),
            ChildItem('组群', model='auth.group'),
        ], icon='fa fa-users'),
        ParentItem('账号操作', children=[
            ChildItem('Password change', url='admin:password_change'),
            ChildItem('Log Out', url='admin:logout'),
        ], align_right=True, icon='fa fa-cog'),
    )

