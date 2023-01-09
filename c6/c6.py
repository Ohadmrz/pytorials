import datetime


class RavKav:

    rides = {'short': {'range': (0, 15), 'price': 5.5},
             'medium': {'range': (16, 40), 'price': 12},
             'long': {'range': (40, 1000), 'price': 40},
             }

    def __init__(self, holder_id, holder_name):
        self.__holder_id = holder_id
        self.__holder_name = holder_name
        self.__balance = 0
        self.__log_date = {}
        self.__log_types = {}

    def get_holder_id(self):
        return self.__holder_id

    def get_holder_name(self):
        return self.__holder_name

    def topup(self, amnt):
        if amnt > 0:
            self.__balance += amnt

    @staticmethod
    def _km2type(km) -> str:
        for ride_type, ride_details in RavKav.rides.items():
            if ride_details['range'][0] <= km <= ride_details['range'][1]:
                return ride_type

    def ride(self, km, date: datetime.date = datetime.date.today()):
        ride_type = self._km2type(km)
        price = self.rides[ride_type]['price']
        if self.__balance < price:
            return False

        self.__balance -= price

        if date not in self.__log_date:
            self.__log_date[date] = 0

        self.__log_date[date] += 1

    def get_rides_by_date(self, date: datetime.date):
        return self.__log_date.get(date)



if __name__ == '__main__':
    rav_kav = RavKav(123456, "aaa")
    rav_kav.topup(100)
    rav_kav.ride(20)
    rav_kav.ride(30)
    print(rav_kav.get_rides_by_date(datetime.date.today()))








