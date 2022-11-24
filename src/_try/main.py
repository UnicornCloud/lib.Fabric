import hyperion
# from fabric import *
from fabric import Connection

host = "192.168.121.15"
user = "vagrant"
port = 22
config = ""
key_filename = "/home/me/.uni/hyperion/vagrant/instance/wordpress/.vagrant/machines/default/libvirt/private_key"


def connection():
    return Connection(host=host, user=user, connect_kwargs={"key_filename": key_filename})


con1 = connection()

con1.run("whoami")

hyperion.pci_info()