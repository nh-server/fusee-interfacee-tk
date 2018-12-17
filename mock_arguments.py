class MockArguments():
    # Simple data class to fake command line arguments

    def __init__(self):
        self.payload = ""
        self.wait    = True
        self.vid     = None
        self.pid     = None
        self.platform  = None
        self.relocator = ""
        self.skip_checks   = True
        self.permissive_id = True