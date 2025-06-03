import openseespy.opensees as ops
import matplotlib.pyplot as plt
import opsvis as vis

#unidades base
m = 1
kg = 1
s = 1

#otras unidades 
N = kg/m*s**2
kgf = 9.81 * N
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



#aplicar la carga puntual en el centro
ops.node(3, 3.0, 0.0)
#elimino el anterior elemento para crear dos 
ops.remove('element', 1)
#creamos dos elementos
ops.element('elasticBeamColumn', 1, 1, 3, Area, E, I, 1) #el ultimo 1 es el tag de la tranformacio ngeometrica
ops.element('elasticBeamColumn', 2, 3, 2, Area, E, I, 1) #el ultimo 1 es el tag de la tranformacio ngeometrica

#listo ahora observamos de nuevo el modelo
vis.plot_model(fig_wi_he=(20., 15.))
plt.show()


#definimos la carga puntual
P = -1000 * N
# aplicamos la fuerza
ops.timeSeries('Linear', 1)
ops.pattern('Plain', 1, 1)
ops.load(3, 0, P*kgf, 0)

# realizamos el analisis
ops.wipeAnalysis()
ops.constraints('Plain')
ops.numberer('Plain')
ops.system('FullGeneral')
ops.algorithm('Linear')
ops.integrator('LoadControl',1)
ops.analysis('Static')
ops.analyze(1)

vis.plot_defo(5,fig_wi_he=(20., 15.))
plt.show()

disp = ops.nodeDisp(3)
print("vector desplazamiento: ")
print(disp)

#--------------------- codigo para graficar la fuerza
vis.plot_loads_2d(
    nep=17,
    sfac=False,
    fig_wi_he=False,
    fig_lbrt=False,
    fmt_model_loads={'color': 'black', 'linestyle': 'solid',
                     'linewidth': 1.2, 'marker': '', 'markersize': 1},
    node_supports=True,
    truss_node_offset=0.0,
    ax=None
)
plt.show()
#-----------------------

Ew = {} #diccionario vacio, para graficar todo el modelo
sfac = 0.0003 #factor de escala para el diagrama

sfacN, sfacV, sfacM = 5.e-5, 5.e-5, 5.e-5

vis.section_force_diagram_2d('N', sfacN)
plt.title('Axial force distribution')

vis.section_force_diagram_2d('T', sfacV)
plt.title('Shear force distribution')

vis.section_force_diagram_2d('M', sfacM)
plt.title('Bending moment distribution')

plt.show()






