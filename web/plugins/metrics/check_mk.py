#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

# Metric definitions for Check_MK's checks

KB = 1024
MB = 1024 * 1024
GB = 1024 * 1024 * 1024
TB = 1024 * 1024 * 1024 * 1024
PB = 1024 * 1024 * 1024 * 1024 * 1024

#   .--Units---------------------------------------------------------------.
#   |                        _   _       _ _                               |
#   |                       | | | |_ __ (_) |_ ___                         |
#   |                       | | | | '_ \| | __/ __|                        |
#   |                       | |_| | | | | | |_\__ \                        |
#   |                        \___/|_| |_|_|\__|___/                        |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definition of units of measurement.                                 |
#   '----------------------------------------------------------------------'

unit_info[None] = {
    "title"  : "",
    "symbol" : "",
    "render" : lambda v: "%.1f" % v,
}

unit_info["count"] = {
    "title"  : _("Count"),
    "symbol" : "",
    "render" : lambda v: "%d" % v,
}

# value ranges from 0.0 ... 100.0
unit_info["%"] = {
    "title"  : _("%"),
    "symbol" : _("%"),
    "render" : lambda v: "%s%%" % drop_dotzero(v),
}

# Similar as %, but value ranges from 0.0 ... 1.0
unit_info["100%"] = {
    "title"  : _("%"),
    "symbol" : _("%"),
    "render" : lambda v: "%s%%" % drop_dotzero(100.0 * v),
}

unit_info["s"] = {
    "title" : _("sec"),
    "symbol" : _("s"),
    "render" : age_human_readable,
}

unit_info["/s"] = {
    "title" : _("per second"),
    "symbol" : _("/s"),
    "render" : lambda v: "%s%s" % (drop_dotzero(v), _("/s")),
}

unit_info["bytes"] = {
    "title"  : _("Bytes"),
    "symbol" : _("B"),
    "render" : bytes_human_readable,
}

unit_info["c"] = {
    "title"  : _("Degree Celsius"),
    "symbol" : _(u"°C"),
    "render" : lambda v: "%s %s" % (drop_dotzero(v), _(u"°C")),
}


#.
#   .--Metrics-------------------------------------------------------------.
#   |                   __  __      _        _                             |
#   |                  |  \/  | ___| |_ _ __(_) ___ ___                    |
#   |                  | |\/| |/ _ \ __| '__| |/ __/ __|                   |
#   |                  | |  | |  __/ |_| |  | | (__\__ \                   |
#   |                  |_|  |_|\___|\__|_|  |_|\___|___/                   |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definitions of metrics                                              |
#   '----------------------------------------------------------------------'

metric_info["mem_used"] = {
    "title" : _("Used RAM"),
    "unit"  : "bytes",
    "color" : "#80ff40",
}

metric_info["mem_free"] = {
    "title" : _("Free RAM"),
    "unit"  : "bytes",
    "color" : "#ffffff",
}

metric_info["swap_used"] = {
    "title" : _("Used Swap space"),
    "unit"  : "bytes",
    "color" : "#008030",
}

metric_info["caches"] = {
    "title" : _("Memory used by caches"),
    "unit"  : "bytes",
    "color" : "#ffffff",
}

metric_info["swap_free"] = {
    "title" : _("Free Swap space"),
    "unit"  : "bytes",
    "color" : "#eeeeee",
}

metric_info["execution_time"] = {
    "title" : _("Execution time"),
    "unit"  : "s",
    "color" : "#22dd33",
}

metric_info["load1"] = {
    "title" : _("CPU load average of last minute"),
    "unit"  : None,
    "color" : "#6688ff",
}

metric_info["fs_used"] = {
    "title" : _("Used filesystem space"),
    "unit"  : "bytes",
    "color" : "#00ffc6",
}

metric_info["temp"] = {
    "title" : _("Temperature"),
    "unit"  : "c",
    "color" : "#3399ff",
}

metric_info["ctxt"] = {
    "title" : _("Context switches"),
    "unit"  : "/s",
    "color" : "#ddaa66",
}

metric_info["pgmajfault"] = {
    "title" : _("Major Page Faults"),
    "unit"  : "/s",
    "color" : "#ddaa22",
}

metric_info["proc_creat"] = {
    "title" : _("Process creations"),
    "unit"  : "/s",
    "color" : "#ddaa99",
}

metric_info["threads"] = {
    "title" : _("Number of threads"),
    "unit"  : "count",
    "color" : "#aa44ff",
}

metric_info["user"] = {
    "title" : _("User"),
    "help"  : _("Percentage of CPU time spent in user space"),
    "unit"  : "%",
    "color" : "#60f020",
}

metric_info["system"] = {
    "title" : _("System"),
    "help"  : _("Percentage of CPU time spent in kernel space"),
    "unit"  : "%",
    "color" : "#ff6000",
}

metric_info["io_wait"] = {
    "title" : _("IO-Wait"),
    "help"  : _("Percentage of CPU time spent waiting for IO"),
    "unit"  : "%",
    "color" : "#00b0c0",
}

metric_info["time_offset"] = {
    "title" : _("Time offset"),
    "unit"  : "s",
    "color" : "#9a52bf",
}


#.
#   .--Checks--------------------------------------------------------------.
#   |                    ____ _               _                            |
#   |                   / ___| |__   ___  ___| | _____                     |
#   |                  | |   | '_ \ / _ \/ __| |/ / __|                    |
#   |                  | |___| | | |  __/ (__|   <\__ \                    |
#   |                   \____|_| |_|\___|\___|_|\_\___/                    |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  How various checks' performance data translate into the known       |
#   |  metrics                                                             |
#   '----------------------------------------------------------------------'

check_metrics["check-mk"]                                       = {}

check_metrics["check_mk-cpu.loads"]                             = {}
check_metrics["check_mk-ucd_cpu_load"]                          = {}
check_metrics["check_mk-statgrab_load"]                         = {}
check_metrics["check_mk-hpux_cpu"]                              = {}
check_metrics["check_mk-blade_bx_load"]                         = {}

check_metrics["check_mk-cpu.threads"]                           = {}

check_metrics["check_mk-mem.linux"]                             = {}

check_metrics["check_mk-df"]                                    = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-vms_df"]                                = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-vms_diskstat.df"]                       = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_disk"]                                     = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-df_netapp"]                             = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-df_netapp32"]                           = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-zfsget"]                                = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-hr_fs"]                                 = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-oracle_asm_diskgroup"]                  = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-mysql_capacity"]                        = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-esx_vsphere_counters.ramdisk"]          = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-hitachi_hnas_span"]                     = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-hitachi_hnas_volume"]                   = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-emcvnx_raidgroups.capacity"]            = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-emcvnx_raidgroups.capacity_contiguous"] = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-ibm_svc_mdiskgrp"]                      = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-fast_lta_silent_cubes.capacity"]        = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-fast_lta_volumes"]                      = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-libelle_business_shadow.archive_dir"]   = { 0: { "name": "fs_used", "scale" : MB } }

check_metrics["check_mk-nvidia.temp"]                           = {}
check_metrics["check_mk-cisco_temp_sensor"]                     = {}
check_metrics["check_mk-cisco_temp_perf"]                       = {}
check_metrics["check_mk-cmctc_lcp.temp"]                        = {}
check_metrics["check_mk-cmctc.temp"]                            = {}
check_metrics["check_mk-smart.temp"]                            = {}
check_metrics["check_mk-f5_bigip_chassis_temp"]                 = {}
check_metrics["check_mk-f5_bigip_cpu_temp"]                     = {}
check_metrics["check_mk-hp_proliant_temp"]                      = {}
check_metrics["check_mk-akcp_sensor_temp"]                      = {}
check_metrics["check_mk-akcp_daisy_temp"]                       = {}
check_metrics["check_mk-fsc_temp"]                              = {}
check_metrics["check_mk-viprinet_temp"]                         = {}
check_metrics["check_mk-hwg_temp"]                              = {}
check_metrics["check_mk-sensatronics_temp"]                     = {}
check_metrics["check_mk-apc_inrow_temperature"]                 = {}
check_metrics["check_mk-hitachi_hnas_temp"]                     = {}
check_metrics["check_mk-dell_poweredge_temp"]                   = {}
check_metrics["check_mk-dell_chassis_temp"]                     = {}
check_metrics["check_mk-dell_om_sensors"]                       = {}
check_metrics["check_mk-innovaphone_temp"]                      = {}
check_metrics["check_mk-cmciii.temp"]                           = {}
check_metrics["check_mk-ibm_svc_enclosurestats.temp"]           = {}
check_metrics["check_mk-wagner_titanus_topsense.temp"]          = {}
check_metrics["check_mk-enterasys_temp"]                        = {}
check_metrics["check_mk-adva_fsp_temp"]                         = {}
check_metrics["check_mk-allnet_ip_sensoric.temp"]               = {}
check_metrics["check_mk-qlogic_sanbox.temp"]                    = {}
check_metrics["check_mk-bintec_sensors.temp"]                   = {}
check_metrics["check_mk-knuerr_rms_temp"]                       = {}
check_metrics["check_mk-arris_cmts_temp"]                       = {}
check_metrics["check_mk-casa_cpu_temp"]                         = {}
check_metrics["check_mk-rms200_temp"]                           = {}
check_metrics["check_mk-juniper_screenos_temp"]                 = {}
check_metrics["check_mk-lnx_thermal"]                           = {}
check_metrics["check_mk-climaveneta_temp"]                      = {}
check_metrics["check_mk-carel_sensors"]                         = {}
check_metrics["check_mk-netscaler_health.temp"]                 = {}
check_metrics["check_mk-kentix_temp"]                           = {}

check_metrics["check_mk-kernel"]                                = { "processes" : { "name" : "proc_creat", } }

check_metrics["check_mk-kernel.util"]                           = { "wait" : { "name" : "io_wait" } }
check_metrics["check_mk-vms_sys.util"]                          = { "wait" : { "name" : "io_wait" } }
check_metrics["check_mk-vms_cpu"]                               = { "wait" : { "name" : "io_wait" } }
check_metrics["check_mk-ucd_cpu_util"]                          = { "wait" : { "name" : "io_wait" } }
check_metrics["check_mk-lparstat_aix.cpu_util"]                 = { "wait" : { "name" : "io_wait" } }

check_metrics["check_mk-mbg_lantime_state"]                     = { "offset" : { "name" : "time_offset", "scale" : 0.000001 }} # convert us -> sec
check_metrics["check_mk-mbg_lantime_nb_state"]                  = { "offset" : { "name" : "time_offset", "scale" : 0.000001 }} # convert us -> sec

#.
#   .--Perf-O-Meters-------------------------------------------------------.
#   |  ____            __        ___        __  __      _                  |
#   | |  _ \ ___ _ __ / _|      / _ \      |  \/  | ___| |_ ___ _ __ ___   |
#   | | |_) / _ \ '__| |_ _____| | | |_____| |\/| |/ _ \ __/ _ \ '__/ __|  |
#   | |  __/  __/ |  |  _|_____| |_| |_____| |  | |  __/ ||  __/ |  \__ \  |
#   | |_|   \___|_|  |_|        \___/      |_|  |_|\___|\__\___|_|  |___/  |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definition of Perf-O-Meters                                         |
#   '----------------------------------------------------------------------'

perfometer_info.append(("stacked",      ( ["execution_time"], 90.0, None)))
perfometer_info.append(("logarithmic",  ( "load1",         4.0, 2.0)))
perfometer_info.append(("logarithmic",  ( "temp",         40.0, 1.2)))
perfometer_info.append(("logarithmic",  ( "ctxt",       1000.0, 2.0)))
perfometer_info.append(("logarithmic",  ( "pgmajfault", 1000.0, 2.0)))
perfometer_info.append(("logarithmic",  ( "proc_creat", 1000.0, 2.0)))
perfometer_info.append(("logarithmic",  ( "threads",     400.0, 2.0)))
perfometer_info.append(("stacked",      ( [ "user", "system", "io_wait" ],                               100.0,       None)))
perfometer_info.append(("stacked",      ( [ "fs_used(%)" ],                                              100.0,       None)))
perfometer_info.append(("stacked",      ( [ "mem_used", "swap_used", "caches", "mem_free", "swap_free" ], None, ("mem_total,mem_used,swap_used,+,/", "100%"))))
perfometer_info.append(("stacked",      ( [ "mem_used" ],                                                "mem_total", None)))
perfometer_info.append(("logarithmic",  ( "time_offset",  1.0, 10.0)))


#.
#   .--Graphs--------------------------------------------------------------.
#   |                    ____                 _                            |
#   |                   / ___|_ __ __ _ _ __ | |__  ___                    |
#   |                  | |  _| '__/ _` | '_ \| '_ \/ __|                   |
#   |                  | |_| | | | (_| | |_) | | | \__ \                   |
#   |                   \____|_|  \__,_| .__/|_| |_|___/                   |
#   |                                  |_|                                 |
#   +----------------------------------------------------------------------+
#   |  Definitions of time series graphs                                   |
#   '----------------------------------------------------------------------'
graph_info.append({
    # "title"          : _("Das ist der Titel"),       # Wenn fehlt, dann nimmer er den Titel der ersten Metrik
    # "vertical_label" : _("Das hier kommt vertikal"), # Wenn fehlt, dann nimmt er die Unit der ersten Metrik
    "metrics" : [
        ( "fs_used", "area" ),
    ]
})

graph_info.append({
    "title"   : _("CPU utilization"),
    "metrics" : [
        ( "user",    "area" ),
        ( "system",  "stack" ),
        ( "io_wait", "stack" ),
    ]
})

graph_info.append({
    "metrics" : [
        ( "time_offset", "area" ),
    ]
})
