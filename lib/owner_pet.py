class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

    def get_pet_type(self):
        return self._pet_type 
    
    def set_pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception('no!')
        
    pet_type = property(get_pet_type, set_pet_type)
        
    

class Owner:

   

    def __init__(self, name): 
        self.name = name
        self.my_pets = []

    def pets(self):
        self.my_pets = []
        for pet in Pet.all:
            if pet.owner.name == self.name:
               self.my_pets.append(pet)
        return self.my_pets
    
    def add_pet(self, pet):
            if pet.pet_type in Pet.PET_TYPES:
                pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(Pet.all, key=lambda pet: pet.name)
        return sorted_pets

    
