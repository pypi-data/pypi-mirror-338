from pydantic import ConfigDict, Field

from apolo_app_types.protocols.common.abc_ import AbstractAppFieldType
from apolo_app_types.protocols.common.schema_extra import (
    SchemaExtraMetadata,
)


class IngressGrpc(AbstractAppFieldType):
    enabled: bool


class Ingress(AbstractAppFieldType):
    model_config = ConfigDict(
        protected_namespaces=(),
        json_schema_extra=SchemaExtraMetadata(
            title="Ingress",
            description="Configuration for Ingress.",
        ).as_json_schema_extra(),
    )
    enabled: bool = Field(
        ...,
        description="Indicates whether the ingress is enabled.",
        title="Ingress Enabled",
    )
    clusterName: str = Field(  # noqa: N815
        ...,
        description="The name of the cluster where the ingress is deployed.",
        title="Cluster Name",
    )
    grpc: IngressGrpc | None = Field(default=None, title="Enable GRPC")
    http_auth: bool = Field(
        default=False,
        title="Enable Platform Authentication",
        description="Enable/disable HTTP authentication",
    )
