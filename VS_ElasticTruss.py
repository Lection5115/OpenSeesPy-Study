# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:33:06 2022

@author: lection
"""
import openseespy.opensees as ops
import openseespyvis.Get_Rendering as opsplt

# wipe model
ops.wipe()
# create model
ops.model('basic', '-ndm', 2, '-ndf', 2)

ops.node(1, 0.0, 0.0)
ops.node(2, 144.0,  0.0)
ops.node(3, 168.0,  0.0)
ops.node(4,  72.0, 96.0)

ops.fix(1, 1, 1)
ops.fix(2, 1, 1)
ops.fix(3, 1, 1)

ops.uniaxialMaterial("Elastic", 1, 3000.0)


ops.element("Truss",1,1,4,10.0,1)
ops.element("Truss",2,2,4,5.0,1)
ops.element("Truss",3,3,4,5.0,1)

# plot model
opsplt.plot_model()