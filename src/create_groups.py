import matplotlib.pyplot as plt
import illustris_python.groupcat as gc
import numpy as np

basePath = "/hpcfs/home/ciencias/fisica/docentes/je.forero/Illustris-1/"

subhalo_fields = ['SubhaloMass','SubhaloSFRinRad']
subhalos = gc.loadSubhalos(basePath,135,fields=subhalo_fields)

halo_fields = ['GroupFirstSub', 'Group_M_Crit200', 'GroupNsubs']
halos = gc.loadHalos(basePath, 135, fields=halo_fields)

for k in subhalos.keys():
    print(k)


for k in halos.keys():
    print(k)

mass_msun = halos['Group_M_Crit200'] * 1e10 / 0.704
n_in_halo = halos['GroupNsubs']

fig = plt.figure(1, figsize=(11,10))
plt.plot(mass_msun,n_in_halo, '.')

ax = plt.axes()
ax.set_xlim([1E9, 1E15])
ax.set_ylim([1, 1E5])

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Total Mass [$M_\odot$]')
plt.ylabel('N_substructures')
plt.savefig('test.png')
plt.gca().cla()
plt.close(fig)

log_mass_msun = np.log10(mass_msun)
mass_limit = log_mass_msun > 10.0
number_limit = n_in_halo > 2

fig = plt.figure(1, figsize=(11,10))
plt.hist(log_mass_msun[mass_limit], log=True, bins=np.linspace(10,15.0, 26.0), alpha=0.5, color='blue')


ax = plt.axes()
ax.set_xlim([10, 15])
ax.set_ylim([1, 1E5])
plt.xlabel('$\log_{10}$Total Mass [$M_\odot$]')
plt.ylabel('Number')
plt.savefig('test2.png')
plt.gca().cla()
plt.close(fig)

