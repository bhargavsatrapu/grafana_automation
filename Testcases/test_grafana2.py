from Utilities import image_comparison_util
from Page_objects.grafana import Grafana
from Page_objects.login import Login_page
from Utilities.db_utils import DB_Utils
from Utilities.read_config_util import ReadConfig
import json

def test_grafana_application_2(setup):
    testDataFile = open("./Test_data/test2.json")
    data = json.load(testDataFile)
    page = setup
    grafana_page = Grafana(page)
    login_page = Login_page(page)
    db_utils=DB_Utils()
    db_utils.connect_db()
    db_utils.execute_query(data["query_drop_table"])
    db_utils.create_table_and_insert_query(data["query_create_table"],data["query_insert_record"],data["table_data_records"])
    db_utils.close_db_connection()
    login_page.launch_application(ReadConfig.get_config_properties("URL"))
    login_page.login_in_grafana(ReadConfig.get_config_properties("USER_NAME"),
                                ReadConfig.get_config_properties("PASSWORD"))
    grafana_page.time_series_visualization(data["query_select_data"], data["path_generated_graph_image"])
    assert image_comparison_util.assert_images(data["path_expected_graph_image"],
                                               data["path_generated_graph_image"]) == 1, "both graph are not identical"
    login_page.log_out_from_grafana()