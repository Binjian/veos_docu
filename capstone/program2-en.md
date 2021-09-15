<!-- pandoc program2-en.md --pdf-engine=xelatex -o program2-en.pdf -V CJKmainfont='Source Han Sans SC' --wrap=preserve -->
<!-- pandoc program2-en.md -o program2-en.docx -V CJKmainfont='Source Han Sans SC' --wrap=preserve --reference-doc='SAMPLE-proposal.docx'y -->
<!-- ---
开放仿真环境下能效优化系统的评估和改进
... -->


<!-- markdownlint-disable-file MD013 -->

# Evaluation and improvement of Vehicle energy optimization system in open-ended simulation environment

## sponsor

- Company sponsor: Charles Huang (CEO) & Jason Fu (CTO), Newrizon
- Company mentor: Binjian Xin, Newrizon


## Background

Collaboration between UM-SJTU Joint Institute and Newrizon VerTEx lab.

- VerTEx proactively joined this program
- VerTEx will assign dedicated engineer as a mentor
- Students need to discuss with the mentor on the tasks and deliverables

Newrizon VerTEx lab
- Newrizon AI lab under Intelligent Technical System
- A dedicated group at Newrizon working on apply artificial intelligence in vehichle energy optimization systems.


Vehicle energy optimization system (VEOS) is the optimal motion planning system of EV system based on the vehicle motion states and driver input. Since its decision is based on the observation of the ego vehicle, it's necessary to evaluate the function and performance on diverse road conditions and conduct improvements following the evaluation accordingly. The real massive road test is obviously an indispensable way for this purpose, while the application of the simulation technology for typical test scenarios is a convenient and cost-efficient method to early issue discovery and analysis. Furthermore, making use of virtual computing platform, the system can even be improved and validated. 

Besides, the design, development and verification of VEOS are usually based on several test scenarios, its function and performance need to be evaluated when the scenarios deviates from the targeted ones. Through the simulation platform, one can configure diverse road environments, road static or dynamic properties. Thus the designed functions can be validated on its generalization capability.

### Purpose 

This project aims to set up an open-ended simulation environment in which the road topology and geometric properties like road length, curvation, elevation etc. as well as dynamic objects on the road can be configured or pre-programmed. In such environment the generalization capability, overfitting property, safety and multiagent behavior will be investigated and verified as pre-requisite before the feature release in SOP.

### Expected Deliverables 

1. Set up the open-ended road simulation system:

- Generate road network with randomly sampled curvature and connection topology
- Generate Non-Play-Character object vehicles with pre-programmed motion trajectories
- Generate autonmous driving object vehicles with pre-trained baseline reinforcement learning agents
- Spawn object vehicles on the map
- Spawn ego vehicles with VEOS
  
2. Evaluate the function and performance index of VEOS through the simulation platform 
- Collect data through simulation platform and train the VEOS system
- Evaluate the generalization capability of VEOS under diverse road conditions
- Evaluate the safety property for vehicles with VEOS, for example crash, traffic rules impediments
- Evaluate the competetive and cooperative behavior of the multi-agent system sharing the same VEOS strategy

3. Propose improvement of VEOS based on the simulation results. Implement the improvement proposals in the simulation platform by retrain the veos system with validation.
- collect and analyse the simulation data
- collect some actual road test result and compare them with simulation results.

|![](fig/panel.jpg){width=400pix}|
|:--:|
|<b>Open-ended Driving Simuation System</b>|


## Team 

Students with the following knowledge and skills are encouraged to apply:

- Vehicle motion control 
- Basic knowledge in deep reinforcement learning
- Programming skills
  - Python
  - Tensorflow or Pytorch is a plus
  - Basic Linux knowledge


## Benefit to Students:

- Access to most up-to-date electric commercial vehicle platform
- Learn state of the art deep learning applications in the EV industry 
- Get in-depth knowledge on deep reinforcement learning
- Gain experience in a fast-growing startup enterprise 
