# Hands-on Linux-03 : Managing Users and Groups

Purpose of the this hands-on training is to teach the students how to manage users and groups.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- explain users and groups in linux.

- manage users and groups.

## Outline

- Part 1 - Basic User Commands

- Part 2 - User Management

- Part 3 - User Passwords

- Part 4 - Group Management

## Part 1 - Basic User Commands
​
### whoami
​
```bash
whoami
sudo su
pwd
whoami
su ec2-user
sudo su -
pwd
```
​
### who
​
```bash
exit
who
who
```
​
### w
​
```bash
w
who
```
​
### id
​
```bash
id
id root
sudo su
useradd user1
id user1
```
​
### su
​
```bash
su ec2-user
su user1
sudo su user1
pwd
exit
sudo su - user1
pwd
```
​
### passwd
​
```bash
exit
sudo su
useradd user2
passwd user2
su - user2
passwd
exit
su user2
```
​
## Part 2 - User management
​
### /etc/passwd
​
```txt
exit
cat /etc/passwd
tail -3 /etc/passwd
```
​
### useradd
​
```txt
sudo useradd user3
cd /home
ls
cd /etc
ls login*
cat login.defs
sudo nano login.defs
sudo useradd user4
cd /home && ls
cat /etc/passwd
sudo useradd -m user5
cd /home && ls
sudo useradd -m -d /home/user6home user6
ls
sudo useradd -m -c "this guy is developer" user7
cat /etc/passwd
cat /etc/passwd | grep user7
```
​
### userdel
​
```txt
cat /etc/passwd
sudo userdel user5
cat /etc/passwd
cd /home
ls
sudo userdel -r user1
cd /home
ls
```
​
### usermod
​
```txt
cat /etc/passwd
sudo usermod -c "this guy will be an aws solution architect" user7
cat /etc/passwd
sudo usermod --help
sudo usermod -l Superuser user2
cat /etc/passwd
```
​
## Part 3 - User Passwords
​
### passwd-etc/shadow-etc/login.defs.
​
```txt
  cd /etc
  sudo cat shadow
  cat /etc/login.defs
```
​
## Part 4 - Group Management
​
### groups
​
```txt
cd
groups
sudo groupadd linux
sudo groupadd aws
sudo groupadd python
cat /etc/group
groups
sudo usermod -a -G linux ec2-user
cat /etc/group
groups
sudo usermod -G aws ec2-user
cat /etc/group
sudo groupmod -n my-linux linux
cat /etc/group
groups
cat /etc/group
sudo groupdel python
cat /etc/group
sudo gpasswd -a user7 aws
cat /etc/group
sudo gpasswd -d user7 aws
cat /etc/group
```