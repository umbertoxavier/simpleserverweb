import socket
 
HOST,PORT = ' ',12000
 
my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
my_socket.bind((HOST,PORT))
my_socket.listen(1)

print('Serving on port ',PORT)
 
while True:
    connection,address = my_socket.accept()
    request = connection.recv(1024).decode('utf-8')
    string_list = request.split(' ')    
 
    method = string_list[0]
    requesting_file = string_list[1]
    
    print(method)
    print('Client request ',requesting_file) 
    
    myfile = requesting_file.lstrip('/')
    
    if(myfile == ''):
        myfile = 'index.html'
        
    if(myfile == 'index2'):
        myfile = 'index2.html'
    
    try:
        file = open(myfile,'rb') 
        response = file.read()
        file.close()
 
        header = 'HTTP/1.1 200 OK\n'

        mimetype = 'text/html'    
 
        header += 'Content-Type: '+str(mimetype)+'\n\n'
        
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
 
    final_response = header.encode('utf-8')
    final_response += response
    connection.send(final_response)
    connection.close()
