

Efficiently creating optimization models
________________________________________________________________________

|PyPI version| |License|

.. |Supported Python Versions| image:: https://img.shields.io/pypi/pyversions/optlanghelper)
   :target: https://pypi.org/project/optlanghelper/
   :alt: Python versions

.. |PyPI version| image:: https://img.shields.io/pypi/v/optlanghelper.svg?logo=PyPI&logoColor=brightgreen
   :target: https://pypi.org/project/optlanghelper/
   :alt: PyPI version

.. |Actions Status| image:: https://github.com/freiburgermsu/optlanghelper/workflows/Test%20optlanghelper/badge.svg
   :target: https://github.com/freiburgermsu/optlanghelper/actions
   :alt: Actions Status

.. |License| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License

.. .. |Downloads| image:: https://pepy.tech/badge/modelseedpy
..    :target: https://pepy.tech/project/modelseedpy
..    :alt: Downloads


.. note::

   This project is under active development, and may be subject to losing back-compatibility.

----------------------
Installation
----------------------

OptlangHelper can be installed via ``pip`` through the ``PyPI`` channel::

 pip install optlanghelper


----------------------
Usage
----------------------

The OptlangHelper package is a collection of functions that make it easier to build linear programming models using the Optlang package.   This is accomplished through dictionaries of variables, constraints, and an objective that are added to a model at the end of iterating through all conditions.  Since each solver -- such as GLPK, CPLEX, and GUROBI -- differently defines variables and constraints, a separate class (although using the same function design and arguments) is provided for each of these solvers.  This requires the user to correctly select the proper OptlangHelper class that will construct the appropriate model for their solver.

****************
GLPK
****************

The GLPK class is used to construct an optlang model for the GLPK solver.  This is the simplest of the solvers and is employed by default for optlang without specification for CPlex or Gurobi.

++++++++++++++++++++++
Named Tuples
++++++++++++++++++++++

There are several NamedTuples that are defined in OptlangHelper and assist with defining variables, constraints, and the objective.

``Bounds`` object has attributes of 

- ``lb``, the lower bound of the entity associated with this bound:  default is 0.
- ``up``, the upper bound of the associated entity:  default is 1000.


``tupVariable`` object has attributes of 

- ``name``, the name of the variable represented by this tuple
- ``bounds``, the lower and upper limit bounds associated with the tuple: (0,1000) is the default
- ``type``, the variable type: "integer"; "binary"; "continuous" is the default.


``tupConstraint`` object has attributes of 

- ``name``, the name of the variable represented by this tuple
- ``bounds``, the lower and upper limit bounds associated with the tuple: (0,0) is the default
- ``expr``, the constraint expression: ``None`` is the default.


``tupObjective`` object has attributes of 

- ``name``, the name of the variable represented by this tuple
- ``expr``, the objective expression: ``None`` is the default.
- ``direction``, the optimization direction: "max" is the default.

All of the above objects are fed into the ``define_model`` function

- ``model_name``, the name of the model
- ``variables``, the tupVariable objects for the model.
- ``constraints``, the tupConstraint objects for the model.
- ``objective``, the tupObjective object for the model.
- ``optlang``, specifies whether an optlang model is returned (``True``), or the raw dictionary (``False``) by default.

This function calls all of the class functions and returns either the GLPK model as as dictionary or an optlang object.


++++++++++++++++++++++
Example
++++++++++++++++++++++

 The following blocks define the intended usage of the GLPK class.


.. code-block:: python

 from optlanghelper import tupVariable, tupConstraint, tupObjective, define_model

 # define the variables
 variables = {}
 for var in vars:
     variables[var.name] = tupVariable(var.name, Bounds(0, 5), "continuous")
     variables[var.name+"_bin"] = tupVariable(var.name+"_bin", Bounds(0, 1), "binary")

 # define the constraints
 constraints = {}
 for name, content in constraint_info.items():
    lb, ub = content["low_bound"], content["high_bound"]
    consExpr = {}
    ## define the constraint expression
    for varName, coef in var_info.items():
        if varName not in consCoefs:  continue
        coef2 = consCoefs[varName]
        consExpr[varName].update({"elements": [varName, coef2], "operation": "Mul"})
    ## create the constraint tuple
    constraints[nutrient] = tupConstraint(name=nutrient, bounds=Bounds(lb, ub), expr={"elements": list(consExpr.values()), "operation": "Add"})

 for varName in var_info.keys():
    constraints[varName+"_bin"] = tupConstraint(varName+"_bin", bounds=Bounds(0,None),
                                             expr={
                                                 "elements": [
                                                     variables[varName].bounds.ub,
                                                     {"elements": [-1, variables[varName].name,], "operation": "Mul"},
                                                     {"elements": [-variables[varName].bounds.ub, variables[varName+"_bin"].name], "operation": "Mul"}],
                                                "operation": "Add"})

 # define the objective
 objective = tupObjective("< optimization name>", [], "min")
 for varName, coef in var_info.items():
     objective.expr.append({
         "elements": [
             {"elements": [variables[varName].name, coef],
             "operation": "Mul"}],
         "operation": "Add"
     })

 # create an optlang model from all of the variables, constraints, and objective defined above
 model = define_model("< model name>", list(variables.values()), list(constraints.values()), objective, True)

