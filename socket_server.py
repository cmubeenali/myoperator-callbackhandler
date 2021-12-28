import socket
import sys

def print_output(message):
    with open('/opt/myoperator-callbackhandler/output.txt', 'a+') as f:
        try:            
            f.seek(0)
            f.write('\n')
            f.write(message)
        except Exception as err:
            f.write(err)
        finally:
            f.close()  

if __name__=='__main__':  
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
        print_output('Bind failed. Error Code : ' 
            + str(massage[0]) + ' Message ' 
            + massage[1])
        sys.exit()
        
    # print if Socket binding operation completed    
    print_output('Socket binding operation completed')
    
    # With the help of listening () function
    # starts listening
    soc.listen(9)

    while True:
        conn, address = soc.accept()
        # print the address of connection
        print_output('Connected with ' + address[0] + ':' 
            + str(address[1]))
        data = conn.recv(1024)

        print_output("RECEIVED: %s" % (data.decode('ascii')))
        conn.close()