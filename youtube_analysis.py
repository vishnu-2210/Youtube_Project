import mysql.connector

# Function to establish a connection to MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",  
        user="root", 
        password="Activa@5g",  
        database="youtube2025" 
    )

# Function to perform Total Number of Videos
def total_videos(cursor):
    cursor.execute("SELECT SUM(total_videos) AS total_videos FROM youtube_stats;")
    total_videos = cursor.fetchone()[0]
    return total_videos

# Function to perform Top 3 Most Engaging Channels
def top_engaging_channels(cursor):
    cursor.execute("SELECT channel_name, engagement_score FROM youtube_stats ORDER BY engagement_score DESC LIMIT 3;")
    top_engagement = cursor.fetchall()
    print("\nTop 3 Most Engaging Channels:")
    return top_engagement

# Function to perform Average Video Length
def average_video_length(cursor):
    cursor.execute("SELECT AVG(avg_video_length_min) AS avg_video_length FROM youtube_stats;")
    avg_video_length = cursor.fetchone()[0]
    return avg_video_length

# Function to perform Average AI-Generated Content Percentage
def average_ai_content(cursor):
    cursor.execute("SELECT AVG(ai_generated_content_pct) AS avg_ai_content_pct FROM youtube_stats;")
    avg_ai_content_pct = cursor.fetchone()[0]
    return avg_ai_content_pct

# Function to perform Metaverse Integration Distribution
def metaverse_distribution(cursor):
    cursor.execute("SELECT metaverse_integration_level, COUNT(*) AS count FROM youtube_stats GROUP BY metaverse_integration_level;")
    metaverse_dist = cursor.fetchall()
    print("\nMetaverse Integration Distribution:")
    return metaverse_dist

# Function to perform Neural Interface Compatible Channels
def neural_interface_compatible(cursor):
    cursor.execute("SELECT COUNT(*) AS neural_compatible_count FROM youtube_stats WHERE neural_interface_compatible = TRUE;")
    neural_compatible_count = cursor.fetchone()[0]
    return neural_compatible_count

# Function to perform Average Content Value Index
def average_content_value(cursor):
    cursor.execute("SELECT AVG(content_value_index) AS avg_content_value FROM youtube_stats;")
    avg_content_value = cursor.fetchone()[0]
    return avg_content_value

# Function to perform Total Number of Subscribers
def total_subscribers(cursor):
    cursor.execute("SELECT SUM(total_subscribers) AS total_subscribers FROM youtube_stats;")
    total_subscribers = cursor.fetchone()[0]
    return total_subscribers

# Average subscribers per video
def average_subscribers_per_video(cursor):
    cursor.execute("""
        SELECT AVG(total_subscribers / total_videos)
        FROM youtube_stats
        WHERE total_videos > 0
    """)
    return cursor.fetchone()

# High AI content and engagement
def high_ai_engagement(cursor):
    cursor.execute("""
        SELECT channel_name, ai_generated_content_pct, engagement_score
        FROM youtube_stats
        WHERE ai_generated_content_pct > 70
        ORDER BY engagement_score DESC
    """)
    return cursor.fetchall()

# Main function to call all the analytical operations
def perform_analysis():
    conn = get_connection()
    cursor = conn.cursor()

    # Perform all operations
    total_videos(cursor)
    top_engaging_channels(cursor)
    average_video_length(cursor)
    average_ai_content(cursor)
    metaverse_distribution(cursor)
    neural_interface_compatible(cursor)
    average_content_value(cursor)
    total_subscribers(cursor)
    average_subscribers_per_video(cursor)
    high_ai_engagement(cursor)

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    perform_analysis()