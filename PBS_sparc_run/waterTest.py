from sparc.sparc_core import SPARC
from ase.build import molecule
from ase.units import kJ, mol
hvalue = [.2,.16,.14,.12]
for x in hvalue:
	water = molecule('H2O')
	hydrogen = molecule('H2')
	oxygen = molecule('O2')
	water.cell = [[6,0,0],[0,6,0],[0,0,6]]
	water.center()
	hydrogen.cell = [[6,0,0],[0,6,0],[0,0,6]]
	hydrogen.center()
	oxygen.cell = [[6,0,0],[0,6,0],[0,0,6]]
	oxygen.center()

	calc1 = SPARC(KPOINT_GRID=[1,1,1],
		 h = x,
            	 EXCHANGE_CORRELATION = 'GGA_PBE',
            	 TOL_SCF=1e-5,
            	 RELAX_FLAG=1,
            	 PRINT_FORCES=1,
            	 PRINT_RELAXOUT=1)
	water.set_calculator(calc1)
	hydrogen.set_calculator(calc1)
	oxygen.set_calculator(calc1)
	h2oPot = water.get_potential_energy()
	h2Pot = hydrogen.get_potential_energy()
	o2Pot = oxygen.get_potential_energy()
	print('Grid Spacing: ', x)
	print('H2O Potential Energy (eV): ',  h2oPot)
	print('H2 Potential Energy (eV): ',  h2Pot)
	print('O2 Potential Energy (eV): ',  o2Pot)
	total = h2Pot + .5 *  o2Pot -  h2oPot
	print('Reaction Energy 1 mol H2O (eV): ', total)
	print('Reaction Energy 2 mol H2O (eV): ', 2* total)
	kJTotal = total * mol / kJ
	print('Reaction Energy (kJ/mol): ', kJTotal)
	print('Percent Error: ', 100 * ((kJTotal - 285.8261)/285.8261))
