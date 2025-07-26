class pbfedFunctions:
    def encryptBinFile_funct(data):
        from cryptography.fernet import Fernet

        try:
            from cryptography.fernet import Fernet
            fkey = genKey_Class.genKey((data['pwd']))
            fernet = Fernet(fkey)
            with open(data['file'],'rb') as f1:
                bindata = f1.read()
            encrypted = fernet.encrypt(bindata)

            fn = (data['file'].partition('.'))[0]+"_Encrypted."+(data['file'].partition('.'))[2]
            with open(fn,"wb") as f1:
                f1.write(encrypted)
            
            rmsg = "Encrypted"
            status = 1
            rmsg += '\n\nFile Saved >'+fn
            
        except:
            status=0
            rmsg='ERROR'
        
        return {"stat" : status,
                "note" : rmsg}

    def decryptBinFile_funct(data):
        from cryptography.fernet import Fernet

        rmsg = ""
        try:
            with open(data['file'],"rb") as f2:
                bindata = f2.read()
                fkey = genKey_Class.genKey((data['pwd']))
                fernet = Fernet(fkey)
                try:
                    decrypted = fernet.decrypt(bindata)
                    status=1
                    rmsg += "Decrypted"
                except:
                    return {"stat" : 0,
                            "note" : '_Invalied_Password_'}
        except:
            return {"stat" : 0,
                    "note" : '_File_Not_Found_'}

        opfile = (data['file'].partition('.'))[0]+"_Decrypted."+(data['file'].partition('.'))[2]
        with open(opfile,"wb") as f1:
                f1.write(decrypted)

        rmsg+='\n\nfile saved > '+opfile
        

        return {"stat" : status,
                "note" : rmsg}
    

    def encryptMessage_funct(data):
        from cryptography.fernet import Fernet
        import os

        try:
            from cryptography.fernet import Fernet
            fkey = genKey_Class.genKey((data['pwd']))
            fernet = Fernet(fkey)
            msg=data['msg']
            encrypted = fernet.encrypt(msg.encode()).decode()

            if data['file'].endswith(".txt"):
                fn=data['file']
            else:
                fn=data['file']+".txt"

            with open((os.getcwd().replace("\\","/")+"/PB_TIED_gui/output/")+fn,"w") as f1:
                f1.write(encrypted)
            
            rmsg = "Encrypted"
            status = 1
            rmsg += '\n\nFile Saved >'+fn
            
        except:
            status=0
            rmsg='ERROR'
        
        return {"stat" : status,
                "note" : rmsg}

    def decryptMessage_funct(data):
        from cryptography.fernet import Fernet
        import os

        if data['file'].endswith(".txt"):
            fn=(os.getcwd().replace("\\","/")+"/PB_TIED_gui/output/") + data['file']
        else:
            fn=(os.getcwd().replace("\\","/")+"/PB_TIED_gui/output/") + data['file']+".txt"

        try:
            with open(fn,"r") as f2:
                message = f2.read()
                fkey = genKey_Class.genKey((data['pwd']))
                fernet = Fernet(fkey)
                try:
                    decrypted = fernet.decrypt(message.encode()).decode()
                    opfile = (os.getcwd().replace("\\","/")+"/PB_TIED_gui/output/") + data['file']+"_decrypted.txt"
                    with open(opfile,"w") as f1:
                        f1.write(decrypted)
                    status=1
                    rmsg=decrypted

                except:
                    return {"stat" : 0,
                            "note" : '_Invalied_Password_'}
        except:
            return {"stat" : 0,
                    "note" : '_File_Not_Found_'}

        return {"stat" : status,
                "note" : rmsg}

    def encryptTextFile_funct(data):
        from cryptography.fernet import Fernet

        try:
            from cryptography.fernet import Fernet
            fkey = genKey_Class.genKey((data['pwd']))
            fernet = Fernet(fkey)
            with open(data['file'],'r') as f1:
                msg = f1.read()
            encrypted = fernet.encrypt(msg.encode()).decode()

            fn = (data['file'].partition('.'))[0]+"_Encrypted"+(data['file'].partition('.'))[2]
            with open(fn,"w") as f1:
                f1.write(encrypted)
            
            rmsg = "Encrypted"
            status = 1
            rmsg += '\n\nFile Saved >'+fn
            
        except:
            status=0
            rmsg='ERROR'
        
        return {"stat" : status,
                "note" : rmsg}

    def decryptTextFile_funct(data):
        from cryptography.fernet import Fernet

        rmsg = ""
        try:
            with open(data['file'],"r") as f2:
                message = f2.read()
                fkey = genKey_Class.genKey((data['pwd']))
                fernet = Fernet(fkey)
                try:
                    decrypted = fernet.decrypt(message.encode()).decode()
                    status=1
                    rmsg += "Decrypted"
                except:
                    return {"stat" : 0,
                            "note" : '_Invalied_Password_'}
        except:
            return {"stat" : 0,
                    "note" : '_File_Not_Found_'}

        opfile = fn = (data['file'].partition('.'))[0]+"_Decrypted.txt"
        with open(opfile,"w") as f1:
                f1.write(decrypted)

        rmsg+='\n\nfile saved > '+opfile
        

        return {"stat" : status,
                "note" : rmsg}
    

class genKey_Class:
    def genKey(value):
        import hashlib
        import base64

        pwd=value.encode()
        genkey = hashlib.sha256(pwd).digest()
        fernet_key = base64.urlsafe_b64encode(genkey)

        return fernet_key
