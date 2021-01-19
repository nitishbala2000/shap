This is a fork of the popular [shap](https://github.com/slundberg/shap/) repository, **not** intended
be merged to the main repository. I am altering shap for one of my own projects. The changes made are: 
allow for the passing of a matplotlib axes object to the **shap.plots.bar**, **shap.summary_plot**, **ahap.dependence_plot** 
and **shap.force_plot** plot functions in order to make them thread-safe

This can be used in a project via `pip install git+https://github.com/nitishbala2000/shap.git`