class Bus:
    __driverName=''
    __busNum=''
    __routeNum=0
    __model=''
    __year=0
    __milage=0

    def __init__(self, driverName0, busNum0, routeNum0, model0, year0, milage0):
        self.__driverName = driverName0
        self.__busNum = busNum0
        self.__routeNum = routeNum0
        self.__model = model0
        self.__year = year0
        self.__milage = milage0
        print 'New object created!'

    def get_driverName(self):
        return self.__driverName
    def get_busNum(self):
        return self.__busNum
    def get_routeNum(self):
        return self.__routeNum
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def get_milage(self):
        return self.__milage

    def busAge(self,currYear=2019):
        return currYear - self.get_year()


def busInfoOut(i):
    print str(busPark[i].busAge()) + ' years old bus'
    print 'Driver name: ' + busPark[i].get_driverName()
    print 'Bus Num: ' + busPark[i].get_busNum()
    print 'Bus Year: ' + str(busPark[i].get_year())
    print '---------------'

i=0
busPark =  [Bus('Ivanov I.I.', '1234 AA-7', 1, 'MAZ216', 2010, 40000),
    Bus('Andreev A.D', '1221 MA-7', 73, 'MAZ103', 2008, 72000),
    Bus('Nikitin M.D', '3244 OP-7', 91, 'MAZ105', 2002, 240000),
    Bus('Sergeev S.S.', '5435 AC-7', 1, 'MAZ216', 2011, 40000),
    Bus('Pavlov A.P', '0210 PP-7', 1, 'MAZ216', 2016, 72000),
    Bus('Artemov B.B', '2313 TO-7', 29, 'MAZ103', 2001, 440000),
    Bus('Denisov I.T.', '4323 EB-7', 1, 'MAZ105', 2019, 40000),
    Bus('Artemov R.A', '5688 TC-7', 91, 'MAZ216', 2017, 272000),
    Bus('Nastasieva N.C', '2322 MP-7', 29, 'MAZ103', 2009, 640000),
    Bus('Natalieva I.O.', '9930 PE-7', 100, 'MAZ216', 2011, 30000),
    Bus('Vodilov F.A', '1121 IK-7', 100, 'MAZ105', 2013, 732000)]

routeNum=0
termNum=0

routeNum = int(input('Vvedite nomer marshruta \n'))

while i < len(busPark):
    if busPark[i].get_routeNum() == routeNum:
        busInfoOut(i)
    i+=1
i=0
termNum = int(input('Vvedite cpok ekspluatacii \n'))
while i < len(busPark):
    if busPark[i].busAge() > termNum:
        busInfoOut(i)
    i+=1