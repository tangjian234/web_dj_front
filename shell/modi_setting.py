
import sys

setting_file_name = sys.argv[1]
app_name = sys.argv[2]

app_name = '\'' + sys.argv[2] + '\''

print(setting_file_name)

with open(setting_file_name, "r") as f:
    lines= f.readlines()
    f.close()

for i in range(0,len(lines)-1) : 
  if 'INSTALLED_APPS' in lines[i]:
    lines[i] = 'INSTALLED_APPS = [ ' +  app_name +',\n'
    print(lines[i])
  if 'ALLOWED_HOSTS = []' in lines[i]:
    lines[i]= "ALLOWED_HOSTS = [\'jian\',\'73.254.182.128\',\'127.0.0.1\']"
    print(lines[i])

with open(setting_file_name, "w") as f:
    f.writelines(lines)
    f.close()

