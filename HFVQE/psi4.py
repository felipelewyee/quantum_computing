import psi4
mol = psi4.geometry("""
  H    0.0000000    0.0000000    0.0000000
  H    0.0000000    0.0000000    1.3000000
  H    0.0000000    0.0000000    2.6000000
  H    0.0000000    0.0000000    3.9000000
  H    0.0000000    0.0000000    5.2000000
  H    0.0000000    0.0000000    6.5000000
symmetry c1
""")

# Set computation options
psi4.set_options({'basis': 'sto-3g'})

wfn = psi4.core.Wavefunction.build(mol, psi4.core.get_global_option('basis'))
mints = psi4.core.MintsHelper(wfn.basisset())

# OEI
S = np.asarray(mints.ao_overlap())
T = np.asarray(mints.ao_kinetic())
V = np.asarray(mints.ao_potential())
H = T + V

# Build ERI Tensor
I = np.asarray(mints.ao_eri())
