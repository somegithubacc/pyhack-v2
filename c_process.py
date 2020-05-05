import pymem

class c_process( ):
    def __init__( self ):
        self.process = self.get_process( "csgo" )
        
        #game specific
        self.server_browser = self.get_module( "serverbrowser.dll" )
        self.client_panorama = self.get_module( "client_panorama.dll" )
        self.engine = self.get_module( "engine.dll" )

    def get_process( self, process ):
        return_process = None

        while return_process == None:
            try:
                return_process = pymem.Pymem( process )
            except pymem.exception.ProcessNotFound:
                pass

        return return_process
    
    def get_module( self, module ):
        return_module = None

        while return_module == None:
            try:
                return_module = pymem.process.module_from_name( self.process.process_handle, module )
            except:
                pass

        return return_module