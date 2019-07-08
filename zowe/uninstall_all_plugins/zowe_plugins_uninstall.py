#!/usr/bin/env python
import os

plugins_list = []
plugins_output = os.popen("zowe plugins list").readlines()

if plugins_output:
    for line in plugins_output:
        if "No plugins" in line:
            print("No plugins installed.\nNothing to do. Exiting...")
            break
        elif "pluginName" in line:
            plugins_list.append(str(line.split()[2]))

if plugins_list:
    for plugin in plugins_list:
        print("Uninstalling {} plugin...".format(plugin))
        os.system("zowe plugins uninstall {}".format(plugin))