import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Dummy data for illustration; replace with actual data
strikes = np.linspace(23000, 24500, 100)
call_oi = np.random.randint(0, 100, size=100)
put_oi = np.random.randint(0, 100, size=100)
profit_loss = np.maximum(0, strikes - 23600) - np.maximum(0, 23584.05 - 23600)  # Example function for profit/loss
current_price = 23584.05
current_strike = 23600

# Creating the payoff diagram using Plotly
fig = go.Figure()

# Adding the profit/loss curve
fig.add_trace(go.Scatter(
    x=strikes,
    y=profit_loss,
    mode='lines',
    name='Profit / Loss',
    line=dict(color='blue')
))

# Adding the Call and Put OI bars
fig.add_trace(go.Bar(
    x=strikes,
    y=call_oi,
    name='Call OI',
    marker_color='red',
    opacity=0.6
))

fig.add_trace(go.Bar(
    x=strikes,
    y=put_oi,
    name='Put OI',
    marker_color='green',
    opacity=0.6
))

# Adding vertical line for current price
fig.add_shape(type='line',
              x0=current_price, y0=min(profit_loss), x1=current_price, y1=max(profit_loss),
              line=dict(color='black', dash='dash'))

# Adding annotations
fig.add_annotation(x=current_price, y=0,
                   text=f"Current price: {current_price}",
                   showarrow=True, arrowhead=1, ax=-40, ay=40)

# Adding shaded regions for standard deviations (dummy values for example)
fig.add_shape(type="rect",
              x0=strikes[0], y0=min(profit_loss), x1=strikes[25], y1=max(profit_loss),
              line=dict(color="gray", width=0),
              fillcolor="red", opacity=0.1)

fig.add_shape(type="rect",
              x0=strikes[25], y0=min(profit_loss), x1=strikes[50], y1=max(profit_loss),
              line=dict(color="gray", width=0),
              fillcolor="yellow", opacity=0.1)

fig.add_shape(type="rect",
              x0=strikes[50], y0=min(profit_loss), x1=strikes[75], y1=max(profit_loss),
              line=dict(color="gray", width=0),
              fillcolor="green", opacity=0.1)

fig.add_shape(type="rect",
              x0=strikes[75], y0=min(profit_loss), x1=strikes[-1], y1=max(profit_loss),
              line=dict(color="gray", width=0),
              fillcolor="blue", opacity=0.1)

# Adding text annotations for projected loss at a specific strike price
projected_loss_strike = 23600
projected_loss_value = -8  # Example value for projected loss

fig.add_annotation(x=projected_loss_strike, y=-8,
                   text=f"Projected loss: {projected_loss_value} (-0.49%)",
                   showarrow=True, arrowhead=1, ax=-50, ay=-50)

# Customizing x-axis tick labels to show full values instead of "k"
tick_vals = np.arange(23000, 24501, 100)
tick_texts = [str(int(val)) for val in tick_vals]

fig.update_layout(
    title="Payoff Diagram",
    xaxis_title="Strike Price",
    yaxis_title="Profit / Loss",
    barmode='overlay',
    showlegend=True,
    legend=dict(x=1.05, y=1),  # Move the legend outside the plot area
    xaxis=dict(
        tickmode='array',
        tickvals=tick_vals,
        ticktext=tick_texts
    )
)

# Displaying the plot
st.plotly_chart(fig)

# Displaying additional information
st.write(f"Current price: {current_price}")
st.write(f"Projected loss: {projected_loss_value} (-0.49%)")
