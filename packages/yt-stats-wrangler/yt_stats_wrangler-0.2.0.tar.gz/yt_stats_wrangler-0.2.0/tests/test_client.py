import os
import pytest
from yt_stats_wrangler.api.client import YouTubeDataClient

# Use the CDCodes channel ID to test the client and ensure it's interfacing with the API

# CDCodes channel will be used for testing API access
TEST_CHANNEL_ID = 'UCB2mKxxXPK3X8SJkAc-db3A'
# CDcodes and personal channel (homedawg) used for multiple ID testing
TEST_CHANNELS = ['UCB2mKxxXPK3X8SJkAc-db3A', 'UC0pIFIthf92_8ku2NAYFG_Q']


@pytest.fixture(scope="module")
def yt_client():
    # Test that the client is able to connect with a valid API Key
    api_key = os.getenv("YOUTUBE_API_V3_KEY")
    if not api_key:
        pytest.skip("YOUTUBE_API_V3_KEY environment variable not set")
    return YouTubeDataClient(api_key=api_key)

def test_initialization(yt_client):
    assert yt_client.youtube is not None

def test_quota_initial_state(yt_client):
    yt_client.reset_quota_used()
    assert yt_client.quota_used == 0
    assert yt_client.max_quota == -1  # default unlimited

def test_get_channel_statistics(yt_client):
    result = yt_client.get_channel_statistics(TEST_CHANNEL_ID, key_format="upper", output_format="raw")
    # Check that the result is a list with one dictionary
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], dict)
    assert "CHANNEL_ID" in result[0]
    assert result[0]["CHANNEL_ID"] == TEST_CHANNEL_ID

def test_get_channel_statistics_for_channels(yt_client):
    result = yt_client.get_channel_statistics_for_channels(TEST_CHANNELS, key_format="upper", output_format="raw")

    # Check that the result is a list of dicts
    assert isinstance(result, list)
    assert len(result) >= len(TEST_CHANNELS)
    assert all(isinstance(entry, dict) for entry in result)

    # Check required fields exist
    for channel in result:
        assert "CHANNEL_ID" in channel
        assert "SUBSCRIBERS" in channel

def test_get_channel_statistics_for_channels_pandas(yt_client):
    df = yt_client.get_channel_statistics_for_channels(TEST_CHANNELS, key_format="lower", output_format="pandas")

    assert hasattr(df, "shape")
    assert "channel_id" in df.columns
    assert df.shape[0] == len(TEST_CHANNELS)

    # Test that the client finds the uploads playlist
def test_get_uploads_playlist_id(yt_client):
    playlist_id = yt_client.get_uploads_playlist_id(TEST_CHANNEL_ID)
    assert playlist_id.startswith("UU")  # Upload playlists usually start with 'UU'

    # Test that videos are being found on the channel
def test_get_all_video_details_for_channel(yt_client):
    videos = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID)
    assert isinstance(videos, list)
    assert len(videos) > 0
    assert "videoId" in videos[0]

def test_get_all_video_details_for_channels_returns_videos(yt_client):
    # Provide one or more known-good test channel IDs
    test_channels = TEST_CHANNELS  # Add more if available

    results = yt_client.get_all_video_details_for_channels(test_channels, key_format="raw")

    # Should return a list
    assert isinstance(results, list)

    if results:
        # Each result should be a dictionary with expected keys
        sample = results[0]
        assert isinstance(sample, dict)
        assert "videoId" in sample
        assert "title" in sample
        assert "publishedAt" in sample

    # Test that stats are correctly returned
def test_get_video_stats(yt_client):
    videos = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID)
    video_ids = [v["videoId"] for v in videos[:5]]  # Limit to 5 for test
    stats = yt_client.get_video_stats(video_ids)

    assert isinstance(stats, list)
    assert len(stats) > 0
    assert isinstance(stats[0], dict)
    assert "videoId" in stats[0]
    assert "viewCount" in stats[0] or "view_count" in stats[0]

def test_get_video_comments(yt_client):
    videos = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID)
    video_id = videos[0]["videoId"]  # Just one video to limit quota usage

    comments = yt_client.get_top_level_video_comments(video_id)

    assert isinstance(comments, list)
    if comments:  # Some videos may have comments disabled
        assert isinstance(comments[0], dict)
        assert "videoId" in comments[0]
        assert "author" in comments[0]
        assert "text" in comments[0]
        assert "publishedAt" in comments[0]
        assert "likeCount" in comments[0]
        assert "videoTopLevelComments_commit_time" in comments[0]


def test_quota_check_with_unlimited(yt_client):
    yt_client.reset_quota_used()
    yt_client.set_max_quota(-1)
    assert yt_client.check_quota() is True
    yt_client.quota_used = 9999
    assert yt_client.check_quota() is True

def test_quota_check_with_limit(yt_client):
    yt_client.reset_quota_used()
    yt_client.set_max_quota(5)

    yt_client.quota_used = 4
    assert yt_client.check_quota() is True

    yt_client.quota_used = 5
    assert yt_client.check_quota() is False

def test_quota_blocks_api_call(yt_client):
    yt_client.reset_quota_used()
    yt_client.set_max_quota(0)  # no calls allowed

    result = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID)
    assert result == [] or len(result) == 0
    assert yt_client.quota_used == 0

def test_get_top_level_comments_for_video_ids(yt_client):
    yt_client.reset_quota_used()
    yt_client.set_max_quota(-1)  # unlimited for testing

    # One known valid video ID (from CDcodes channel)
    valid_id = "Q6CCdCBVypg"  # You can replace with a known-valid ID if needed
    invalid_id = "invalid_video_id_123456"

    video_ids = [valid_id, invalid_id]
    comments = yt_client.get_top_level_comments_for_video_ids(video_ids)

    #  Check structure
    assert isinstance(comments, list)

    #  At least the valid one should return some comments
    assert any(comment["videoId"] == valid_id for comment in comments)

    #  The invalid one should be tracked in failed_ids
    assert hasattr(yt_client, "failed_ids_for_comments")
    assert invalid_id in yt_client.failed_ids_for_comments

def test_get_all_video_details_for_channel_key_format(yt_client):
    results = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID, key_format="lower")
    assert "video_id" in results[0]

    results = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID, key_format="upper")
    assert "VIDEO_ID" in results[0]

    results = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID, key_format="mixed")
    assert "video_Id" in results[0]

    results = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID, key_format="raw")
    assert "videoId" in results[0]

    with pytest.raises(ValueError):
        yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID, key_format="invalid")

def test_get_video_stats_key_format(yt_client):
    video_ids = [v["videoId"] for v in yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID)[:1]]

    # Test lower
    result = yt_client.get_video_stats(video_ids, key_format="lower")
    assert "video_id" in result[0]

    # Test upper
    result = yt_client.get_video_stats(video_ids, key_format="upper")
    assert "VIDEO_ID" in result[0]

    # Test mixed
    result = yt_client.get_video_stats(video_ids, key_format="mixed")
    assert "video_Id" in result[0]

    # Test raw
    result = yt_client.get_video_stats(video_ids, key_format="raw")
    assert "videoId" in result[0]

    # Test invalid format
    with pytest.raises(ValueError):
        yt_client.get_video_stats(video_ids, key_format="camel")

def test_get_top_level_video_comments_key_format(yt_client):
    video_ids = [v["videoId"] for v in yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID)[:1]]
    video_id = video_ids[0]

    result = yt_client.get_top_level_video_comments(video_id, key_format="lower")
    if result:  # if there are comments
        assert "video_id" in result[0]

    result = yt_client.get_top_level_video_comments(video_id, key_format="upper")
    if result:
        assert "VIDEO_ID" in result[0]

    result = yt_client.get_top_level_video_comments(video_id, key_format="mixed")
    if result:
        assert "video_Id" in result[0]

    result = yt_client.get_top_level_video_comments(video_id, key_format="raw")
    if result:
        assert "videoId" in result[0]

    with pytest.raises(ValueError):
        yt_client.get_top_level_video_comments(video_id, key_format="💥")

def test_get_top_level_comments_for_video_ids_key_format(yt_client):
    video_ids = [v["videoId"] for v in yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID)[:1]]

    result = yt_client.get_top_level_comments_for_video_ids(video_ids, key_format="lower")
    if result:
        assert "video_id" in result[0]

    result = yt_client.get_top_level_comments_for_video_ids(video_ids, key_format="mixed")
    if result:
        assert "video_Id" in result[0]

    result = yt_client.get_top_level_comments_for_video_ids(video_ids, key_format="raw")
    if result:
        assert "videoId" in result[0]

    with pytest.raises(ValueError):
        yt_client.get_top_level_comments_for_video_ids(video_ids, key_format="WRONG")

def test_get_all_video_details_for_channels_key_format(yt_client):
    # Use a small number of test channels (ideally with at least 1 video each)
    test_channels = TEST_CHANNELS  # Add more if needed

    # lower case
    result = yt_client.get_all_video_details_for_channels(test_channels, key_format="lower")
    if result:
        assert "video_id" in result[0]
        assert all("video_id" in vid for vid in result)

    # upper case
    result = yt_client.get_all_video_details_for_channels(test_channels, key_format="upper")
    if result:
        assert "VIDEO_ID" in result[0]

    # mixed case
    result = yt_client.get_all_video_details_for_channels(test_channels, key_format="mixed")
    if result:
        assert "video_Id" in result[0]

    # raw case (original YouTube keys)
    result = yt_client.get_all_video_details_for_channels(test_channels, key_format="raw")
    if result:
        assert "videoId" in result[0]

    # invalid format - Ids should be stored in the failed channel ids list
    yt_client.get_all_video_details_for_channels(test_channels, key_format="camelCase")
    assert test_channels[0] in yt_client.failed_channel_ids


def test_get_channel_id_from_handle(yt_client):
    # Skip if the quota isn't sufficient AND the client is not set to unlimited (-1)
    if yt_client.max_quota != -1 and yt_client.get_remaining_quota() < 100:
        pytest.skip("Not enough quota to run handle-based test")

    handle = "@cdcodes"
    channel_id = yt_client.get_channel_id_from_handle(handle)

    assert isinstance(channel_id, str)
    assert channel_id.startswith("UC")


def test_get_channel_ids_from_handles(yt_client):
    if yt_client.max_quota != -1 and yt_client.get_remaining_quota() < 200:
        pytest.skip("Not enough quota to test multiple handles")

    handles = ["@cdcodes", "@homedawg_yt"]
    channel_ids = yt_client.get_channel_ids_from_handles(handles)

    assert isinstance(channel_ids, list)
    assert len(channel_ids) == len(handles)
    for cid in channel_ids:
        assert isinstance(cid, str)
        assert cid.startswith("UC")

def test_get_replies_to_comment(yt_client):
    yt_client.reset_quota_used()
    yt_client.set_max_quota(100)

    # First, find a video with comments and replies
    videos = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID)
    video_id = videos[0]["videoId"]
    top_comments = yt_client.get_top_level_video_comments(video_id)

    # Find a top-level comment that has replies
    comment_with_replies = None
    for comment in top_comments:
        if comment.get("replyCount", 0) > 0:
            comment_with_replies = comment
            break

    if not comment_with_replies:
        pytest.skip("No comment with replies found")

    comment_id = comment_with_replies["commentId"]

    replies = yt_client.get_replies_to_comment(comment_id)

    assert isinstance(replies, list)
    if replies:
        reply = replies[0]
        assert isinstance(reply, dict)
        assert "commentId" in reply
        assert "parentId" in reply
        assert reply["parentId"] == comment_id

def test_get_all_video_comments(yt_client):
    yt_client.reset_quota_used()
    yt_client.set_max_quota(100)

    videos = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID)
    video_id = videos[0]["videoId"]  # Take the first video

    comments = yt_client.get_all_video_comments(video_id, key_format="upper", output_format="raw")

    assert isinstance(comments, list)
    if comments:
        first_comment = comments[0]
        assert isinstance(first_comment, dict)
        assert "COMMENT_ID" in first_comment
        assert "VIDEO_ID" in first_comment
        assert "PARENT_ID" in first_comment


def test_get_all_comments_for_video_ids(yt_client):
    yt_client.reset_quota_used()
    yt_client.set_max_quota(150)

    videos = yt_client.get_all_video_details_for_channel(TEST_CHANNEL_ID)
    video_ids = [v["videoId"] for v in videos[:2]]  # Limit to 2 videos for test

    all_comments = yt_client.get_all_comments_for_video_ids(video_ids, key_format="upper", output_format="raw")

    assert isinstance(all_comments, list)
    if all_comments:
        comment = all_comments[0]
        assert isinstance(comment, dict)
        assert "COMMENT_ID" in comment
        assert "VIDEO_ID" in comment
        assert "PARENT_ID" in comment



