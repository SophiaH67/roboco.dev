import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()


with open("nginx.conf.dist", "r") as f:
    nginx_conf = f.read()

    nginx_conf = nginx_conf.replace("{{ip}}", ip)

    with open("nginx.conf", "w") as f:
        f.write(nginx_conf)
