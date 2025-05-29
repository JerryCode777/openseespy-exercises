import openseespy.opensees as ops
import opsvis as vis 
import matplotlib.pyplot as plt

#unidades base
m = 1
kg = 1
s = 1

#otras unidades
N = kg * m / s**2
cm = 0.01 * m
Pa = N / m**2
MPa = 10e6 * Pa
kgf = 9.81 * N

#constantes
g = 9.81 * m /s**2

# materiales
fc = 210 *kgf/ cm**2
E_mod = 150*fc**0.5*kgf/cm**2
G_mod = 0.5*E_mod/(1+0.2)

b = .3
h = .6
Area = b * h
Iz = b * h **3 / 12
Iy = b ** 3 * h / 12

aa, bb = max(b,h),min(b,h)
beta= 1/3-0.21*bb/aa*(1-(bb/aa)**4/12)
jxx = beta*bb**3*aa

ops.wipe()
ops.model('Basic', '-ndm', 3, '-ndf', 6)

ops.node(1, 0, 0, 0)
ops.node(2, 5.0, 0, 0)

ops.fix(1,*[1,1,1,0,0,0])
ops.fix(2,*[0,1,0,0,0,0])

ops.geomTransf('Linear',1, *[0,1,0])

ops.element('elasticBeamColumn', 1, 1, 2, Area, E_mod, G_mod, jxx, Iy, Iz, 1)

vis.plot_model(fig_wi_he=(20.,15.))
ele_shapes = {1: ['rect', [b, h]],#'circ', [b]],

              2: ['rect', [b, h]],
              3: ['rect', [b, h]]}#'I', [b, h, b/6., h/10.]]}
vis.plot_extruded_shapes_3d(ele_shapes,fig_wi_he=(40., 30.))
plt.show()


