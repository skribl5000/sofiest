from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView, example_view, get_events, get_bets, post_bet, get_bet, get_categories


urlpatterns = [
    url(r'^auth/login/$',
        obtain_auth_token,
        name='auth_user_login'),
    url(r'^auth/register/$',
        CreateUserAPIView.as_view(),
        name='auth_user_create'),
    url(r'^auth/logout/$',
        LogoutUserAPIView.as_view(),
        name='auth_user_logout'),
    url(r'^example_view/', example_view, name='test'),
    url(r'^events/', get_events, name='active_events'),
    url('^bets/', get_bets, name='bets'),
    url('^post_bet/', post_bet, name='post_bet'),
    url('^get_bet/', get_bet, name='get_bet'),
    url('^event_category/', get_categories, name='event_category')
]