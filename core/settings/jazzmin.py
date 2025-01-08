JAZZMIN_SETTINGS = {
    "site_title": "Restaurant Admin",
    "site_header": "Restaurant Management",
    "site_brand": "Restaurant Admin",
    "site_logo": "images/restaurant_logo.png",  # Your logo here
    "login_logo": "images/restaurant_logo.png",  # Your login logo here
    "login_logo_dark": True,
    "site_logo_classes": "img-circle",  # Circular image style
    "site_icon": "images/restaurant_icon.png",  # Site icon
    "welcome_sign": "Welcome to the Restaurant Management",
    "copyright": "2025 Restaurant Group",
    "search_model": ["auth.User", "restaurants.Restaurant"],

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "restaurants.Restaurant"},
        {"app": "users"},
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    "order_with_respect_to": ["auth", "restaurants", "users"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "restaurants.Restaurant": "fas fa-utensils",
        "users.User": "fas fa-user-circle",
    },

    "custom_css": "common/css/admin_style.css",  # Custom CSS for style
    "custom_js": "common/js/admin_dashboard.js",  # Custom JS for interactivity
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"restaurants.Restaurant": "vertical_tabs"},
    "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "dark_mode_theme": "slate",
    "theme": "cosmo",  # Vibrant theme
    "navbar": "navbar-dark bg-primary",  # Dark navbar with primary color
    "sidebar": "sidebar-dark-primary",  # Dark sidebar
    "sidebar_nav_small_text": False,
    "sidebar_nav_flat_style": True,  # Flat sidebar
    "sidebar_nav_compact_style": False,
    "button_classes": {
        "primary": "btn-danger",  # Red primary buttons
        "secondary": "btn-info",  # Info buttons
        "success": "btn-success",  # Green buttons
        "danger": "btn-warning"  # Orange buttons for warnings
    },
    "footer_fixed": True,  # Fixed footer
    "layout_boxed": False,  # Full-width layout
}
