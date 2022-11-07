# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:47:42 2022

@author: lection
"""
import openseespy.opensees as ops

# ------------------------------
# Start of model generation
# -----------------------------

#        number of dimensions   number of dofs: set up a model
#ops.model('basic', '-ndm', ndm, '-ndf', ndf=ndm*(ndm+1)/2)
ops.model('basic', '-ndm', 2, '-ndf', 3)

#         nodal coordinates.
#ops.node(nodeTag, *crds, '-ndf', ndf, '-mass', *mass, '-disp', *disp, '-vel', *vel, '-accel', *accel)
ops.node(2, 144.0,  0.0)

#ops.element(eleType, eleTag, *eleNodes, *eleArgs)
#eleType = 'Truss'
#eleTag = 1
#eleNodes = [iNode, jNode]
#eleArgs = [A, matrixTag]
ops.element("Truss",1,1,4,10.0,1)

#uniaxialMaterial(matType, matTag, *matArgs)
#matArgs = [Fy, E0, b]
ops.uniaxialMaterial("Elastic", 1, 3000.0)

#ops.fix(nodeTag, *constrValues)
#constrValues: 0 free,1 fixed
ops.fix(1, 1, 1)

#represents the relationship between t and the load factor applied to the loads, λ, 
#λ=F(t).
#ops.timeSeries(tsType, tsTag, *tsArgs)
#timeSeries('Linear', tag, '-factor', factor=1.0, '-tStart', tStart=0.0)
ops.timeSeries("Linear", 1)

#pattern(patternType, patternTag, *patternArgs)
#Each LoadPattern in OpenSees has a TimeSeries associated with it
#                       constant factor
ops.pattern("Plain", 1, 1)

# Create the nodal load - command: load nodeID xForce yForce
#ops.load(nodeTag, xForce, yForce)
ops.load(4, 100.0, -50.0)

# ------------------------------
# Start of analysis generation
# ------------------------------

#system(systemType, *systemArgs)
#This class is used for symmetric positive definite matrix systems which have a banded profile. 
#The matrix is storedin a 1 dimensional array
#size:(bandwidth/2) times the number of unknowns
ops.system("BandSPD")

#A Plain numberer just takes whatever order the domain gives it nodes and numbers them.
#this ordering is both dependent on node numbering and size of the model.
ops.numberer('Plain')

#             Load factor increment λ.           optional
#integrator('LoadControl', incr, numIter=1, minIncr=incr, maxIncr=incr)
ops.integrator("LoadControl", 1.0)

#construct a SolutionAlgorithm object
#Determines the sequence of steps taken to solve the non-linear equation.
#algorithm('Linear', secant=False, initial=False, factorOnce=False)
ops.algorithm("Linear")

#analysis(analysisType)
#'Static'- for static analysis
#'Transient'- for transient analysis constant time step
#'VariableTransient' - for transient analysis with variable time step
#'PFEM' - for PFEM analysis.
# create analysis object
ops.analysis("Static")

#Eigen value analysis.
#eigen(solver='-genBandArpack', numEigenvalues)

#analyze(numIncr=1, dt=0.0, dtMin=0.0, dtMax=0.0, Jd=0)
#numIncr (int)	Number of analysis steps to perform. (required except for PFEM analysis)
#dt (float)	Time-step increment. (required for Transient analysis and VariableTransient analysis.`)
#dtMin (float)	Minimum time steps. (required for VariableTransient analysis)
#dtMax (float)	Maximum time steps (required for VariableTransient analysis)
#Jd (float)	Number of iterations user would like performed at each step.
# perform the analysis
ops.analyze(1)