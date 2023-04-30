"""
 Implementation of drawable menu items

Sub menu items are defined in models.py
"""
from django import template
from .models import MenuItem

register = template.Library()


class MenuNode(template.Node):
    """
    MenuNode _summary_

    Each node is an instance of
    django.template.Node and has a render() method.

    Args:
        template (Node instance): Getting the renders from standard
         Django Node instance
    """    """"""

    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        menu_items = MenuItem.objects.filter(menu=self.menu_name)
        menu_items.select_related("parent").order_by("order")

    def build_menu(self, menu_items: list):
        """
        build_menu: Update dictionary representing the tree
        structure, and a string representing the HTML
        code for the menu.

        Args:
            menu_items (list): list of MenuItem objects

        Returns:
            Dictionary representing the tree structure
        """
        menu_dict = {}
        for item in menu_items:
            if item.parent_id is None:
                menu_dict[item] = []
            else:
                parent = item.parent
                if parent not in menu_dict:
                    menu_dict[parent] = []
                menu_dict[parent].append(item)

        return menu_dict

    def render_menu(self, menu_tree: dict):
        """
        render_menu create an HTML code
        for rendering the menu tree

        Args:
            menu_tree (dict): contains all objects
            that contain the db
        """
        html = "<ul>"

        for parent, children in menu_tree.items():
            if parent.is_active():
                active = "active"
            else:
                active = ""
            html += f"<li class='{active}'><a href='{parent.url}'>{parent.name}</a>"
            if children:
                html += self.render_menu(children)
            html += "</ul>"

        return html
@register.tag("draw_menu")
def do_draw_menu(parser, token):
    try:
        tag, menu_name = token.split_contents()
    except template.TemplateSyntaxError:
        raise template.TemplateSyntaxError(f"{tag}, tag must be a one argument")

    return MenuNode(menu_name)