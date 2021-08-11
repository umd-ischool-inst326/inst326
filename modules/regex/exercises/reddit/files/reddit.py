#!/usr/bin/env python3

"""
Collect the last year of UMD Reddit data from PushShift API.
"""

import csv
import time
import requests

cols = [
  "allow_live_comments",
  "author",
  "author_fullname",
  "awarders",
  "can_mod_post",
  "contest_mode",
  "created_utc",
  "domain",
  "full_link",
  "id",
  "is_crosspostable",
  "is_meta",
  "is_original_content",
  "is_reddit_media_domain",
  "is_robot_indexable",
  "is_self",
  "is_video",
  "locked",
  "media_only",
  "no_follow",
  "num_comments",
  "num_crossposts",
  "over_18",
  "parent_whitelist_status",
  "permalink",
  "pinned",
  "pwls",
  "retrieved_on",
  "score",
  "selftext",
  "send_replies",
  "spoiler",
  "stickied",
  "subreddit",
  "subreddit_id",
  "subreddit_subscribers",
  "subreddit_type",
  "thumbnail",
  "title",
  "total_awards_received",
  "upvote_ratio",
  "url",
  "whitelist_status",
  "wls"
]

out = csv.writer(open('reddit.csv', 'w'))
out.writerow(cols)

days = 0
count = 0
while days < 365:
    days += 1
    time.sleep(1)
    url = "https://api.pushshift.io/reddit/search/submission"
    params = {
        "subreddit": "UMD",
        "after": f"{days}d",
        "before": f"{days-1}d",
        "limit": 1000
    }
    try:
        results = requests.get(url, params=params).json()['data']
        for result in results:
            out.writerow([result.get(col) for col in cols])
        print(days, len(results))
    except:
        print(f"retrying days={days}")
        days -= 1
