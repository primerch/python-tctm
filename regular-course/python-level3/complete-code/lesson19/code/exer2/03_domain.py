import socket


def getIpAddr(domain):
    try:
        ipAddr = socket.gethostbyname(domain)
        return ipAddr
    except:
        print(f"{domain}的域名不存在！")


domain = input("请输入域名：")
ipAddr = getIpAddr(domain)
print(f"{domain} 的IP地址是：{ipAddr}")
