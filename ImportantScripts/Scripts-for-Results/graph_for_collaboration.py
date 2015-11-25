#!/usr/bin/python
__author__ = 'eb'

import matplotlib.pyplot as plt


# baseline_ingress = [0, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
#                     4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
#                     4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
#                     4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
#                     4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
#                     4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
#                     4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
#                     4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
#                     4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
#                     4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8 ]
#
# baseline_egress = [0, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
#                    2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
#                    2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
#                    2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
#                    2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
#                    2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
#                    2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
#                    2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
#                    2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
#                    2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6 ]


# columns     = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sb1_ingress = [0, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 60, 60, 60, 60, 60, 60, 60, 60, 64,
               60, 60, 60, 80, 80, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 40, 40, 40, 40, 40, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 60, 60, 60, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]

sb1_egress = [0, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 40, 40, 40, 40, 40, 40, 40, 40, 46,
              40, 40, 40, 40, 40, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6]


sb2_ingress = [0, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 40, 40, 40, 40, 40, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 60, 60, 60, 60, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8 ]

sb2_egress = [0, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6 ]


sb3_ingress = [0, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 40, 40, 40, 40, 40, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 62, 60, 60, 60, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8 ]

sb3_egress = [0, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6 ]

cbta_ingress = [0, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 40, 40, 40, 40, 40, 40, 40, 40, 44,
               40, 40, 40, 40, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8  ]

cbta_egress = [0, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
               2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
               2, 2, 2, 30, 30, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
               2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
               2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
               2, 80, 80, 80, 80, 80, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
               2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
               2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
               2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6,
               2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6 ]

# Populate time series
time_series = [x for x in range(len(sb1_ingress))]

plt.figure(1)
plt.subplot(411)
# Plot the traffic average
sb1_ingress_plot, = plt.plot(time_series,
                            sb1_ingress,
                            linewidth=2,
                            label="SecureBox-1 Ingress",
                            linestyle='-',
                            color='crimson')

sb1_egress_plot, = plt.plot(time_series,
                           sb1_egress,
                           linewidth=2,
                           label="SecureBox-1 egress",
                           linestyle='--',
                           color='blue')

# Set plot's attributes
plt.xlim(min(time_series), max(time_series)+2)
plt.ylim(0, max(sb1_ingress)+5)

# Set legend
plt.legend([sb1_ingress_plot, sb1_egress_plot],
           ['Ingress Traffic', 'Egress Traffic'], fontsize=24)
plt.locator_params(nbins=20)

# set the annotations
ax = plt.gca()
# Event 1
ax.arrow(31, 0, 0, 55, head_width=2, head_length=5, fc='k', ec='k')
ax.text(22, 20, 'Event 1', fontsize=20)
# Event 2
ax.arrow(44, 0, 0, 75, head_width=2, head_length=5, fc='k', ec='k')
ax.text(44, 20, 'Event 2', fontsize=20)
# Event 2
ax.arrow(103, 0, 0, 35, head_width=2, head_length=5, fc='k', ec='k')
ax.text(103, 20, 'Event 3', fontsize=20)
# Event 5
ax.arrow(172, 0, 0, 55, head_width=2, head_length=5, fc='k', ec='k')
ax.text(172, 20, 'Event 6', fontsize=20)

# Set labels
# plt.xlabel('Time Series', fontsize=16)
plt.ylabel('Traffic kb/s', fontsize=24)
plt.title('SecureBox 1', fontsize=26)
plt.grid(True)



plt.subplot(412)
# Plot the traffic average
sb2_ingress_plot, = plt.plot(time_series,
                            sb2_ingress,
                            linewidth=2,
                            label="SecureBox-1 Ingress",
                            linestyle='-',
                            color='crimson')

sb2_egress_plot, = plt.plot(time_series,
                           sb2_egress,
                           linewidth=2,
                           label="SecureBox-1 egress",
                           linestyle='--',
                           color='blue')

# Set plot's attributes
plt.xlim(min(time_series), max(time_series)+2)
plt.ylim(0, max(sb1_ingress)+5)

# Set legend
plt.legend([sb2_ingress_plot, sb2_egress_plot],
           ['Ingress Traffic', 'Egress Traffic'], fontsize=24)
plt.locator_params(nbins=20)

# set the annotations
ax = plt.gca()
# Event 3
ax.arrow(103, 0, 0, 35, head_width=2, head_length=5, fc='k', ec='k')
ax.text(103, 20, 'Event 3', fontsize=20)
# Event 4
ax.arrow(132, 0, 0, 55, head_width=2, head_length=5, fc='k', ec='k')
ax.text(132, 20, 'Event 4', fontsize=20)

# Set labels
# plt.xlabel('Time Series', fontsize=16)
plt.ylabel('Traffic kb/s', fontsize=24)
plt.title('SecureBox 2', fontsize=26)
plt.grid(True)


plt.subplot(413)
# Plot the traffic average
sb3_ingress_plot, = plt.plot(time_series,
                            sb3_ingress,
                            linewidth=2,
                            label="SecureBox-1 Ingress",
                            linestyle='-',
                            color='crimson')

sb3_egress_plot, = plt.plot(time_series,
                           sb3_egress,
                           linewidth=2,
                           label="SecureBox-1 egress",
                           linestyle='--',
                           color='blue')

# Set plot's attributes
plt.xlim(min(time_series), max(time_series)+2)
plt.ylim(0, max(sb1_ingress)+5)

# Set legend
plt.legend([sb2_ingress_plot, sb2_egress_plot],
           ['Ingress Traffic', 'Egress Traffic'], fontsize=24)
plt.locator_params(nbins=20)

# set the annotations
ax = plt.gca()
# Event 3
ax.arrow(103, 0, 0, 35, head_width=2, head_length=5, fc='k', ec='k')
ax.text(103, 20, 'Event 3', fontsize=20)
# Event 5
ax.arrow(144, 0, 0, 55, head_width=2, head_length=5, fc='k', ec='k')
ax.text(144, 20, 'Event 5', fontsize=20)

# Set labels
# plt.xlabel('Time Series', fontsize=16)
plt.ylabel('Traffic kb/s', fontsize=24)
plt.title('SecureBox 3', fontsize=26)
plt.grid(True)

plt.subplot(414)
# Plot the traffic average
cbta_ingress_plot, = plt.plot(time_series,
                            cbta_ingress,
                            linewidth=2,
                            label="SecureBox-1 Ingress",
                            linestyle='-',
                            color='crimson')

cbta_egress_plot, = plt.plot(time_series,
                           cbta_egress,
                           linewidth=2,
                           label="SecureBox-1 egress",
                           linestyle='--',
                           color='blue')

# Set plot's attributes
plt.xlim(min(time_series), max(time_series)+2)
plt.ylim(0, max(cbta_egress)+5)

# Set legend
plt.legend([cbta_ingress_plot, cbta_egress_plot],
           ['Ingress Traffic', 'Egress Traffic'], fontsize=24)
plt.locator_params(nbins=20)

# set the annotations
ax = plt.gca()
# Event 1
ax.arrow(31, 0, 0, 35, head_width=2, head_length=5, fc='k', ec='k')
ax.text(22, 20, 'Event 1', fontsize=20)
# Event 2
ax.arrow(43, 0, 0, 35, head_width=2, head_length=5, fc='k', ec='k')
ax.text(44, 20, 'Event 2', fontsize=20)
# Event 3
ax.arrow(103, 0, 0, 75, head_width=2, head_length=5, fc='k', ec='k')
ax.text(103, 20, 'Event 3', fontsize=20)

# Set labels
plt.xlabel('Time Series', fontsize=24)
plt.ylabel('Traffic kb/s', fontsize=24)
plt.title('Cloud-Based Traffic Analyser', fontsize=26)
plt.grid(True)


plt.show()
