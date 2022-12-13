from pydantic import BaseModel, Field, validator

from hpctl import utils


class _Resource(BaseModel):
    cpus: int = Field(0, alias="ncpus")
    gpus: int = Field(0, alias="ngpus")
    mem: str = Field(0)

    @validator("mem")
    def convert_mem(cls, val):
        return utils.convert_raw_bytes(val)


class _NodeInfo(BaseModel):
    type: str = Field("-", alias="node_type")
    loc: str = Field("-", alias="dloc")
    arch: str = "-"
    cpu_type: str = "-"
    network: str = "-"


class Node(BaseModel):
    fqdn: str = Field("-", alias="Mom")
    state: str = "-"
    comment: str = "-"
    queue: str = "-"
    info: _NodeInfo = Field(None, alias="resources_available")
    resources_available: _Resource = None
    resources_assigned: _Resource = None
    jobs: list[str] = Field(default_factory=[])


class Nodes(BaseModel):
    nodes: list = Field(default_factory=[])
