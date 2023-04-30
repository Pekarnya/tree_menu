"""
 Implementation of drawable menu items

Sub menu items are defined in models.py
"""
from django import template
from menu.models import MenuItem
import logging

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
        logging.warning(f"menu name: {menu_name}")

    def render(self, context):
        menu_items = MenuItem.objects.filter(menu=self.menu_name).select_related("parent").order_by("order")
        logging.warning(f"menu items: {menu_items}")

        menu_tree = self.build_menu(menu_items)
        logging.warning(menu_tree)
        menu_html = self.render_menu(menu_tree)
        logging.warning(f"menu html: {menu_html}")
        return menu_html

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
        logging.warning(f"menu tree{menu_tree}")

        html ="".join("<ul>")
        for parent, children in menu_tree.items():
            logging.warning(f"children: {children}")
            logging.warning(f"menu_items: {menu_tree.items()}")
            if parent:
                active = "active"
                html += f"<li class='{active}'><a href='{parent.url}'>{parent.name}</a></li>"
            else:
                html += "</li>"
            
            if children:
                active = "active"
                html += "<ul>"
                html += "<a href=''></a>"
                logging.warning(f"child: {children}")
            else:
                html += "</ul>"

        return html


@register.tag("draw_menu")
def draw_menu(parser, token):
    try:
        tag, menu_name = token.split_contents()
    except template.TemplateSyntaxError:
        raise template.TemplateSyntaxError(f"{tag}, tag must be a one argument")

    return MenuNode(menu_name)