import numpy as np
import pylab as p

#design variables
#    hl.Mach_bypass = .95
#    hl.Mach_pod_max = .90
#    hl.Mach_c1_in = .65
#    hl.c1_PR_des = 13

#    #initial guesses
#    hl.compress.W_in = .35
#    hl.flow_limit.radius_tube = hl.pod.radius_tube_inner = 178
#    hl.compress.Ts_tube = hl.flow_limit.Ts_tube = hl.tube_wall_temp.tubeWallTemp = 322 
#    hl.compress.c2_PR_des = 5 

#Mach, Battery Energy, Comp Energy/s, Time

data = np.array([
[0.69999999999999996, 0.70999999999999996, 0.71999999999999997, 0.72999999999999998, 0.73999999999999999, 0.75, 0.76000000000000001, 0.77000000000000002, 0.78000000000000003, 0.79000000000000004, 0.80000000000000004, 0.81000000000000005, 0.82000000000000006, 0.83000000000000007, 0.84000000000000008, 0.85000000000000009, 0.8600000000000001, 0.87000000000000011, 0.88000000000000012, 0.89000000000000012, 0.90000000000000013, 0.91000000000000014, 0.92000000000000015, 0.93000000000000016],
[425.64734534294513, 419.65424475203628, 413.82772409685742, 408.16094022060747, 402.64742075574082, 397.28103790778948, 392.05598627110015, 386.96676904786113, 382.00815317806808, 377.1751865322513, 372.46316034132201, 367.86760002503087, 363.38424705208229, 359.00904154735571, 354.73813422797747, 350.56784050845937, 346.49464897789539, 342.51522233298749, 338.62635318664013, 334.82501553606085, 331.1082699045225, 327.47334674417999, 323.91756978015695, 320.43839279530488],
[345.33770199869105, 346.5392280454048, 347.77005182839076, 349.03173094706352, 350.32484572200718, 351.6500050517148, 353.00781977374407, 354.399264528071, 355.82499428958067, 357.28562569758549, 358.78210283805197, 360.31530103162191, 361.88440156468499, 363.49217031265931, 365.13789903116964, 366.82390861203487, 368.54951824043007, 370.31660813514264, 372.13130119605955, 373.97719159650512, 375.8732069051859, 377.81270605751422, 379.79821127671244, 381.83106344615129],
[2806.4660132501872, 2766.9510642991399, 2728.5344445946644, 2691.1710344215876, 2654.8181588290604, 2619.4354147766339, 2584.9845248643965, 2551.429246469414, 2518.7350758993498, 2486.8693617511071, 2455.8010571955297, 2425.500659505698, 2395.9400904532899, 2367.0925816309168, 2338.9327531514996, 2311.4363110447871, 2284.5801031509586, 2258.3421252724447, 2232.7012298020227, 2207.6374650729285, 2183.1314499199289, 2159.164923588, 2135.7202403087272, 2112.780611837175]
])

fig, ax = p.subplots()
# Twin the x-axis twice to make independent y-axes.
axes = [ax, ax.twinx(), ax.twinx()]
# Make some space on the right side for the extra y-axis.
fig.subplots_adjust(right=0.75)
# Move the last y-axis spine over to the right by 20% of the width of the axes
axes[-1].spines['right'].set_position(('axes', 1.2))
# To make the border of the right-most axis visible, we need to turn the frame
# on. This hides the other plots, however, so we need to turn its fill off.
axes[-1].set_frame_on(True)
axes[-1].patch.set_visible(False)
# And finally we get to plot things...
colors = ('Green', 'Red', 'Blue')
index = [1, 2, 3]

for i, ax, color in zip(index, axes, colors):
    if i == 1:
		ax.plot(data[0],data[1], color=color, lw=3)
		ax.set_ylabel('Battery Size (kW-hr)', color=color, fontsize = 18)
		ax.set_ylim([0,450])
    if i == 2:
		ax.plot(data[0],data[2], color=color, lw=3)
		ax.set_ylabel('Compressor Power Req (kW)', color=color, fontsize = 18)
		ax.set_ylim([0,450])
    if i == 3:
		ax.plot(data[0],data[3], color=color, lw=3)
		ax.set_ylabel('Total Mission Time', color=color, fontsize = 18)
		ax.set_ylim([0,3000])
    ax.tick_params(axis='y', colors=color)
axes[0].set_xlabel('Max Pod Mach', fontsize=18)

#p.tick_params(axis='both', which='major', labelsize=15)

#p.ylabel('Battery', fontsize=18)
#p.title('Battery vs Max Pod Mach', fontsize=20)
#p.plot(data[0],data[1], label="Tube (c1MN = .65)", lw=3)
#p.xlim([0.65,0.95])
#p.ylim([0,450])
#ax2 = p.twinx()
#ax2.plot(data[0],data[3], label="Tube", lw=3)
#ax2.set_ylabel('Total time')
p.legend(loc="best")
    
#p.gcf().set_size_inches(11,5.5)
#p.gcf().savefig('test2png.png',dpi=130)
p.show()