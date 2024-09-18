from pydantic import BaseModel, RootModel
from typing import List, Optional


class Interface(BaseModel):
    bandwidth: Optional[str] = None
    bia: Optional[str] = None
    description: Optional[str] = None
    hardware_type: str
    interface: str
    interface_up_time: Optional[str] = None
    ip_address: Optional[str] = None
    link_status: str
    link_status_change: Optional[str] = None
    mac_address: Optional[str] = None
    mtu: str
    protocol_status: str


class InterfaceList(RootModel):
    root: List[Interface]

    @property
    def interfaces(self) -> List[Interface]:
        return self.root
