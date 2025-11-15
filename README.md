# honeytrace  

a small, fake ssh honeypot i built to learn how attackers think and to mess around with network security,safely. 
it listens on a port, acts like a real ssh login, logs whatever username/password someone tries, and even lets them run fake shell commands so i can watch what they'd try to do.  

i basically wanted something simple, noisy and fun to look at traffic and like  attacker behavior
## features  
- fake ssh banner and a login flow  
- logs username and password attempts  
- basic geoip lookup 
- fake shell (captures commands like `ls`, `cat`, `pwd` etc)  
- timestamped logs are saved automatically  
- minimal python and runs anywhere  

## how to run:
-use python3 honeytrace.py. 
-default port is 2222
-so connect using netcat: nc localhost 2222

## why a honeypot?
it piqued my interest and  helped me learn a lot, stuff like logging, tcp behavior, python sockets etc etc which is pretty cool.

## disclaimer  
for learning only. don’t expose it to networks you don’t own
