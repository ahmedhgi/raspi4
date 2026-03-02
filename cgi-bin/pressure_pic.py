#!/usr/bin/python3
filename = "/home/platz4/raspi4/02.03./pressure1.rrd"
import rrdtool
ret = rrdtool.graph(	'-' ,
   			'--imgformat', 'PNG' ,
			'--width','640' ,
			'--height','300' ,
			'--start','-1hour' ,
			'--end', 'now' ,
			'--vertical-label', "hPa" ,
			'--alt-autoscale' ,
			'--title', 'Druck in der Hose' ,
			'DEF:pressure=/home/platz4/raspi4/02.03./pressure1.rrd:pressure:AVERAGE' ,
			'AREA:pressure#CCFFCC:' ,
             		'LINE1:pressure#0000FF:Luftdruck BMP280' ,
             		'GPRINT:pressure:MIN:Min\\:  %3.2lf hPa' ,
             		'GPRINT:pressure:MAX:Max\\: %3.2lf hPa' ,
             		'GPRINT:pressure:AVERAGE: Avg\\: %3.2lf hPa' ,
             		'GPRINT:pressure:LAST: Aktuell\\: %3.2lf hPa' )
