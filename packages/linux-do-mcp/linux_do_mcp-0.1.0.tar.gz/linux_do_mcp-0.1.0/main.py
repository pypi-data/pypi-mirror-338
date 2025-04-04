import os
import copy
import json
import httpx
from asyncio import sleep
from typing import Dict, List, Optional, Any, Union, Literal
from mcp.server.fastmcp import FastMCP, Context

mcp = FastMCP("linux-do-mcp")
username = os.getenv('LINUX_DO_USERNAME')
api_key = os.getenv('LINUX_DO_API_KEY')

# Maps for category and notification types
CATEGORY_MAP = {
    "Feedback": 2,
    "Development": 4,
    "Flea Market": 10,
    "Off-Topic": 11,
    "Resources": 14,
    "Job Market": 27,
    "Book Club": 32,
    "News Flash": 34,
    "Benefits": 36,
    "Documentation": 42,
    "Set Sail": 46,
    "Web Archive": 92,
}

NOTIFICATION_TYPE_MAP = {
    "mentioned": 1,
    "replied": 2,
    "quoted": 3,
    "edited": 4,
    "liked": 5,
    "private_message": 6,
    "invited_to_private_message": 7,
    "invitee_accepted": 8,
    "posted": 9,
    "moved_post": 10,
    "linked": 11,
    "granted_badge": 12,
    "invited_to_topic": 13,
    "custom": 14,
    "group_mentioned": 15,
    "group_message_summary": 16,
    "watching_first_post": 17,
    "topic_reminder": 18,
    "liked_consolidated": 19,
    "post_approved": 20,
    "code_review_commit_approved": 21,
    "membership_request_accepted": 22,
    "membership_request_consolidated": 23,
    "bookmark_reminder": 24,
    "reaction": 25,
    "votes_released": 26,
    "event_reminder": 27,
    "event_invitation": 28,
    "chat_mention": 29,
    "chat_message": 30,
    "chat_invitation": 31,
    "chat_group_mention": 32,
    "chat_quoted": 33,
    "assigned": 34,
    "question_answer_user_commented": 35,
    "watching_category_or_tag": 36,
    "new_features": 37,
    "admin_problems": 38,
    "linked_consolidated": 39,
    "chat_watched_thread": 40,
    "following": 800,
    "following_created_topic": 801,
    "following_replied": 802,
    "circles_activity": 900,
}

NOTIFICATION_MAP = {
    "reply": "mentioned,group_mentioned,posted,quoted,replied",
    "like": "liked,liked_consolidated,reaction",
    "other": "edited,invited_to_private_message,invitee_accepted,moved_post,linked,granted_badge,invited_to_topic,custom,watching_first_post,topic_reminder,post_approved,code_review_commit_approved,membership_request_accepted,membership_request_consolidated,votes_released,event_reminder,event_invitation,chat_group_mention,assigned,question_answer_user_commented,watching_category_or_tag,new_features,admin_problems,linked_consolidated,following,following_created_topic,following_replied,circles_activity"
}

# Helper functions to format responses
def format_topic_response(data: Dict) -> Dict:
    return {
        "content": [{
            "type": "text",
            "text": json.dumps({
                "topics": [{
                    "title": topic["title"],
                    "created_at": topic["created_at"],
                    "url": f"https://linux.do/t/{topic['id']}",
                    "poster": next((user["username"] for user in data["users"] 
                                   if user["id"] == topic["posters"][0]["user_id"]), "某位佬友")
                } for topic in data["topic_list"]["topics"]]
            }, indent=2)
        }],
        "isError": False
    }

def format_search_response(data: Dict) -> Dict:
    return {
        "content": [{
            "type": "text",
            "text": json.dumps({
                "topics": [{
                    "title": topic["fancy_title"],
                    "created_at": topic["created_at"],
                    "url": f"https://linux.do/t/{topic['id']}",
                } for topic in data["topics"]],
                "posts": [{
                    "username": post["username"],
                    "created_at": post["created_at"],
                    "like_count": post["like_count"],
                    "url": f"https://linux.do/t/{post['topic_id']}"
                } for post in data["posts"]]
            }, indent=2)
        }],
        "isError": False
    }

def format_category_topic_response(data: Dict, category_id: int) -> Dict:
    filtered_topics = [
        topic for topic in data["topic_list"]["topics"] 
        if topic.get("category_id") == category_id
    ][:5]
    
    category_name = next((category["name"] for category in data["category_list"]["categories"] 
                         if category["id"] == category_id), "未知分类")
    
    return {
        "content": [{
            "type": "text",
            "text": json.dumps({
                "category": category_name,
                "topics": [{
                    "title": topic["title"],
                    "created_at": topic["created_at"],
                    "url": f"https://linux.do/t/{topic['id']}",
                    "poster": next((user["name"] for user in data["users"] 
                                  if user["id"] == topic["posters"][0]["user_id"]), "某位佬友")
                } for topic in filtered_topics]
            }, indent=2)
        }],
        "isError": False
    }

def format_notification_response(data: Dict) -> Dict:
    formatted_notifications = []
    
    for notification in data["notifications"]:
        notification_type = next(
            (key for key, value in NOTIFICATION_TYPE_MAP.items() 
             if value == notification["notification_type"]), "unknown"
        )
        
        username = notification["data"].get("display_username", "") or notification.get("acting_user_name", "")
        title = notification.get("fancy_title", "") or notification["data"].get("topic_title", "")
        message = notification["data"].get("message", "")
        
        # Handle specific notification types
        if "个回复" in username:
            message = username
            username = "系统通知"
        
        if (notification["notification_type"] == NOTIFICATION_TYPE_MAP["granted_badge"] and 
            notification["data"].get("badge_name")):
            message = f"获得了 \"{notification['data']['badge_name']}\" 徽章"
        
        formatted_notifications.append({
            "username": username,
            "title": title,
            "notification_type": notification_type,
            "message": message,
            "created_at": notification["created_at"],
            "read": notification["read"]
        })
    
    return {
        "content": [{
            "type": "text",
            "text": json.dumps({"notifications": formatted_notifications}, indent=2)
        }],
        "isError": False
    }

def format_bookmark_response(data: Dict) -> Dict:
    return {
        "content": [{
            "type": "text",
            "text": json.dumps({
                "bookmarks": [{
                    "title": bookmark.get("topic_title", ""),
                    "created_at": bookmark["created_at"],
                    "url": bookmark["bookmarkable_url"],
                    "username": bookmark.get("user", {}).get("username", "某位佬友")
                } for bookmark in data["bookmarks"]]
            }, indent=2)
        }],
        "isError": False
    }

def format_private_message_response(data: Dict) -> Dict:
    return {
        "content": [{
            "type": "text",
            "text": json.dumps({
                "messages": [{
                    "title": topic["title"],
                    "created_at": topic["created_at"],
                    "url": f"https://linux.do/t/{topic['id']}",
                    "last_poster": next((user["name"] for user in data["users"] 
                                       if user["id"] == topic["posters"][0]["user_id"]), "某位佬友")
                } for topic in data["topic_list"]["topics"]]
            }, indent=2)
        }],
        "isError": False
    }

# API request helper function
async def fetch_linux_do_api(endpoint: str, params: Dict = None, requires_auth: bool = False) -> Dict:
    if params is None:
        params = {}
    
    url = f"https://linux.do/{endpoint}"
    
    headers = {}
    if requires_auth:
        headers["User-Api-Key"] = api_key
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=headers)
        response.raise_for_status()
        
        return response.json()

# Generic topic handler
async def handle_topic_endpoint(endpoint: str, params: Dict = None, requires_auth: bool = False) -> Dict:
    if params is None:
        params = {}
    
    period = params.get("period", "")
    api_path = f"{endpoint}/{period}.json" if period else f"{endpoint}.json"
    
    api_params = {
        "page": params.get("page", 1),
        "per_page": params.get("per_page", 10)
    }
    
    data = await fetch_linux_do_api(api_path, api_params, requires_auth)
    return format_topic_response(data)

# Tool implementations
@mcp.tool(
    name="latest_topic",
    description="获取Linux.do有新帖子的话题",
    schema={
        "type": "object",
        "properties": {
            "page": {
                "type": "number",
                "description": "页码，默认为1"
            },
            "per_page": {
                "type": "number",
                "description": "每页条数，默认为10"
            }
        }
    }
)
async def latest_topic(ctx: Context, page: int = 1, per_page: int = 10) -> Dict:
    return await handle_topic_endpoint("latest", {"page": page, "per_page": per_page})

@mcp.tool(
    name="top_topic",
    description="获取Linux.do过去一年一月一周一天中最活跃的话题",
    schema={
        "type": "object",
        "properties": {
            "period": {
                "type": "string",
                "enum": ["daily", "weekly", "monthly", "quarterly", "yearly", "all"],
                "description": "时间周期：每日/每周/每月/每年/全部"
            },
            "page": {
                "type": "number",
                "description": "页码，默认为1"
            },
            "per_page": {
                "type": "number",
                "description": "每页条数，默认为10"
            }
        },
        "required": ["period"]
    }
)
async def top_topic(ctx: Context, period: str, page: int = 1, per_page: int = 10) -> Dict:
    return await handle_topic_endpoint("top", {"period": period, "page": page, "per_page": per_page})

@mcp.tool(
    name="hot_topic",
    description="获取Linux.do最近热门话题",
    schema={
        "type": "object",
        "properties": {
            "page": {
                "type": "number",
                "description": "页码，默认为1"
            },
            "per_page": {
                "type": "number",
                "description": "每页条数，默认为10"
            }
        }
    }
)
async def hot_topic(ctx: Context, page: int = 1, per_page: int = 10) -> Dict:
    return await handle_topic_endpoint("hot", {"page": page, "per_page": per_page})

@mcp.tool(
    name="category_topic",
    description="获取Linux.do特定分类下的话题",
    schema={
        "type": "object",
        "properties": {
            "category": {
                "type": "string",
                "enum": ["Development", "Resources", "Documentation", "Flea Market",
                    "Job Market", "Book Club", "Set Sail", "News Flash",
                    "Web Archive", "Benefits", "Off-Topic", "Feedback"],
                "description": "话题分类名称"
            },
            "page": {
                "type": "number",
                "description": "页码，默认为1"
            },
            "per_page": {
                "type": "number",
                "description": "每页条数，默认为10"
            }
        },
        "required": ["category"]
    }
)
async def category_topic(ctx: Context, category: str, page: int = 1, per_page: int = 10) -> Dict:
    category_id = CATEGORY_MAP.get(category)
    if not category_id:
        return {
            "content": [{"type": "text", "text": "Invalid category"}],
            "isError": True
        }
    
    api_params = {
        "page": page,
        "per_page": 50  # Request more to ensure we have enough after filtering
    }
    
    data = await fetch_linux_do_api("categories_and_latest", api_params)
    return format_category_topic_response(data, category_id)

@mcp.tool(
    name="new_topic",
    description="获取Linux.do最近几天创建的话题",
    schema={
        "type": "object",
        "properties": {
            "page": {
                "type": "number",
                "description": "页码，默认为1"
            },
            "per_page": {
                "type": "number",
                "description": "每页条数，默认为10"
            }
        }
    }
)
async def new_topic(ctx: Context, page: int = 1, per_page: int = 10) -> Dict:
    return await handle_topic_endpoint("new", {"page": page, "per_page": per_page}, True)

@mcp.tool(
    name="unread_topic",
    description="获取Linux.do您当前正在关注或追踪，具有未读帖子的话题",
    schema={
        "type": "object",
        "properties": {
            "page": {
                "type": "number",
                "description": "页码，默认为1"
            },
            "per_page": {
                "type": "number",
                "description": "每页条数，默认为10"
            }
        }
    }
)
async def unread_topic(ctx: Context, page: int = 1, per_page: int = 10) -> Dict:
    return await handle_topic_endpoint("unread", {"page": page, "per_page": per_page}, True)

@mcp.tool(
    name="unseen_topic",
    description="获取Linux.do新话题和您当前正在关注或追踪，具有未读帖子的话题",
    schema={
        "type": "object",
        "properties": {
            "page": {
                "type": "number",
                "description": "页码，默认为1"
            },
            "per_page": {
                "type": "number",
                "description": "每页条数，默认为10"
            }
        }
    }
)
async def unseen_topic(ctx: Context, page: int = 1, per_page: int = 10) -> Dict:
    return await handle_topic_endpoint("unseen", {"page": page, "per_page": per_page}, True)

@mcp.tool(
    name="post_topic",
    description="获取Linux.do您发过帖子的话题",
    schema={
        "type": "object",
        "properties": {
            "page": {
                "type": "number",
                "description": "页码，默认为1"
            },
            "per_page": {
                "type": "number",
                "description": "每页条数，默认为10"
            }
        }
    }
)
async def post_topic(ctx: Context, page: int = 1, per_page: int = 10) -> Dict:
    return await handle_topic_endpoint("posted", {"page": page, "per_page": per_page}, True)

@mcp.tool(
    name="topic_search",
    description="搜索Linux.do论坛上的话题",
    schema={
        "type": "object",
        "properties": {
            "term": {
                "type": "string",
                "description": "搜索关键词"
            },
        },
        "required": ["term"]
    }
)
async def topic_search(ctx: Context, term: str) -> Dict:
    if not term:
        return {
            "content": [{"type": "text", "text": "Search term is required"}],
            "isError": True
        }
    
    api_params = {"term": term}
    data = await fetch_linux_do_api("search/query.json", api_params)
    return format_search_response(data)

@mcp.tool(
    name="new_notification",
    description="获取Linux.do您最近的未读通知",
    schema={
        "type": "object",
        "properties": {
            "limit": {
                "type": "number",
                "description": "获取的通知数量，默认为30"
            },
            "read": {
                "type": "boolean",
                "description": "是否已读，默认为false"
            },
            "filter_by_types": {
                "type": "array",
                "items": {
                    "type": "string",
                    "enum": ["reply", "like", "other"]
                },
                "description": "过滤通知类型，默认为所有类型"
            },
        }
    }
)
async def new_notification(ctx: Context, limit: int = 10, read: bool = False, filter_by_types: List[str] = None) -> Dict:
    api_params = {
        "limit": limit,
        "recent": "true",
        "bump_last_seen_reviewable": "true"
    }
    
    if filter_by_types:
        mapped_types = []
        for filter_type in filter_by_types:
            if filter_type in NOTIFICATION_MAP:
                mapped_types.extend(NOTIFICATION_MAP[filter_type].split(","))
        
        if mapped_types:
            api_params["filter_by_types"] = ",".join(mapped_types)
            api_params["silent"] = "true"
    
    data = await fetch_linux_do_api("notifications.json", api_params, True)
    return format_notification_response(data)

@mcp.tool(
    name="my_bookmark",
    description="获取Linux.do您收藏的帖子",
    schema={
        "type": "object",
        "properties": {}
    }
)
async def my_bookmark(ctx: Context) -> Dict:
    data = await fetch_linux_do_api(f"u/{username}/user-menu-bookmarks.json", {}, True)
    return format_bookmark_response(data)

@mcp.tool(
    name="my_private_message",
    description="获取Linux.do您收到的私信",
    schema={
        "type": "object",
        "properties": {}
    }
)
async def my_private_message(ctx: Context) -> Dict:
    data = await fetch_linux_do_api(f"topics/private-messages/{username}.json", {}, True)
    return format_private_message_response(data)

if __name__ == "__main__":
    mcp.run()