host = '45.9.43.17'
user = 'root'
secret = 'fZ^xh6a4#FYV'
port = 22
import paramiko

# Update the next three lines with your
import time
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=secret)
channel = client.invoke_shell()
time.sleep(0.2)
channel.send("cd ../balancer\n")
time.sleep(0.1)
def send_tg(error):
    print(error, "error")
def  append_user_to_balancer(user_id, user_setiings):
    channel.send("\n")
    buf = channel.recv(100000).decode()
    channel.send("python3 main.py\n")
    time.sleep(0.1)
    time.sleep(0.1)
    channel.send("1\n")
    time.sleep(0.2)
    channel.send(user_id + "\n")
    time.sleep(0.2)
    buf = channel.recv(100000).decode()
    print(buf)
    if "error_code" in buf:
        for i in buf.split("\n"):
            if "error_code" in i:
                print(i)
    else:
        print("ok")
    # channel.send("\x01")
    # time.sleep(0.1)
    # channel.send("\x04")
    time.sleep(0.5)
def  append_balancer(balancer_id):
    channel.send("\n")
    buf = channel.recv(100000).decode()
    channel.send("python3 main.py\n")
    time.sleep(0.1)
    time.sleep(0.1)
    channel.send("3\n")
    time.sleep(0.2)
    channel.send(balancer_id + "\n")
    time.sleep(0.2)
    buf = channel.recv(100000).decode()
    print(buf)
    print("ok")
    # channel.send("\x01")
    # time.sleep(0.1)
    # channel.send("\x04")
    time.sleep(0.5)
def  get_col():
    channel.send("\n")
    time.sleep(0.1)
    buf = channel.recv(100000).decode()
    channel.send("python3 main.py\n")
    time.sleep(0.1)
    time.sleep(0.1)
    channel.send("2\n")
    time.sleep(0.2)
    buf = channel.recv(100000).decode()
    print(buf)
    # channel.send("\x01")
    # time.sleep(0.1)
    # channel.send("\x04")
    time.sleep(0.1)
append_balancer("balancer5.txt")
get_col()
for i in range(10000, 1000000):
    append_user_to_balancer("mark" + str(i), [])
get_col()
for i in range(100):
    pass
    # try:
    #     append_user_to_balancer("marker" + str(i), [])
    # except Exception as e:
    #     send_tg(str(e))
    # try:
    #     get_col()
    # except Exception as e:
    #     send_tg(str(e))

# _stdin, _stdout,_stderr = client.exec_command("df")
# print(_stdout.read().decode())
client.close()
# from paramiko import SSHClient
# import paramiko
# import time
# client = SSHClient()
# # client.load_system_host_keys()
# client.connect(host, username=user, password=secret)
# channel = client.get_transport().open_session()
# print(channel)
# shell = channel.invoke_shell()
# commands = [
#     "screen",
#     "python3 ../fol/main.py"
# ]
# for cmd in commands:
#     shell.send(cmd + "\n")
#     out = shell.recv(1024)
#     print(out)
#     time.sleep(1)
# client.close()
