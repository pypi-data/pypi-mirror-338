from datetime import timedelta

import streamlit as st
from connection import run_sql
from streamlit_extras.chart_container import chart_container

# Query data with 15-minute cache for recent activity
df = run_sql(
    """
SELECT
    warehouse_name as WAREHOUSE_NAME,
    COUNT(*) as QUERY_COUNT,
    AVG(execution_time) / 1000 as AVG_EXECUTION_TIME_S,
    SUM(bytes_scanned) / POWER(1024, 3) as GB_SCANNED
FROM snowflake.account_usage.query_history
WHERE start_time >= DATEADD('hour', -24, CURRENT_TIMESTAMP())
GROUP BY 1
ORDER BY 2 DESC;
""",
    ttl=timedelta(minutes=15),
)  # More frequent updates for recent activity

st.write(
    "Welcome to your Snowflake monitoring dashboard! Use the navigation to explore different views."
)

# Display overview metrics
st.write("### 24 Hour Activity Overview")
with chart_container(df):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Queries", f"{df['QUERY_COUNT'].sum():,}")

    with col2:
        st.metric("Avg Execution Time", f"{df['AVG_EXECUTION_TIME_S'].mean():.1f}s")

    with col3:
        st.metric("Data Scanned", f"{df['GB_SCANNED'].sum():.1f} GB")

    # Show warehouse activity breakdown
    st.write("### Warehouse Activity")
    st.bar_chart(
        df.set_index("WAREHOUSE_NAME")[["QUERY_COUNT"]], use_container_width=True
    )

# Example of longer cache for historical trends
historical_df = run_sql(
    """
SELECT
    DATE_TRUNC('day', start_time) as DATE,
    COUNT(*) as QUERY_COUNT,
    SUM(bytes_scanned) / POWER(1024, 4) as TB_SCANNED
FROM snowflake.account_usage.query_history
WHERE start_time >= DATEADD('day', -30, CURRENT_TIMESTAMP())
GROUP BY 1
ORDER BY 1;
""",
    ttl=timedelta(hours=6),
)  # Longer cache for historical data

st.write("### 30 Day Trends")
tab1, tab2 = st.tabs(["Query Volume", "Data Scanned"])

with tab1:
    st.line_chart(
        historical_df.set_index("DATE")[["QUERY_COUNT"]], use_container_width=True
    )

with tab2:
    st.line_chart(
        historical_df.set_index("DATE")[["TB_SCANNED"]], use_container_width=True
    )
