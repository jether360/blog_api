from django.apps import AppConfig


class BlogApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_api'

def ready(self):
        import blog_api.models