from custos_portal.app_config import CustosAppConfig


class AdminConfig(CustosAppConfig):
    name = 'custos_portal.apps.admin'
    label = 'custos_portal_admin'
    verbose_name = 'Admin'
    app_order = 100
    url_home = 'custos_portal_admin:list_requests'
    fa_icon_class = 'fa-cog'
    app_description = """
        Configure and share resources with other users.
    """
    nav = [
        {
            'label': 'Application Catalog',
            'icon': 'fa fa-list',
            'url': 'custos_portal_admin:list_requests',
            'active_prefixes': ['applications', 'list-requests']
        }
    ]