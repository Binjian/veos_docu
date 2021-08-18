# VEOS by Data Driven Planning 
Prerequisite:
	- fixed test scenes 
	- No Air Conditioning
	- Round Trip (Elimniate topographic impact) 
## Expriement Results 
- baselines
	- driver styles analysis (analysis)
	- pedal map comparison
	- A2C
	- different initial map

- Declining in each epoch 
		- RL agent cooperative / Human driver adapting?
		- Epoch tendcy
			- declining in total loss / inclining in total reward
			- entropy declining / becoming more and more deterministic
			- expected wh declining
			- seems cooperative, at least no conflict 
 	- baseline: strong regen --> higher efficiency
 	- methods
 	- achievements
 	- status
- long-term in resume mode (model and table resumed)


- weak regen (fix coastdown / constrained action space)

- strong regen (exploit coastdown / relax action space)

## Analysis
weaker regen:  not stronger regen, but better motion control for the test case
	- possible models

- debug
	- tools
		- **driving style analysis (quantitative)**
		- vehicle interfaces and systems (stable and reliable)
		- synchronization
		- data logging (for analysis and offline algo)
			- energy consumpt cross-check by UDP messages
		- model resume
		- udp episodic analysis
		- debug (latency analysis)
		- verifying DL algo with cpu only resources
	- analysis
		- optimal motion planning
		- exploit regen
		- better assistance for manual motion control for eco 
		- reward shaping (penalize braking could be cooperative)
		- need recurrency to encode system dynamics

## Theory
- not like this: big data --> NN --> label ==> good result
- learn from data (distribution) not label (label is supervision)
	- distribution, law of large number n>30, (multiplicity with samples)
	- dynamic environment --> drifting distribution
	- **advantages**: previously impossible cases can be solved elegantly by big data.
- basic observability/controllability
	- observation enough? fully observable --> which should I observe?
	- control signal sufficient/efficient? 
	- long-term dependency
- Model
	- Complete observable model (MDP)
		- human driver model $Th=Th(\mathbf{O_h})$
		- pedal map $\tilde{PM}(Th)=Trq$
		- $Trq=\tilde{PM}\circ Th=\tilde{PM}(Th(O_h))$
		- $\mathbf{O_h}=(vel, road, objects)$
		- Objective: Optimal Motion Planning 
			- $\min_{Trq}(\Sigma_{i}(u\cdot i)\cdot dt)$
			- follow the optimal motion planning (follow the optimal speed curve) 
				- reduce unnecessary large torque
				- maintain a speed when regenerative brake occurs (exploit regenerative brake)
	- Implementation, POMDP
		- $\mathbf{O_{rl}}=(vel, Th)$
		- $\mathbf{O_{rlx}}=(vel, Th, MotionPlan)$

## Outlook
### fully autonomous
1. optimal motion control/prediction
2. exploit regen
### assistance system
1. fix driving style and analysis
2. different reward

### Challenge
动态过程未知，奖励不完全知道，并非简单将数据灌入神经网络,需要考虑几个因素。
 - sample efficiency 
 - offline data utilization
 - reward shaping
 - memory
### Counter measures 

