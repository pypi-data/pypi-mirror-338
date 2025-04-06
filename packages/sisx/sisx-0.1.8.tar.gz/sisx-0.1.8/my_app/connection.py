from datetime import timedelta
from typing import Optional

import pandas as pd
import streamlit as st
from snowflake.snowpark import Session


def _get_session() -> Session:
    if "snowpark_session" not in st.session_state:
        connection = st.connection("snowflake")
        st.session_state["snowpark_session"] = connection.session()
    return st.session_state["snowpark_session"]


def _run_sql(query: str) -> pd.DataFrame:
    return _get_session().sql(query).to_pandas()


def run_sql(query: str, ttl: Optional[timedelta] = timedelta(hours=2)):
    """
    Execute a SQL query and cache the results.

    Args:
        query: The SQL query to execute
        ttl: Time-to-live for the cache. Defaults to 2 hours.
            Set to None to use the default cache invalidation.

    Returns:
        pandas.DataFrame: The query results as a pandas DataFrame
    """

    return st.cache_data(ttl=ttl)(_run_sql)(query)
