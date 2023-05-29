from utils.cheking import Сhecking
from utils.api import Google_maps_api
import allure

"""Создание, измененение и удаление новой локации"""

@allure.epic("Позитивная проверка  API")
class Test_create_place():

    @allure.description("Создание, измененение и удаление новой локации")
    def test_create_new_place(self):
        print("Метод POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Сhecking.check_status_code(result_post, 200)
        Сhecking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Сhecking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = Google_maps_api.get_new_place(place_id)
        Сhecking.check_status_code(result_get, 200)
        Сhecking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Сhecking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Сhecking.check_status_code(result_put, 200)
        Сhecking.check_json_token(result_put, ['msg'])
        Сhecking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Сhecking.check_status_code(result_get, 200)
        Сhecking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Сhecking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Метод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Сhecking.check_status_code(result_delete, 200)
        Сhecking.check_json_token(result_delete, ['status'])
        Сhecking.check_json_value(result_delete, 'status', 'OK')

        print("Метод GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Сhecking.check_status_code(result_get, 404)
        Сhecking.check_json_token(result_get, ['msg'])
        Сhecking.check_json_search_in_value(result_get, 'msg', 'failed')

        print("Тестирование создания, изменения и удаления новой локации прошло успешно !!!")
