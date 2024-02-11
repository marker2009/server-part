host = '45.9.43.17'
username = 'root'
secret = 'fZ^xh6a4#FYV'
port = 22
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, secret)

sftp = ssh.open_sftp()

path = "/fol/work/s_nam/rs.pkl"
localpath = "globalsave.pkl"
sftp.put(localpath, path)

sftp.close()
ssh.close()
