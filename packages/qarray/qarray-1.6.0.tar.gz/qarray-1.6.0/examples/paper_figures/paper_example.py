import matplotlib.pyplot as plt

from qarray import DotArray, charge_state_changes

array = DotArray(
	Cdd=[
		[0.0, 0.1],
		[0.1, 0.0]
	],
	Cgd=[
		[1., 0.1],
		[0.1, 1]
	],
	algorithm="default",
	implementation="rust",
	charge_carrier="holes",
	T=0.0
)

# array.run_gui()


min, max, res = -4, 4, 400
# computing the ground state charge configurations
n = array.do2d_open("P1", min, max, res, "P2", min, max, res)
n_virtual = array.do2d_open("vP1", min, max, res, "vP2", min, max, res)
n_detuning_U = array.do2d_open("e1_2", min, max, res, "U1_2", min, max, res)
n_closed = array.do2d_closed("P1", min, max, res, "P2", min, max, res, n_charges=2)

fig, ax = plt.subplots(2, 2, figsize=(5, 5))
extent = (min, max, min, max)
ax[0, 0].set_title("Open")
ax[0, 0].imshow(charge_state_changes(n), origin="lower", cmap='Greys', extent=extent)
ax[0, 0].set_xlabel("P1")
ax[0, 0].set_ylabel("P2")

ax[0, 1].set_title("Virtual gates")
ax[0, 1].imshow(charge_state_changes(n_virtual), origin="lower", cmap='Greys', extent=extent)
ax[0, 1].set_xlabel("vP1")
ax[0, 1].set_ylabel("vP2")

ax[1, 0].set_title("Detuning - on-site energy")
ax[1, 0].imshow(charge_state_changes(n_detuning_U), origin="lower", cmap='Greys', extent=extent)
ax[1, 0].set_xlabel("$e_{12}$")
ax[1, 0].set_ylabel("$U_{12}$")

ax[1, 1].set_title("Closed (2 holes)")
ax[1, 1].imshow(charge_state_changes(n_closed), origin="lower", cmap='Greys', extent=extent)
ax[1, 1].set_xlabel("P1")
ax[1, 1].set_ylabel("P2")
plt.tight_layout()
plt.show()