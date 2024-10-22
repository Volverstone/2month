class Computer:

    def __init__(self,memory,cpu):
        self.__memory = memory
        self.__cpu = cpu

    def __str__(self):
        return f'CPU: {self.__cpu}, memory: {self.__memory}'

    @property
    def memory(self):
        return (self.__memory)

    @property
    def cpu(self):
        return (self.__cpu)

    @memory.setter
    def memory(self,value):
        self.__memory = value

    @cpu.setter
    def cpu(self,value):
        self.__memory = value


    def make_computations(self):
        return self.__memory * self.__cpu

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory


class Phone:
    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list

    def __str__(self):
        return f'sim_card_list: {self.__sim_card_list}'

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self,value):
        self.__sim_card_list = value

    def call(self,sim_card_number, call_to_number):

        if sim_card_number == 1:
            return (f" Идет звонок на номер {call_to_number} с сим карты - {sim_card_number} - {self.__sim_card_list[0]}")

        elif sim_card_number == 2:
            return (f" Идет звонок на номер {call_to_number} с сим карты - {sim_card_number} - {self.__sim_card_list[1]}")

class Smartphone(Computer,Phone):

    def __init__(self,memory,cpu,sim_card_list):
        Computer.__init__(self,memory,cpu)
        Phone.__init__(self, sim_card_list)




    def use_gps(self,location):
        print (f"чтобы дойти до {location}, сядтье на автобус 51\n"
                f"выйти на остановке 'Третьяковской'\n"
                f"пройти на восток по улице 'Койбагарова'\n"
                f"на перекрестке пройти налево. Вы подшли до пункта назначения {location}")
    def __str__(self):
        return super().__str__() + f' ,sim_card_list: {self.sim_card_list}'



acer = Computer(64, 16)
nokia = Phone(["Beeline", "Megacom"])
pocox3 = Smartphone(32, 8, ["O","Megacom" ])
iphone = Smartphone(86, 6, ["Beeline", "Megacom"])


print(acer)
print(nokia)
print (pocox3)
print(iphone)


pocox3.use_gps("Спорт зал 'ЛЕОНИК'") #funs use_gps
print(f'func make_computations : {acer.make_computations()}') #func make_computations
print(nokia.call(1, "+9969997120220"))#Beeline
print(nokia.call(2, "+9969997120220"))#Megacom

#здесь я решил сильно не заморачиваться т.к. спешу
#до дедлайна в 2 просто не успеваю
print(acer > iphone) #__gt__ func
print(acer < iphone) #__lt__ func
print(iphone <= pocox3) #__le__ func
print(acer >= pocox3) #__ge__ func
print(pocox3 != acer) #__ne__ func
print(iphone == iphone) #__eq__ func






