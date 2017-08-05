import paramiko
import subprocess

results = { }
hosts = [ "10.0.1.44" ]

for host in hosts:
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
	client.connect(host)
	stdin, stdout, stderr = client.exec_command("ps awx | grep bash | grep -v grep")
	results[host] = stdout.readlines()
	client.close()

for host in results:
	print "%s == %s" % (host, ' '.join(line.rstrip() for line in results[host]))

results = { }

for host in hosts:
	c = subprocess.Popen(["ssh", host, "ps", "awx", "|", "grep", "bash", "|", "grep", "-v", "grep"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	results[host] = c.communicate()[0].split("\n")

for host in results:
	print "%s == %s" % (host, ' '.join(results[host]))