
class Service:
    def __init__(self,name:str, in_port:int, out_port:int) -> None:
        self.name = name
        self.in_port = in_port
        self.out_port = out_port
        

class Interface:
    pass

class Node:
    def __init__(self,id:int) -> None:
        self.id = id
        self.interfaces:list[Interface] = []
        self.time = 0
        self.services:list[Service] = []
