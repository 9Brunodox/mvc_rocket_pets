from  src.controllers.pet_deleter_controller import PetDeleterController

def test_delete_pet(mocker):
    mocker_repository = mocker.Mock()
    controller = PetDeleterController(mocker_repository)
    controller.delete("Buddy")

    mocker_repository.delete_pet.assert_called_once_with("Buddy")