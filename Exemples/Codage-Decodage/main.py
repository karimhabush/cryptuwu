#!/usr/bin/env python3
import base64 

def encode_base64(filepath):
    try :
        f_input = open(filepath, 'rb') #open binary file in read mode
        f_read = f_input.read()
        f_encode = base64.b64encode(f_read)
        f_output = open(filepath+".enc","w")
        f_output.write(f_encode.decode("utf-8"))
        
        f_input.close()
        f_output.close()
    except Exception as e: 
        print(str(e))
        print(filepath)

def decode_base64(filepath):
    try :
        f_input = open(filepath, 'rb') #open binary file in read mode
        f_read = f_input.read()
        f_decode = base64.b64decode(f_read)
        f_output = open(filepath+".dec","wb")
        f_output.write(f_decode)
        
        f_input.close()
        f_output.close()
    except Exception as e: 
        print(str(e))

decode_base64("./test.txt.enc")
    