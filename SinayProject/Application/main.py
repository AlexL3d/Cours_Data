from Get.NumberTrade import GetNumberTrade
from Get.ServiceLineCode import GetServiceLineCode
from Get.VesselsParticulars import GetVesselParticulars
from Get.ListCodes import ListAllCodes
from Get.Schedules import GetSchedules


#https://fr.python-requests.org/en/latest/user/quickstart.html

if __name__ == '__main__':

    ListeNumberTrade = GetNumberTrade()

    ServiceLineCode = GetServiceLineCode(ListeNumberTrade)

    VesselParticular = GetVesselParticulars(ServiceLineCode)

    ListCodes = ListAllCodes(VesselParticular)

    Schedules = GetSchedules(ListCodes)