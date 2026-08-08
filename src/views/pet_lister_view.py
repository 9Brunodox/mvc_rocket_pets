from src.controllers.pet_lister_controller import PetListerController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PetListController(ViewInterface):
    def __init__(self, controller: PetListerController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self._controller.list()
        return HttpResponse(status_code=200, body=body_response)