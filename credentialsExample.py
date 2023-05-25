class Credentials:
    _username = ""
    _password = ""
    _host = ""
    _database = ""

    @classmethod
    def get_username(self) -> str:
        return self._username
    
    @classmethod
    def get_password(self) -> str:
        return self._password
    
    @classmethod
    def get_host(self) -> str:
        return self._host
    
    @classmethod
    def get_database(self) -> str:
        return self._database