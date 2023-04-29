# Django Tree Menu
This Django app implements a tree menu with the following features:

* Menu is implemented through a template tag.
* All items above the selected item are expanded. The first level of nesting under the selected item is also expanded.
* Menu is stored in the database.
* Menu is edited in the standard Django admin panel.
* The active menu item is determined based on the URL of the current page.
* Multiple menus can be displayed on a single page, identified by their name.
* Clicking on a menu item takes you to the URL specified in the menu. The URL can be specified explicitly or through a named URL.
* Only 1 database query is required to render each menu.
# Installation
Install Django and Python standard library.
Add 'tree_menu' to your INSTALLED_APPS setting.
Include the 'tree_menu.urls' in your project's urls.py.
Run python manage.py migrate to create the menu models.
# Usage
In the Django admin panel, create one or more menus.
In your template, use the template tag {% draw_menu 'menu_name' %} to draw the menu with the specified name.
# Example
## urls.py
    from django.urls import include, path

    urlpatterns = [
        path('tree_menu/', include('tree_menu.urls')),
        # ... other paths ...
    ]

## menu.html
    {% load tree_menu_tags %}
    {% draw_menu 'main_menu' %}
# Contributing
Contributions are welcome! Please submit a pull request with your changes.

# License
***
This project is licensed under the MIT License - see the LICENSE file for details.

# Admin login for local using only!: 
    login: admin
    password: admin
    e-mail: admin@mail.com
