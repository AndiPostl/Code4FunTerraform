#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Bash as CGI"
echo "</title></head><body>"

echo "<center><h1>Meetup Code4Fun - Prime Tower, Sep 19, 2018</center/h1>"
echo ""
echo "<h1>General system information for host <font color=red>$(hostname -s)</font/h1>"
echo ""

echo "<h1>Memory Info</h1>"
echo "<pre> $(free -m) </pre>"

echo "<h1>Disk Info:</h1>"
echo "<pre> $(df -h|grep -v tmpfs) </pre>"

echo "<h1>CPU Info</h1>"
echo "<pre> $(lscpu|grep -v Flags) </pre>"

echo ""
echo "<center>Information generated on $(date)</center>"
echo "</body></html>"

