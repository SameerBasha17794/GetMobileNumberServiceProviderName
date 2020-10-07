import phonenumbers
from phonenumbers import carrier, NumberParseException


def get_service_provider_name():
    mobile_num = input("Enter Mobile Number with Country Code : ")
    try:
        service_provider = phonenumbers.parse(mobile_num)
        return carrier.name_for_number(service_provider, "en")
    except NumberParseException:
        return "Please Enter Country Code"
    except Exception as ex:
        return ex


print(get_service_provider_name())
