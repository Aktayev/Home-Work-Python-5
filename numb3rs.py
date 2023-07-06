import re
import sys


def main():
    ip = validate((input("IP: ")))
    print(ip)

# def validate(ip):
#     try:
#         i_1, i_2, i_3, i_4 = ip.split(".")
#         i_1=int(i_1)
#         i_2=int(i_2)
#         i_3=int(i_3)
#         i_4=int(i_4)
#         if i_1 <=255 and i_2 <=255 and i_3 <=255 and i_4 <=255:
#             return("True")
#         else:
#             return("False")
#     except ValueError:
#         return("False")


def validate(ip):
    try:
       if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip, re.IGNORECASE):
            ip_g1= int(matches.group(1))
            ip_g2= int(matches.group(2))
            ip_g3= int(matches.group(3))
            ip_g4= int(matches.group(4))
            if ip_g1 <=255 and ip_g2 <= 255 and ip_g3 <= 255 and ip_g4 <= 255:
                return True
            else:
                return False
       else:
           return False

    except ValueError:
        return False

if __name__ == "__main__":
    main()
