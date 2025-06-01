# -----------------------------------------------------------------------------
# Title       : PB-TIED (Password-Based Text & Image Encrption-Decryption) Tool
# Author      : https://github.com/Abhiram-ARS
# Description : This Python-based tool provides a simple yet secure way 
#               to encrypt and decrypt messages using a password.
# Version     : Command Line Interface - I (cli-1)
# -----------------------------------------------------------------------------

def clear(n):
    import os

    if n==1:
        ent = input('\n\n\n\n[ Press Enter to Continue ]')
    elif n==2:
        ent = input('\n\n\n\n[ Press Enter to Launch PB-TED ]')
    else:
        pass

    os.system('cls')

def root():
    clear(2)
    main()

def main():
    import art
    clear(0)
    print("*"*70 ,"\n")
    print(art.text2art("PB-TIED", font="starwars"))
    print("\tPassword-Base_Text_&_Image_Encryption-Decryption")
    print("\t\t\t\t\t\t- Abhiram-ARS@github\n")
    print("*"*70 ,"\n")
    print("  +=================================+",
          "  |           MAIN MENU             |",
          "  +-----+---------------------------+",
          "  |  1  | Encrypt - TEXT            |",
          "  |  2  | Decrypt - TEXT            |",
          "  +-----+---------------------------+",
          "  |  3  | Encrypt - IMAGE           |",
          "  |  4  | Decrypt - IMAGE           |",
          "  +-----+---------------------------+",
          "  |  q  | Exit                      |",
          "  +=====+===========================+",sep='\n')

    ch=input("\nEnter Choice :-")
    print("\n"+"*"*50 ,"\n")

    match(ch):
        # Encrypt - TEXT
        case '1':
            data = readData4EncryptionTxt()
            print("="*50)
            retval = encryptDataTxt(data)
            if retval['stat']==1:
                print("Completed.")
                print("Encrypted Data:-\n")
                print(retval['note'])
            else:                                 
                print("_ERROR_:"+retval['note'])

        # Decrypt - TEXT
        case '2':
            data = readData4DecryptionTxt()
            print("="*50)
            retval = decryptDataTxt(data)
            if retval['stat']==1:
                print("Decrypted Data:-\n")
                print(retval['note'])
            else:
                print("_ERROR_:"+retval['note'])

        # Encrypt - IMAGE
        case '3':
            data = readData4Img()
            print("="*50)
            retval = encryptDataImg(data)
            if retval['stat']==1:
                print("Completed.")
                print("Encrypted Data:-\n")
                print(retval['note'])
            else:
                print("_ERROR_:"+retval['note'])
        
        # Decrypt - IMAGE
        case '4':
            data = readData4Img()
            print("="*50)
            retval = decryptDataImg(data)
            if retval['stat']==1:
                print("Decrypted Data:-\n")
                print(retval['note'])
            else:
                print("_ERROR_:"+retval['note'])

        case 'q':
            print("Exiting...!")
            ent=input()
            exit()
        case _:
            print("_ERROR_:_Choice_Not_Defined_")   

    print("="*50)
    clear(1)
    main()

def readData4EncryptionTxt():
    print("  [1]-Encrypt String",
          "  [2]-Encrypt Text File",sep='\n')
    ch1=input("\nEnter Choice :-")
    print("="*50)
    match(ch1):
        case '1':
            message = input("Mesage    : ")
            input_pwd = input("Password  : ")
            file = input("Output File path : ")
        
        case '2':
            try:
                fn = input("Enter Input Filename :")
                if not fn.endswith(".txt"):
                    fn = fn+".txt"
                with open(fn,'r') as f1:
                    message=f1.read()
            except:
                print("_ERROR_:_File_Not_Found_")
                main()
                
            input_pwd = input("Password  : ")
            file = input('Enter Output text file path (or Press Enter for default). -')
            if file=='':
                file = fn[:-4]+'_encrypted.txt'

        case _:
            print("_ERROR_:_Choice_Not_Defined_")
            main()

    

    return {"pwd" : input_pwd,
            "msg" : message, 
            "file": file}

def encryptDataTxt(data):
    from cryptography.fernet import Fernet

    try:
        from cryptography.fernet import Fernet
        fkey = genKey(data['pwd'])
        fernet = Fernet(fkey)
        msg=data['msg']
        encrypted = fernet.encrypt(msg.encode()).decode()

        if data['file'].endswith(".txt"):
            fn=data['file']
        else:
            fn=data['file']+".txt"

        with open(fn,"w") as f1:
            f1.write(encrypted)
        
        rmsg = encrypted
        status = 1
        rmsg += '\n\nFile Saved >'+fn
        
    except:
        status=0
        rmsg='ERROR'
    
    return {"stat" : status,
            "note" : rmsg}

def readData4DecryptionTxt():
    import os

    file = input("File Name : ")
    if not(os.path.exists(file)):
        print("_ERROR_:_File_Not_Found_")
        clear(1)
        main()
    input_pwd = input("Password  : ")
    
    return {'pwd' : input_pwd,
            'file' : file}

def decryptDataTxt(data):
    from cryptography.fernet import Fernet

    if data['file'].endswith(".txt"):
        fn=data['file']
    else:
        fn=data['file']+".txt"

    try:
        with open(fn,"r") as f2:
            message = f2.read()
            fkey = genKey(data['pwd'])
            fernet = Fernet(fkey)
            try:
                decrypted = fernet.decrypt(message.encode()).decode()
                status=1
                rmsg=decrypted
            except:
                return {"stat" : 0,
                        "note" : '_Invalied_Password_'}
    except:
        return {"stat" : 0,
                "note" : '_File_Not_Found_'}

    ch1 = input('Do You want to save decrypted Message to file <y/n> ? ')

    if ch1 in 'yY':
        opfile = input('Enter custom file Name (or Press Enter for default). -')
        if opfile=='':
            opfile = data['file']+'_decrypted.txt'

        with open(opfile,"w") as f1:
            f1.write(decrypted)

        rmsg+='\n\nfile saved > '+opfile
    print("="*50)

    return {"stat" : status,
            "note" : rmsg}

def readData4Img():
    import os

    infile = input("Enter Input Image path (with Extension) :")
    if not(os.path.exists(infile)):
        print("_ERROR_:_File_Not_Found_")
        clear(1)
        main()

    pwd = input("Password  : ")
    opfile = input("Enter Output Image path (with Extension) :")

    return{'pwd' : pwd,
           'infile' : infile,
           'opfile' : opfile}

def encryptDataImg(data):
    from cryptography.fernet import Fernet

    with open(data['infile'], "rb") as file:
        imgData = file.read()

    try:
        fkey = genKey(data['pwd'])
        fernet = Fernet(fkey)
        encrypted = fernet.encrypt(imgData)

        with open(data['opfile'], "wb") as file:
            file.write(encrypted)
        
        rmsg = "Image Encrypted"
        status = 1
        rmsg += '\n\nFile Saved >'+ data['opfile']
        
    except:
        status=0
        rmsg='ERROR'
    
    return {"stat" : status,
            "note" : rmsg}

def decryptDataImg(data):
    from cryptography.fernet import Fernet

    with open(data['infile'], "rb") as file:
        imgData = file.read()

    try:
        fkey = genKey(data['pwd'])
        fernet = Fernet(fkey)
        decrypted = fernet.decrypt(imgData)

        with open(data['opfile'], "wb") as file:
            file.write(decrypted)
        
        rmsg = "Image Decrypted"
        status = 1
        rmsg += '\n\nFile Saved >'+ data['opfile']
        
    except:
        status=0
        rmsg='ERROR'
    
    return {"stat" : status,
            "note" : rmsg}

def genKey(value):
    import hashlib
    import base64

    pwd=value.encode()
    genkey = hashlib.sha256(pwd).digest()
    fernet_key = base64.urlsafe_b64encode(genkey)

    return fernet_key

root()
