from src.controllers.person_finder_controller import PersonFinderController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.params["person_id"]
        body_response = self.__controller.find(person_id)
        return HttpResponse(status_code=200, body=body_response)