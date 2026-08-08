from src.controllers.pet_deleter_controller import PetDeleterController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.params["name"]
        self.__controller.delete(name)
        return HttpResponse(status_code=204)