class CellPhone:
    def __init__(self, manufact, model, rp):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = rp

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, rp):
        self.__retail_price = rp

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
