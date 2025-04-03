


class fNIRS():
    def __init__(self, filepath:str|None=None):

        self.history = []
        pass
    def ParseSNIRF(self, ):

        pass

    def get_new_filename(self,):
        name = ["_" + str(n) for n in self.history]
        name.append(".snirf")
        return name
    
    def WriteSNIRF(self, ):

        print("filename : ", self.get_new_filename())
        pass

    def Trim(self, before_first_feature=20.0, after_last_feature=10.0):
        """ Trims the fnirs file """

        self.history.append("TRIM")
        pass

    def Bandpass(self, ):

        self.history.append("BANDPASS")
        pass

    def Normalize(self, ):

        self.history.append("NORM")
        pass

    def Preprocess(self, ):

        pass
    


fnirs = fNIRS()

fnirs.Trim()

fnirs.WriteSNIRF()