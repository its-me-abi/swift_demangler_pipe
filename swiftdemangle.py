
import subprocess,os,time

class libloader :
    libname = r".\lib\swift-demangle.exe"
    libpath = os.path.normpath(os.path.join(os.path.dirname(__file__), libname))

    def __init__(self,path = ""):
        self.loadedlib = subprocess.Popen([path or self.libpath,""] , stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def send(self,mangledname):
        mangledname = mangledname +  "\n"
        data  = bytes(mangledname, 'UTF-8')

        print("writing to stdin = ", data)
        self.loadedlib.stdin.write(data)
        print ("wrote to stdin")

    def read(self):
        print ( "reading from stdout" )
        return self.loadedlib.stdout.read()

class demangler (libloader):
    def __init__(self,path = ""):
        super().__init__(path)

    def get_demangled_name(self,mangledname ):
        self.send(mangledname)
        data = self.read()
        return data

if __name__ == "__main__":
   name = demangler().get_demangled_name("_TtuRxs8RunciblerFxWx5Mince6Quince_")

   if name == "<A where A: Swift.Runcible>(A) -> A.Mince.Quince":
       print("successfully demangled = ",name)

   else:
       print("code has some problems.failed demangling")