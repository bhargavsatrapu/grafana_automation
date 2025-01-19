from Base.Actions import Actions
import time
import os

class Grafana(Actions):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.cwd = os.getcwd()

    navigation_section_toggle_button = "#mega-menu-toggle"
    dashboard_navigation_option = "//span[text()='Dashboards']"
    dashboard_page_new_button = "//span[text()='New']"
    dashboard_page_new_dashboard_button = "//span[text()='New dashboard']"
    dashboard_page_add_visualization_button = "//span[text()='Add visualization']"
    select_db_mysql_button = "//small[text()='MySQL']/.."
    query_editor_button = "(//label[text()='Code']//..)[1]"
    editor_line = "[class='view-line']"
    dashboard_page_run_query_button = "[class='css-72lnkn-button']"
    zoom_graph_button = "[data-testid='time-series-zoom-to-data']"
    graph_visualization_field = "[data-testid='uplot-main-div']"
        
    def time_series_visualization(self,db_query,path_to_store_grap_png):
        self.click_on_element(self.navigation_section_toggle_button)
        self.click_on_element(self.dashboard_navigation_option)
        self.click_on_element(self.dashboard_page_new_button)
        self.click_on_element(self.dashboard_page_new_dashboard_button)
        self.click_on_element(self.dashboard_page_add_visualization_button)
        self.click_on_element(self.select_db_mysql_button)
        time.sleep(4)
        self.click_on_element(self.query_editor_button)
        time.sleep(10)
        self.click_on_element(self.editor_line)
        self.page.keyboard.type(db_query)
        self.click_on_element(self.dashboard_page_run_query_button)
        time.sleep(4)
        self.click_on_element(self.zoom_graph_button)
        time.sleep(5)
        self.page.locator(self.graph_visualization_field).screenshot(path=os.path.join(path_to_store_grap_png) )



        