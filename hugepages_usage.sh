#!/bin/bash

# show hugepage usage from /proc/meminfo
# Author: pengfeiz

function get_HugePages_Total()
{
    grep "HugePages_Total" /proc/meminfo | awk '{print $2}'
}

function get_HugePages_Free()
{
    grep "HugePages_Free" /proc/meminfo | awk '{print $2}'
}

function record_Hugepages_info()
{
    while true
    do
        calc_Hugepages_used
        sleep $interval
    done
}

function calc_Hugepages_used()
{
    HugePages_Free=`get_HugePages_Free`
    let HugePages_Used=($HugePages_Total-$HugePages_Free)*2

    printf "`date "+%4Y-%m-%d %H:%M:%S"`\t$HugePages_Used\n" >> hugepages_usage.log    

    # temporary: use iostat to record disk utilization
    iostat -x -N -p -t >> disk_usage.log
}

## main function start from here
echo > hugepages_usage.log
echo > disk_usage.log

default_interval=5
HugePages_Total=`get_HugePages_Total`

if [ -z $1 ]; then
    interval=$default_interval
else
    interval=$1
fi
echo "check interval is $interval seconds"

# hugepage usage
record_Hugepages_info






