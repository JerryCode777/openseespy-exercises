import openseespy.opensees as ops
import opsvis as vis
import matplotlib.pyplot as plt

m = 1
kg = 1
s = 1

N = kg * m / s**2
kgf = 9.81 * N
cm = 0.01 * m

g = 9.81 * m / s**2

ops.wipe()
ops.model('Basic','-ndm',3, '-ndf',6)

#nodos
ops.node(1, 0, 0, 0)
ops.node(2, 6, 0, 0)

ops.fix(1, 1, 1, 0, 0, 0, 0)
ops.fix(1, 0, 0, 1, 0, 0, 0)

ops.geomTransf('Linear', 9, *[0,-1,0])

ops.element('elasticBeamColumn', 1, 1, 2, 2.0,15000, 1, 1, 2, 2, 9)

vis.plot_model(fig_wi_he=(20.,15.))
ele_shapes = { 1: ['rect',[1., 2.]]}
vis.plot_extruded_shapes_3d(ele_shapes,fig_wi_he=(40., 30.))
plt.show()