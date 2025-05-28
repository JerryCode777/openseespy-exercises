import openseespy.opensees as ops
import matplotlib.pyplot as plt
import opsvis as vis

#unidades base
m = 1
kg = 1
s = 1

#otras unidades 
N = kg/m*s**2
cm = 0.01 
Pa = N/m**2
MPa = 10e6 * Pa

#contantes fisicas
g = 9.81 * m / s**2

#materiales
fc = 210 * kg/cm**2
E = 15000 * fc ** 0.5
G = 0.5*E/(1+0.2)


ops.wipe()
ops.model('Basic', '-ndm', 2, '-ndf', 3)

#nodos
ops.node(1, 0.0, 0.0)
ops.node(2, 6.0, 0.0)

ops.fix(1,1,1,0)
ops.fix(2,0,1,0)
#section
b, h = 30*cm, 60*cm
Area = b * h
I = b * h**3 /12


#transformacion geometrica
ops.geomTransf('Linear', 1)

ops.element('elasticBeamColumn', 1, 1, 2, Area, E, I, 1) #el ultimo 1 es el tag de la tranformacio ngeometrica

#ploteo del modelo
vis.plot_model(fig_wi_he=(20., 15.))
plt.show()







