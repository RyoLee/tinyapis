# TinyApis
A simple API server

|path|param|description|
|--------|------|-------|
|/timestamp|none|unix timestamp|
|/str2md5|str|md5 hash|
|/2lowercase|str|to lowercase |
|/2uppercase|str|to uppercase|
|/ping|none|ping test|
|/gettoken|key|md5(unix_timestamp_sec/30 + key)|
