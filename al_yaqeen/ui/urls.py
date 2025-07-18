"""URLConf for al_yaqeen.ui"""

from django.contrib.auth import views as auth
from django.urls import path

from al_yaqeen.ui import views

# Create your URLConf here.
app_name = "ui"


auth_urls = [
    path("accounts/login/", auth.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth.LogoutView.as_view(), name="logout"),
    path("accounts/subscribe/", views.SignupView.as_view(), name="subscribe"),
    path("accounts/profile/", views.ProfileView.as_view(), name="profile"),
    path("accounts/<int:pk>/settings/", views.UserUpdateView.as_view(), name="u-user"),
    path("accounts/<int:pk>/delete/", views.UserDeleteView.as_view(), name="d-user"),
    path(
        "accounts/password/change/",
        auth.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password/change/done/",
        auth.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "accounts/password/reset/",
        auth.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password/reset/done/",
        auth.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/password/reset/<uidb64>/<token>/",
        auth.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/password/reset/complete/",
        auth.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]


urlpatterns = [
    *auth_urls,
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("articles/", views.ArticleListView.as_view(), name="articles"),
    path("articles/<int:year>/", views.ArticleYearView.as_view(), name="articles-y"),
    path(
        "articles/<int:year>/<int:month>/",
        views.ArticleMonthView.as_view(),
        name="articles-m",
    ),
    path(
        "articles/<int:year>/<int:month>/<int:day>/",
        views.ArticleDayView.as_view(),
        name="articles-d",
    ),
    path(
        "articles/<int:year>/<int:month>/<int:day>/<slug:slug>/",
        views.ArticleDetailView.as_view(),
        name="article",
    ),
]
