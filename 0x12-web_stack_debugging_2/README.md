# 0x12. Web stack debugging #2

## Concept
![img](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/287/99littlebugsinthecode-holberton.jpg)

## Task
![imge](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/eaeff07a715ff880b1ceb8e863a1d141a74a7f85.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230418%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230418T153114Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=26e3a3a5945e1840534608d93d8d1745e2ae81d3ce018542cf1b0165bd8d4a34)

> The user root is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the root user, as if you fat finger a command and for example run rm -rf /, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do, just need to use a specific command that you need to discover.
>
> For the containers that you are given in this project as well as the checker, everything is run under the root user, which has the ability to run anything as another user.
> 
> write a Bash script that accepts one argument
> 
> the script should run the whoami command under the user passed as an argument
```
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```


