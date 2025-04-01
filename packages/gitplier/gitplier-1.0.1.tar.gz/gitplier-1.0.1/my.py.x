import gitomatic
import sys

#def output(s):
#    sys.stdout.write(s)
#    sys.stdout.flush()

repo = gitomatic.Repository('/home/jbenc/git/rhkernel-docs')
#repo.fetch('rhel', progress=output)
c = repo.merge_base('main', 'ci-container')
print(c)

repo = gitomatic.Repository('/home/jbenc/git/rhel9')
c = repo.merge_base('RHEL-9.1.0', 'RHEL-9.2.0')
print(c)
c = repo.describe('HEAD')
print(c)
c = repo.describe('HEAD', long=True)
print(c)
