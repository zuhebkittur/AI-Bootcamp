import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# Productivity Gauge
# ==========================================================

def create_productivity_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,

            title={
                "text": "Productivity Score"
            },

            gauge={
                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": "darkblue"
                },

                "steps": [

                    {
                        "range": [0, 50],
                        "color": "#ffcccc"
                    },

                    {
                        "range": [50, 75],
                        "color": "#fff4cc"
                    },

                    {
                        "range": [75, 100],
                        "color": "#ccffcc"
                    }

                ],

                "threshold": {

                    "line": {
                        "color": "red",
                        "width": 4
                    },

                    "thickness": 0.8,

                    "value": score
                }
            }
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    return fig


# ==========================================================
# Minutes by Task
# ==========================================================
def create_task_minutes_chart(df):

    chart_data = (
        df.groupby("Task", as_index=False)["Total Minutes"]
        .sum()
        .sort_values("Total Minutes", ascending=True)
    )

    fig = px.bar(
        chart_data,
        x="Total Minutes",
        y="Task",
        orientation="h",
        text="Total Minutes",
        title="📊 Minutes Spent by Task"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        xaxis_title="Minutes",
        yaxis_title="Task"
    )

    return fig

# ==========================================================
# Task Distribution
# ==========================================================

def create_task_distribution_chart(df):

    chart_data = (
        df.groupby("Task")["Total Minutes"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        chart_data,
        names="Task",
        values="Total Minutes",
        hole=0.60,
        title="🍩 Task Distribution"
    )

    fig.update_traces(
        textinfo="percent+label"
    )

    fig.update_layout(
        height=450,
        template="plotly_white",
        margin=dict(l=20, r=20, t=60, b=20),
        legend_title="Tasks"
    )

    return fig