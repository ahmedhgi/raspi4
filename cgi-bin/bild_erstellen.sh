#!/bin/bash
filename="/home/platz4/temperature1.rrd"
rrdtool graph - \
		--imgformat 'PNG' \
		--width 640 \
		--height 300 \
		--start -1hour \
		--end now \
		--vertical-label "Grad Celsuis" \
		--alt-autoscale \
		--title Temperatur \
		DEF:temp1=/home/platz4/temperature1.rrd:temp1:AVERAGE \
		AREA:temp1#CCFFCC: \
             	LINE1:temp1#0000FF:'Temperatur DS18B20' \
             	GPRINT:temp1:MIN:"Min\\:  %3.2lf °C  "  \
             	GPRINT:temp1:MAX:"Max\\: %3.2lf °C  " \
             	GPRINT:temp1:AVERAGE:"Avg\\: %3.2lf °C " \
             	GPRINT:temp1:LAST:"Aktuell\\: %3.2lf °C "
