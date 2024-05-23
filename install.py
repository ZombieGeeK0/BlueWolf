import os

def ckeck():
  if os.name == 'nt':
    os.system('bash linux.sh')
  else:
    os.system('start windows.cmd')

check()
