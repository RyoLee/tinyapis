#!/bin/sh
mkdir -p /config
if [ ! -f "/config/TinyApis.cfg" ];then
    cp /TinyApis.cfg.sample /config/TinyApis.cfg
fi
python /TinyApis.py