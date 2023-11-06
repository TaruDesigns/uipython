from dataclasses import dataclass

from .secrets import UIP_CLIENT_ID, UIP_CLIENT_SECRET

@dataclass
class Settings():
    # UIPApiSecrets
    UIP_CLIENT_ID: str
    UIP_CLIENT_SECRET: str
    UIP_SCOPE: str = "OR.Assets OR.Execution OR.BackgroundTasks OR.Folders OR.Jobs OR.Machines OR.Monitoring OR.Queues OR.Robots OR.Settings OR.Tasks OR.Users OR.Webhooks OR.TestDataQueues"
    UIP_GRANT_TYPE: str = "client_credentials"
    UIP_LOGICAL_NAME: str = "jcaravaca42"
    UIP_TENANT: str = "jorge_pruebas"
    UIP_HOST: str = ""
    
    def get_host(self) -> str:
        """Gets Full Host URL based on Logical Name and Tenant. If UIP_HOST is not provided, it will be assumed it's a cloud tenant
        """
        if self.UIP_HOST and  "cloud" not in self.UIP_HOST:
            return self.UIP_HOST
        else:
            return f"https://cloud.uipath.com/{self.UIP_LOGICAL_NAME}/{self.UIP_TENANT}/orchestrator_"
    
    def get_auth_url(self) -> str:
        """Gets Token (auth) URL based on host
        """
        if self.UIP_HOST:
            return f"{self.UIP_HOST}/identity/connect/token"
        else:
            return "https://cloud.uipath.com/identity_/connect/token"
            
    
UIP_HOST: str = ""
UIP_LOGICAL_NAME: str = "jcaravaca42"
UIP_TENANT: str = "jorge_pruebas"
settings = Settings(UIP_CLIENT_ID=UIP_CLIENT_ID, UIP_CLIENT_SECRET=UIP_CLIENT_SECRET,
                    UIP_HOST=UIP_HOST, UIP_LOGICAL_NAME=UIP_LOGICAL_NAME, UIP_TENANT=UIP_TENANT)
