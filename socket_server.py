import socket
import sys
  
  
# specify Host and Port 
HOST = '' 
PORT = 6000
    
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
try:
    # With the help of bind() function 
    # binding host and port
    soc.bind((HOST, PORT))
       
except socket.error as massage:
      
    # if any error occurs then with the 
    # help of sys.exit() exit from the program
    print('Bind failed. Error Code : ' 
          + str(massage[0]) + ' Message ' 
          + massage[1])
    sys.exit()
      
# print if Socket binding operation completed    
print('Socket binding operation completed')
   
# With the help of listening () function
# starts listening
soc.listen(9)
   
conn, address = soc.accept()
# print the address of connection
print('Connected with ' + address[0] + ':' 
      + str(address[1]))
      
while True:
    data = conn.recv(1024)

    print("RECEIVED: %s" % (data.decode('ascii')))
    conn.close()
    break
soc.close()