from  src.controllers.pets_delete_controller import PetsDeleteController

def test_delete_pet(mocker):
    mocker_repository = mocker.Mock()
    controller = PetsDeleteController(mocker_repository)
    controller.delete("Buddy")

    mocker_repository.delete_pet.assert_called_once_with("Buddy")