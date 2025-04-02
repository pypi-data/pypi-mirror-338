from datetime import timedelta

import streamlit as st
from connection import run_sql
from streamlit_extras.chart_container import chart_container

# Query data with 30-minute cache for weekly metrics
df = run_sql(
    """
SELECT
    TO_VARCHAR(start_time::date, 'YYYY-MM-DD') as QUERY_DATE,
    COUNT(*) as QUERY_COUNT,
    AVG(execution_time) / 1000 as AVG_EXECUTION_TIME_S,
    SUM(bytes_scanned) / POWER(1024, 3) as GB_SCANNED
FROM snowflake.account_usage.query_history
WHERE start_time >= DATEADD('day', -7, CURRENT_TIMESTAMP())
GROUP BY 1
ORDER BY 1;
""",
    ttl=timedelta(minutes=30),
)

st.write("Track your Snowflake query performance and resource utilization over time.")

# Display metrics using chart container
with chart_container(df):
    col1, col2 = st.columns(2)

    with col1:
        st.line_chart(
            df.set_index("QUERY_DATE")["QUERY_COUNT"], use_container_width=True
        )
        st.caption("Daily Query Count")

    with col2:
        st.line_chart(
            df.set_index("QUERY_DATE")["AVG_EXECUTION_TIME_S"], use_container_width=True
        )
        st.caption("Average Execution Time (seconds)")

    st.area_chart(df.set_index("QUERY_DATE")["GB_SCANNED"], use_container_width=True)
    st.caption("Data Scanned (GB)")
