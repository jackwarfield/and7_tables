import subprocess as sp

def main():
  sp.call('mkdir -p fits/1', shell=True,)
  sp.call('mkdir fits/2', shell=True,)

  sp.call(['sh', 'fits1.sh'])
  sp.call(['sh', 'fits2.sh'])

  return 0

if __name__ == '__main__':
  raise SystemExit(main())
