from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('apps.login_reg_app.urls', namespace='users')),
    # url(r'^accounts/', include('apps.login_reg_app.urls', namespace='users')),
    url(r'^books/', include('apps.book_reviews_app.urls', namespace='reviews')),
]
