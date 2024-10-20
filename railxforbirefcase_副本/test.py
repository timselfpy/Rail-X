route_ = toga.Box(style=Pack(direction="column", text_align="center"))


self.route_text = toga.TextInput()
self.route_text.style.padding = 5

route_button = toga.Button(text="查询", on_press=self.emu_route, style=Pack(alignment="bottom"))
route_button.style.padding = 5

route_.add(self.route_text)
route_.add(route_button)

self.route_table = toga.Table(headings=["车型", "车号", "配属路局", "配属动车所", "生产厂家", "备注"],)
self.route_table.style.padding = 5
self.route_table.style.height = 500
route_.add(self.route_table)
route_.add(self.route_text)