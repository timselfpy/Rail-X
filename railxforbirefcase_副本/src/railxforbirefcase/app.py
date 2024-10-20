"""
火车迷好用的一个工具。
"""
import json
from datetime import datetime
import requests
import toga
from toga.style.pack import Pack



class RailXforBirefcase(toga.App):
    def emu_for(self, button):
        text = self.for_text.value
        if "CR" in text.upper() or "CRH" in text.upper():
            search_type = "trainModel"
        elif text.isdigit():
            search_type = "trainSerialNumber"
        elif "铁路局" in text:
            search_type = "trainBureau"
        elif len(text) >= 5:
            search_type = "trainManufacturer"
        elif not text.isdigit():
            search_type = "trainDepartment"
        else:
            return
        data = {
            "trainCategory": "0",
            "type": search_type,
            "keyword": self.for_text.value,
            "pageIndex": "1",
            "pageSize": "99999"
        }
        response = requests.post("https://rail.moefactory.com/api/trainAssignment/queryEmu", data=data)
        response.encoding = "utf-8"
        dic = json.loads(response.text)["data"]["data"]
        data = []
        for i in dic:
            en = []
            for j in i:
                en.append(i[j])
            data.append(en)
        self.for_table.data = data

    def rail_re(self, button):
        text = self.rail_re_text.value
        if "CR" in text.upper() or "CRH" in text.upper():
            q = "emu"
        else:
            q = "train"
        response = requests.get(f"https://api.rail.re/{q}/{text}")
        response.encoding = "utf-8"
        data = []
        for i in json.loads(response.text):
            en = []
            for j in i:
                en.append(i[j])
            data.append(en)
        self.rail_re_table.data = data



    def route(self, button):
        train = self.route_text.value
        date = f"{datetime.today().year}{datetime.today().month}{datetime.today().day}"
        data = {"date": date, "trainNumber": train, "pageIndex": "1", "pageSize": "15"}
        response = requests.post("https://rail.moefactory.com/api/trainNumber/query", data=data)
        response.encoding = "utf-8"
        train_index = response.json()["data"]["data"][0]['trainIndex']

        data = {"date": date, "trainIndex": train_index}
        response = requests.post("https://rail.moefactory.com/api/trainDetails/query", data=data, headers=self.headers)
        response.encoding = "utf-8"
        ls = response.json()["data"]["routing"]["routingItems"]
        all_ls = []
        for i in ls:
            en = []
            for j in i:
                en.append(i[j])
            all_ls.append(en)
        self.route_table.data = all_ls



    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        self.main_window = toga.MainWindow()


        for_ = toga.Box(style=Pack(direction="column", text_align="center"))


        self.for_text = toga.TextInput()
        self.for_text.style.padding = 5

        for_button = toga.Button(text="查询", on_press=self.emu_for, style=Pack(alignment="bottom"))
        for_button.style.padding = 5

        for_.add(self.for_text)
        for_.add(for_button)

        self.for_table = toga.Table(headings=["车型", "车号", "配属路局", "配属动车所", "生产厂家"],)
        self.for_table.style.padding = 5
        self.for_table.style.height = 600
        for_.add(self.for_table)
        for_.add(self.for_text)



        rail_re_ = toga.Box(style=Pack(direction="column", text_align="center"))


        self.rail_re_text = toga.TextInput()
        self.rail_re_text.style.padding = 5

        rail_re_button = toga.Button(text="查询", on_press=self.rail_re, style=Pack(alignment="bottom"))
        rail_re_button.style.padding = 5

        rail_re_.add(self.rail_re_text)
        rail_re_.add(rail_re_button)

        self.rail_re_table = toga.Table(headings=["日期", "车号", "车次"],)
        self.rail_re_table.style.padding = 5
        self.rail_re_table.style.height = 600
        rail_re_.add(self.rail_re_table)
        rail_re_.add(self.rail_re_text)




        route_ = toga.Box(style=Pack(direction="column", text_align="center"))


        self.route_text = toga.TextInput()
        self.route_text.style.padding = 5

        route_button = toga.Button(text="查询", on_press=self.route, style=Pack(alignment="bottom"))
        route_button.style.padding = 5

        route_.add(self.route_text)
        route_.add(route_button)

        self.route_table = toga.Table(headings=["车次", "出发时间", "出发时间", "到达站点", "到达时间"],)
        self.route_table.style.padding = 5
        self.route_table.style.height = 600
        route_.add(self.route_table)
        route_.add(self.route_text)

        container = toga.OptionContainer(
            content=[
                ("配属查询", for_),
                ("交路查询", rail_re_),
                ("交路表", route_),
            ])

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
        }

        self.main_window.content = container

        # Show the main window
        self.main_window.show()




def main():
    return RailXforBirefcase("Rail-X for Birefcase")
