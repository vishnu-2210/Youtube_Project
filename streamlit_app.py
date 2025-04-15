import streamlit as st
from youtube_analysis import (
    get_connection,
    total_videos,
    top_engaging_channels,
    average_video_length,
    average_ai_content,
    metaverse_distribution,
    neural_interface_compatible,
    average_content_value,
    total_subscribers,
    average_subscribers_per_video,
    high_ai_engagement
)

st.title("YouTube 2025 Analytics Dashboard")
option = st.sidebar.selectbox(
    "Choose an analysis:",
    (
        "Total Number of Videos",
        "Top Engaging Channels",
        "Average Video Length",
        "AI-Generated Content Percentage",
        "Metaverse Integration Distribution",
        "Neural Interface Compatible Channels",
        "Average Content Value Index",
        "Total Number of Subscribers",
        "Average Subscribers per Video",
        "High AI Content & High Engagement"
    )
)

conn = get_connection()
cursor = conn.cursor()

if option == "Total Number of Videos":
    total = total_videos(cursor)
    st.write(f"**Total Videos:** {total}")

elif option == "Top Engaging Channels":
    top_channels = top_engaging_channels(cursor)
    st.write("**Top 3 Engaging Channels:**")
    for name, score in top_channels:
        st.write(f"{name} - Engagement Score: {score}")

elif option == "Average Video Length":
    avg = average_video_length(cursor)
    st.write(f"**Average Video Length:** {avg:.2f} mins")

elif option == "AI-Generated Content Percentage":
    avg = average_ai_content(cursor)
    st.write(f"**Average AI Content:** {avg:.2f}%")

elif option == "Metaverse Integration Distribution":
    dist = metaverse_distribution(cursor)
    st.write("**Metaverse Integration Distribution:**")
    for level, count in dist:
        st.write(f"{level}: {count} channels")

elif option == "Neural Interface Compatible Channels":
    count = neural_interface_compatible(cursor)
    st.write(f"**Neural Interface Compatible Channels:** {count}")

elif option == "Average Content Value Index":
    avg = average_content_value(cursor)
    st.write(f"**Avg Content Value Index:** {avg:.2f}")

elif option == "Total Number of Subscribers":
    total = total_subscribers(cursor)
    st.write(f"**Total Subscribers:** {total}")

elif option == "Average Subscribers per Video":
    avg = average_subscribers_per_video(cursor)[0]
    st.write(f"**Avg Subscribers per Video:** {avg:.2f}")

elif option == "High AI Content & High Engagement":
    results = high_ai_engagement(cursor)
    st.write("**High AI Content + High Engagement Channels:**")
    for name, ai_pct, score in results:
        st.write(f"{name} - AI Content: {ai_pct}% - Engagement: {score}")

cursor.close()
conn.close()