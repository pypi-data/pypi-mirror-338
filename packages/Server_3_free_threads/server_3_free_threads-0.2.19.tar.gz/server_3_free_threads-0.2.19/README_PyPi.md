
# Server_3_free_threads
the project appeared as a result of experiments on sockets. <br>
This is a WSGI server based on threads

<br>

***
### *Important!*
*It is supported only on Linux 2.5.44 and later*
***

<br>

## the server uses four threads:
1.<b>accepting_connections</b>, to accept connections<br>
2.<b>reading_from_socket</b>, to read data from a client socket<br>
3.<b>sending_to_socket</b>, to send data to a socket<br>
4.<b>close_client_sock</b>, to close client sockets<br>

<br>

***
### *<p style="color: yellow;">Note</p>*
*It is recommended to use a python 3.13 or later<br>
build from the source code, with the GIL disabled,<br> 
to improve performance*
***

<br>

## Quick start

### log in to the root of your project
![img](https://raw.githubusercontent.com/VadimKazakov-web/Server_3_free_threads/refs/heads/main/img/1.1.png)
![img](https://raw.githubusercontent.com/VadimKazakov-web/Server_3_free_threads/refs/heads/main/img/1.2.png)

<h3>activate the virtual environment</h3>

![img](https://raw.githubusercontent.com/VadimKazakov-web/Server_3_free_threads/refs/heads/main/img/2.1.png)

### install the library with the command:<br>
pip install Server_3_free_threads

### log in before the package <br>where the module is located wsgi.py
![img](https://raw.githubusercontent.com/VadimKazakov-web/Server_3_free_threads/refs/heads/main/img/3.1.png)
![img](https://raw.githubusercontent.com/VadimKazakov-web/Server_3_free_threads/refs/heads/main/img/3.2.png)

### create a text configuration file for the server<br> with any name

The configuration file must contain the following required fields:

* HOST - server host
* PORT - server port
* SOCKET_BACKLOG - this parameter in socket.listen(backlog) <br>determines the size of the queue waiting for connection.
* APP - the module where the wsgi application named *application* is located
* DOMAIN - server domain

sample configuration file:

![img](https://raw.githubusercontent.com/VadimKazakov-web/Server_3_free_threads/refs/heads/main/img/3.3.png)

### starting the server

now you can start the server with the command:

python -m Server_3_free_threads configfile=<*path*> <br>
* *path* - relative path to the configuration file

example:

![img](https://raw.githubusercontent.com/VadimKazakov-web/Server_3_free_threads/refs/heads/main/img/4.1.png)

### done!


