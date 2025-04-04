from datetime import timedelta

import streamlit as st
from connection import run_sql
from streamlit_extras.chart_container import chart_container

# Query data with 1-hour cache for cost metrics
df = run_sql(
    """
SELECT
    TO_VARCHAR(start_time::date, 'YYYY-MM-DD') as USAGE_DATE,
    warehouse_name as WAREHOUSE_NAME,
    SUM(credits_used) as CREDITS_USED,
    COUNT(*) as QUERY_COUNT
FROM snowflake.account_usage.warehouse_metering_history
WHERE start_time >= DATEADD('day', -7, CURRENT_TIMESTAMP())
GROUP BY 1, 2
ORDER BY 1, 2;
""",
    ttl=timedelta(hours=1),
)  # Cost data updates less frequently

st.write("Monitor your Snowflake credit usage and costs across warehouses.")

# Pivot the data for better visualization
df_pivot = df.pivot(
    index="USAGE_DATE", columns="WAREHOUSE_NAME", values="CREDITS_USED"
).fillna(0)

# Display metrics using chart container
with chart_container(df):
    # Show stacked bar chart of credits by warehouse
    st.bar_chart(df_pivot, use_container_width=True)
    st.caption("Daily Credits Used by Warehouse")

    # Show metrics
    total_credits = df["CREDITS_USED"].sum()
    total_queries = df["QUERY_COUNT"].sum()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Credits Used", f"{total_credits:.1f}")
    with col2:
        st.metric("Total Queries Run", f"{total_queries:,}")

    # Show detailed table with chart container
    st.write("### Daily Warehouse Usage Details")
    st.dataframe(
        df.pivot_table(
            index="WAREHOUSE_NAME",
            values=["CREDITS_USED", "QUERY_COUNT"],
            aggfunc="sum",
        ).round(2),
        use_container_width=True,
    )
