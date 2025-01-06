class FileDBError(Exception):
    def __init__(self, err):
        super().__init__("The internal fileassociation db errored out with \""+err+"\". Reinstalling Process might be advised.")