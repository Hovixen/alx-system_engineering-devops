## Command Line for the win

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/324/06AChAO.png)



## Background Context
[CMD CHALLENGE](https://intranet.alxswe.com/rltoken/a83_NOBEtXgFr1Yqej0HYA) is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

### Steps in using the SFTP command-line tool :heavy_check_mark:

**1.**  Connect to the remote sever using `ssh` to test the SSH access using the command

```
$ ssh <your_remote_username>@<your_server_ip> or <remote_hostname>
```
if it connects successfully, enter exit to close the ssh connection
```
$ exit
```

**2.**	Now reconnect using the `sftp` session by using the following command.

```
ssh <your_remote_username>@<your_server_ip> or <remote_hostname>
```
You will now be connected to the remote server and your prompt would change to `sftp`

*P.S: for all successful connection you might be asked to provide a password, this is the password for your sandbox*

Use the command `help` or `?` to get the list of commands used withing the `sftp` session

```
sftp> help
```

**3.**	Copy or download any file or folder from the remote server to the local machine  by using the command `get`

```
sftp> get <name_of_file> or <name_of_dir>
```

**4.**	Upload or move any file or folder from your local machine to the remote server by using the command `put`

```
sftp> put <name_of_file> or <name_of_dir>
```
