import pandas as pd
import mysql.connector

# Load cleaned DataFrame
file = pd.read_csv('youtube.csv')
print(file)

# Drop duplicates
file.drop_duplicates(inplace=True)

# Fill missing values
file.fillna({
    'views': 0,
    'likes': 0,
    'dislikes': 0,
    'comments': '',
}, inplace=True)

# Rename columns
file.rename(columns={
    'Channel Name': 'channel_name',
    'Youtuber Name': 'youtuber_name',
    'Total Videos': 'total_videos',
    'Best Video': 'best_video',
    'Avg Video Length (min)': 'avg_video_length_min',
    'Total Subscribers': 'total_subscribers',
    'Members Count': 'members_count',
    'AI Generated Content (%)': 'ai_generated_content_pct',
    'Neural Interface Compatible': 'neural_interface_compatible',
    'Metaverse Integration Level': 'metaverse_integration_level',
    'Quantum Computing Topics': 'quantum_topics',
    'Holographic Content Rating': 'holographic_rating',
    'Engagement Score': 'engagement_score',
    'Content Value Index': 'content_value_index'
}, inplace=True)

# Filter invalid data
file = file[(file['total_videos'] > 0) & (file['total_subscribers'] > 0)]

# Convert boolean to int if needed
file['neural_interface_compatible'] = file['neural_interface_compatible'].astype(int)

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Activa@5g",
        database="youtube2025"
    )
    cursor = conn.cursor()

# Insert query
    query = """
    INSERT INTO youtube_stats (
        channel_name, youtuber_name, total_videos, best_video,
        avg_video_length_min, total_subscribers, members_count,
        ai_generated_content_pct, neural_interface_compatible,
        metaverse_integration_level, quantum_topics,
        holographic_rating, engagement_score, content_value_index
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

# Insert all rows
    for row in file.itertuples(index=False):
        clean_row = [None if pd.isna(x) else x for x in row]
        cursor.execute(query, tuple(clean_row))

# Commit & close
    conn.commit()

except mysql.connector.Error as e:
    print(e)
finally:
    cursor.close()
    conn.close()

print("✅ Data inserted into MySQL successfully.")
