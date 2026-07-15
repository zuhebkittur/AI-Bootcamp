import plotly.express as px


def create_task_minutes_chart(df):
    """
    Creates a bar chart showing minutes spent on each task.
    """

    chart_data = (
        df.groupby("Task")["Total Minutes"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        chart_data,
        x="Task",
        y="Total Minutes",
        text="Total Minutes",
        title="Minutes Spent by Task"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Task",
        yaxis_title="Minutes",
        height=450
    )

    return fig


def create_task_distribution_chart(df):
    """
    Creates a pie chart showing task distribution.
    """

    chart_data = (
        df.groupby("Task")["Total Minutes"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        chart_data,
        names="Task",
        values="Total Minutes",
        title="Task Distribution"
    )

    return fig