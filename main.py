# run_<script-name>.py
# excutes the associated script  (must keep FindFunc.py and script_init.py in DB directory)
#
# 12/28/2016

#****************************
# ***CHANGE NEXT TWO LINES***
last_edit =  '05/11/2022'
current_script = 'rs2mq_check'
#****************************
#
# Brian M Anderson, PhD
# UNC Health Care
##################################################################################


# Raystation
from connect import *

from script_init import UncScriptInit # Points to production environment folder
UncScriptInitObj = UncScriptInit()
baseDir = UncScriptInitObj.get_path()
sep = UncScriptInitObj.get_sep()



# location of misc files
misc = baseDir + sep + 'misc'
sys.path.append(misc)


#****************************
# ***CHANGE THESE LINES***
import rs2mq_check
print('...just ran {} version {} ...'.format(current_script,last_edit))
#****************************
