# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .member import Member
from .._models import BaseModel

__all__ = [
    "OrganizationListResponse",
    "OrganizationListResponseItem",
    "OrganizationListResponseItemLlmBudgetTable",
    "OrganizationListResponseItemMember",
    "OrganizationListResponseItemMemberLlmBudgetTable",
    "OrganizationListResponseItemTeam",
    "OrganizationListResponseItemTeamLlmModelTable",
]


class OrganizationListResponseItemLlmBudgetTable(BaseModel):
    budget_duration: Optional[str] = None

    max_budget: Optional[float] = None

    max_parallel_requests: Optional[int] = None

    api_model_max_budget: Optional[object] = FieldInfo(alias="model_max_budget", default=None)

    rpm_limit: Optional[int] = None

    soft_budget: Optional[float] = None

    tpm_limit: Optional[int] = None


class OrganizationListResponseItemMemberLlmBudgetTable(BaseModel):
    budget_duration: Optional[str] = None

    max_budget: Optional[float] = None

    max_parallel_requests: Optional[int] = None

    api_model_max_budget: Optional[object] = FieldInfo(alias="model_max_budget", default=None)

    rpm_limit: Optional[int] = None

    soft_budget: Optional[float] = None

    tpm_limit: Optional[int] = None


class OrganizationListResponseItemMember(BaseModel):
    created_at: datetime

    organization_id: str

    updated_at: datetime

    user_id: str

    budget_id: Optional[str] = None

    llm_budget_table: Optional[OrganizationListResponseItemMemberLlmBudgetTable] = None
    """Represents user-controllable params for a LLM_BudgetTable record"""

    spend: Optional[float] = None

    user: Optional[object] = None

    user_role: Optional[str] = None


class OrganizationListResponseItemTeamLlmModelTable(BaseModel):
    created_by: str

    updated_by: str

    api_model_aliases: Union[str, object, None] = FieldInfo(alias="model_aliases", default=None)


class OrganizationListResponseItemTeam(BaseModel):
    team_id: str

    admins: Optional[List[object]] = None

    blocked: Optional[bool] = None

    budget_duration: Optional[str] = None

    budget_reset_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    llm_model_table: Optional[OrganizationListResponseItemTeamLlmModelTable] = None

    max_budget: Optional[float] = None

    max_parallel_requests: Optional[int] = None

    members: Optional[List[object]] = None

    members_with_roles: Optional[List[Member]] = None

    metadata: Optional[object] = None

    api_model_id: Optional[int] = FieldInfo(alias="model_id", default=None)

    models: Optional[List[object]] = None

    organization_id: Optional[str] = None

    rpm_limit: Optional[int] = None

    spend: Optional[float] = None

    team_alias: Optional[str] = None

    tpm_limit: Optional[int] = None


class OrganizationListResponseItem(BaseModel):
    budget_id: str

    created_at: datetime

    created_by: str

    models: List[str]

    updated_at: datetime

    updated_by: str

    llm_budget_table: Optional[OrganizationListResponseItemLlmBudgetTable] = None
    """Represents user-controllable params for a LLM_BudgetTable record"""

    members: Optional[List[OrganizationListResponseItemMember]] = None

    metadata: Optional[object] = None

    organization_alias: Optional[str] = None

    organization_id: Optional[str] = None

    spend: Optional[float] = None

    teams: Optional[List[OrganizationListResponseItemTeam]] = None


OrganizationListResponse: TypeAlias = List[OrganizationListResponseItem]
