


class EEG():
    def __init__(self, filepath:str|None=None):

        self.history = []
        pass
    def ParseHDF5(self, ):

        pass
    
    def ParseEDF(self, ):

        pass

    def WriteHDF5(self, ):

        pass
    def WriteEDF(self, ):

        pass

    def Trim(self, before_first_feature=20.0, after_last_feature=10.0):
        """ Trims the eeg file """

        self.history.append("TRIM")
        pass

    def Bandpass(self, ):

        pass

    def Normalize(self, ):

        pass

    def Preprocess(self, ):

        pass
    


eeg = EEG()