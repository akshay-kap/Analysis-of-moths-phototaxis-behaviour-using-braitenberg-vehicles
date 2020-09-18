# Analysis-of-moth's-phototaxis-behaviour-using-braitenberg-vehicles
- This project is carried out to observe emergent behavior of braitenberg vehicles mimicking moth's photo taxis behavior.
- The simulations were carried out in __webots using khepera's robot (II)__
- The controllers were written in python, the __controller folder__ features python files specific to given experiments(also text file featuring the trajectories are recorede in controllers folder)
  - The experiments focused on imitating "love" behaviour towards light as described by Baritenberg vehicles.
  - Data analysis by varying light intensivity, attraction coefficient towards light source, and repulsion coefficient among multiple agents is been done in python.
  - SVR and Linear regression models were used to comment on non-linear emergent behavior of the  multiple agents mimicing moth's phototaxis nature.

__Read : Report.pdf to understand the complete set up and the analysis carried out __

<br> The typical sensor units for Kaphera robots are shown as:
![khepera](/images/khepra.PNG)

<br> The starting of world view can be seen as:
![Initial World View](/images/simulation_world.PNG)

<br> The comparison of trajectories can be seen from the figure:
![Trajectory comparison with variation in coeffcient of inter - repulsion and attraction towards light](/images/path_comparison.PNG)
