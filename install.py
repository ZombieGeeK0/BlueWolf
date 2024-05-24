import os

def ckeck():
  if os.name == 'nt':
    os.system('chmod 777 linux.sh && chmod +x linux.sh && bash linux.sh')
  else:
    os.system('start windows.bat')

check()
