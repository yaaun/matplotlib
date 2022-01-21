"""
=========================================
Adding special, user-set ticks to an axis
=========================================

It is sometimes helpful to mark an axis with one or more *special* ticks.
By “special tick”, it is meant a tick that is at a non-standard location,
other than determined automatically by the :class:`matplotlib.ticker.Locator`
of the axis.

matplotlib does not, as of version 3.5.1, have a dedicated interface for
adding special ticks – a feature which some graphing software, such as
OriginLab_, provides out of the box. Fortunately it is relatively easy to
add special ticks with existing API functions.

Contributed by :ghuser:`yaaun`.

.. _OriginLab: https://www.originlab.com/doc/Origin-Help/AxesRef-SpecialTicks
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


xs = 


special_ticks = [1.1, 2.5, 3.7] # Some arbitrary tick locations
special_labels = [f"{tick:g}" for tick in special_ticks]

secaxis = axes.secondary_yaxis("left") # or "right", according to preference

# Labels are generated and set manually to circumvent the default axis
# Formatter, which is not guaranteed to generate a tick label.
secaxis.set_yticks(special_ticks, labels=special_labels)

"""
Note that there is no limit to the number of secondary axes and it
is possible to overlay a secondary axis on another axis.

See issue :ghissue:`22262` for discussion.
"""