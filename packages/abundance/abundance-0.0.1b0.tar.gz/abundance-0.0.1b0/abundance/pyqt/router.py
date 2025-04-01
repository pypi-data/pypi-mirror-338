class Router:
    def __init__(self, app, routes):
        self.__name__ = "router"
        self.app = app
        self.page = app.page
        self.layout = app.router_layout
        self.current_page = None
        self.routes = routes
        self.push('/')
        self.page.show()

    def push(self, path):
        route = self.find_route(path, self.routes)
        if route.get('redirect'):
            self.push(route.get('redirect'))
        else:
            component = route['component']()
            component.app = self.app
            if self.current_page:
                self.layout.replaceWidget(self.current_page, component)
                self.current_page.deleteLater()
            else:
                self.layout.addWidget(component)
            self.current_page = component

            if route.get('children'): self.push_child(component, route)

    def push_child(self, parent, route):
        component = route.get('children')['component']()
        component.app = self.app
        if parent.router_layout.count() > 0:
            parent_page = parent.router_layout.itemAt(0).widget()
            parent.router_layout.replaceWidget(parent_page, component)
            parent_page.deleteLater()
        else:
            parent.router_layout.addWidget(component)

        if route.get('children').get('children'): self.push_child(component, route.get('children'))


    def find_route(self, path, routes):
        for route in routes:
            if route["path"] == path:
                new_route = route.copy()
                new_route.pop('children', None)
                return new_route
            children = route.get("children", [])
            result = self.find_route(path, children)
            if result:
                new_route = route.copy()
                new_route.pop('redirect', None)
                new_route["children"] = result
                return new_route
        return None
