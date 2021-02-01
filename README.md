## This is a vulnerability test for Netcore / Netis router command execution.
# Test command inject.
  ### 1.Use the PS command to inject into the product(WF2780 V2.3.40404)
  ![](https://github.com/yhstar00/netis-route/blob/main/6.png)
  ### 2.Use the PS command to inject into the product(WF2411 V1.1.29629)
  ![](https://github.com/yhstar00/netis-route/blob/main/1.png)
  ![](https://github.com/yhstar00/netis-route/blob/main/2.png)
# Test Rstart telnetd.
  ### 1.kill process 14367 on product(WF2411 V1.1.29629)
  ![](https://github.com/yhstar00/netis-route/blob/main/3.png)
  ### 2.Use command telnetd inject
  ![](https://github.com/yhstar00/netis-route/blob/main/4.png)
  ### 3.We can see that the process id is 15755,We made it!
  ![](https://github.com/yhstar00/netis-route/blob/main/5.png)
# Test Netcore / Netis route Remote Command Inject On python.
  ### We made it!
  ![](https://github.com/yhstar00/netis-route/blob/main/7.png)
# Thinks,It's Done.
