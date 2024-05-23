class Admin:
    def __init__(self,name,email,address,designation) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.designation=designation
        self.__Id=None



    @property
    def Id_num(self):
        return self.__Id
    
    @Id_num.setter
    def Id_num(self, value):
        self.__Id= value