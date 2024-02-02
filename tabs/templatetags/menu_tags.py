from django import template
from tabs.models import MenuItem, Menu

register = template.Library()


@register.inclusion_tag("tabs/menu.html")
def draw_menu(menu_name: str, menu_url: str):
    menu_items = Menu.objects.get(url=menu_name).items.all().order_by("parent", "name")
    menu_items_extended = [(m, m.url, m.id, m.parent_id) for m in menu_items]
    parents = {}
    children = {}
    root = [url for _, url, _, parent_id in menu_items_extended if parent_id is None][0]
    if menu_url not in [url for _, url, _, _ in menu_items_extended]:
        menu_url = root
    for m, m_url, m_id, p_id in menu_items_extended:
        children[p_id] = children.get(p_id, []) + [m]
        parents[m_id] = p_id
        if menu_url is None and p_id is None:
            menu_url = m.url
            menu_id = m_id
        elif m.url == menu_url:
            menu_id = m_id

    menu = []
    current_menu_id = menu_id
    while current_menu_id is not None:
        if current_menu_id in children:
            menu.append(children.get(current_menu_id, []))
        current_menu_id = parents[current_menu_id]
    else:
        menu.append(children.get(current_menu_id, []))

    return {
        "menu": menu[::-1],
    }
