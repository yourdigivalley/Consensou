from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("FeaturedReviews/", views.FeaturedReviews, name="FeaturedReviews"),
    path("Explore/", views.Explore, name="Explore"),
    # re_path(r'^SearchProduct/(?P<action>.*)', views.SearchProduct)
    # ath(r'^SearchProduct/$', 'SearchProduct', name='name')
    # url(r'^$',views.SearchProduct),
    path('SearchProduct/',views.SearchProduct, name='SearchProduct'),
    # path('mypage/', views.myview)
    # path("contact/", views.contact, name="ContactUs"),
    # path("tracker/", views.tracker, name="TrackingStatus"),
    # path("search/", views.search, name="Search"),
    # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("checkout/", views.checkout, name="Checkout"),
    # path("handlerequest/", views.handlerequest, name="HandleRequest"),

]

