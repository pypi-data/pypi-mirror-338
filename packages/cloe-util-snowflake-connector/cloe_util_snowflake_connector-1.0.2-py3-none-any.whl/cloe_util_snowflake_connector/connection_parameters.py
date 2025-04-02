import os

import typing_extensions
from pydantic import BaseModel, field_validator


class ConnectionParameters(BaseModel):
    user: str
    password: str
    account: str
    warehouse: str
    role: str | None
    autocommit: bool = True

    @field_validator("account")
    @classmethod
    def check_account_naming(cls, value: str) -> str:
        if "snowflakecomputing.com" in value:
            raise ValueError("should not include snowflakecomputing.com")
        return value

    @classmethod
    def init_from_env_variables(cls) -> typing_extensions.Self:
        user = os.getenv("CLOE_SNOWFLAKE_USER")
        password = os.getenv("CLOE_SNOWFLAKE_PASSWORD")
        account = os.environ["CLOE_SNOWFLAKE_ACCOUNT"]
        warehouse = os.environ["CLOE_SNOWFLAKE_WAREHOUSE"]
        role = os.getenv("CLOE_SNOWFLAKE_ROLE")
        autocommit = bool(os.getenv("CLOE_SNOWFLAKE_AUTOCOMMIT", "True"))
        if user is not None and password is not None:
            return cls(
                user=user,
                password=password,
                account=account,
                warehouse=warehouse,
                role=role,
                autocommit=autocommit,
            )
        raise ValueError(
            "Unknown combination of auth CLOE_SNOWFLAKE_* env variables. Please make sure to set an accepted combination."
        )
