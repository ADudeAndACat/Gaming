import streamlit as st
import pandas as pd
import plotly.express as px
import time_test
from collections import defaultdict
import time

st.set_page_config(page_title="Dice Rolling Benchmarks", layout="wide")

st.title("🎲 Dice Rolling Performance Benchmarks")

# Sidebar controls
st.sidebar.header("Test Configuration")
num_iterations = st.sidebar.slider("Number of Iterations", min_value=1, max_value=100, value=10)
include_json = st.sidebar.checkbox("Include JSON Logging Test", value=False)

if st.button("Run Benchmarks"):
    with st.spinner("Running benchmarks..."):
        # Run benchmark comparison
        time_test.benchmark_comparison(iterations=num_iterations)
        
        # Run other tests
        if include_json:
            time_test.test_json_logging(times=num_iterations)
        time_test.test_healing_spells()
        time_test.test_edge_cases()
        
        # Get benchmark stats
        stats = time_test.benchmark_stats.times
        
        # Convert to DataFrame for visualization
        df_data = []
        for test_name, times in stats.items():
            for t in times:
                df_data.append({
                    'Test': test_name,
                    'Time (seconds)': t,
                    'Time (microseconds)': t * 1_000_000
                })
        
        df = pd.DataFrame(df_data)
        
        # Display results in different sections
        st.header("📊 Benchmark Results")
        
        # Box plot of all implementations
        st.subheader("Performance Distribution")
        fig = px.box(df, x='Test', y='Time (microseconds)', 
                    title='Distribution of Execution Times',
                    points="all")
        st.plotly_chart(fig, use_container_width=True)
        
        # Summary statistics
        st.subheader("Statistical Summary")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Mean Execution Times")
            summary_df = df.groupby('Test')['Time (microseconds)'].mean().reset_index()
            summary_df = summary_df.sort_values('Time (microseconds)')
            fig = px.bar(summary_df, x='Test', y='Time (microseconds)',
                        title='Average Execution Time by Implementation')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### Detailed Statistics")
            stats_df = df.groupby('Test')['Time (microseconds)'].agg([
                'count', 'mean', 'std', 'min', 'max'
            ]).round(3)
            st.dataframe(stats_df, use_container_width=True)
        
        # Individual implementation details
        st.subheader("Implementation Details")
        implementations = ['d', 'd20', 'roll', 'dictionary_roll']
        impl_df = df[df['Test'].isin(implementations)]
        
        fig = px.scatter(impl_df, x='Test', y='Time (microseconds)',
                        title='Individual Test Results',
                        color='Test')
        st.plotly_chart(fig, use_container_width=True)
        
        if include_json:
            st.subheader("JSON Logging Performance")
            json_df = df[df['Test'] == 'test_json_logging']
            st.line_chart(json_df.set_index('Test')['Time (microseconds)'])
