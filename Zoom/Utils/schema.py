Schemas = {
    "Users.list": {
        "type": "object",
        "properties": {
            "status": {
                "type": "string",
                "enum": [
                    "active",
                    "inactive",
                    "pending"
                ],
                "title": "status",
                "description": "User statuses:<br>`active` - Users with an active status.<br>`inactive` - Users with an inactive status.<br>`pending` - Users with a pending status.",
                "default": ""
            },
            "page_size": {
                "type": "integer",
                "description": "The number of records returned within a single API call.",
                "default": 0,
                "maximum": 300
            },
            "page_number": {
                "type": "integer",
                "title": "page_number",
                "description": "The current page number of returned records.",
                "default": 0
            },
            "role_id": {
                "type": "string",
                "description": "Unique identifier for the role. Provide this parameter if you would like to filter the response by a specific role. You can retrieve Role IDs from [List Roles](https://marketplace.zoom.us/docs/api-reference/zoom-api/roles/roles) API. "
            }
        }
    },
    "Users.meetings": {
        "type": "object",
        "required": [
            "userId"
        ],
        "properties": {
            "userId": {
                "type": "string",
                "description": "The user ID or email address of the user."
            },
            "type": {
                "type": "string",
                "enum": [
                    "scheduled",
                    "live",
                    "upcoming"
                ],
                "description": "The meeting types: <br>`scheduled` - All the scheduled meetings.<br>`live` - All the live meetings.<br>`upcoming` - All the upcoming meetings.",
                "default": ""
            },
            "page_size": {
                "type": "integer",
                "description": "The number of records returned within a single API call.",
                "default": 0,
                "maximum": 300
            },
            "page_number": {
                "type": "integer",
                "description": "The current page number of returned records.",
                "default": 0
            }
        }
    },
    "Meetings.get": {
        "type": "object",
        "properties": {
            "meetingId": {
                "type": "integer",
                "description": "The meeting ID."
            },
            "occurrence_id": {
                "type": "string",
                "description": "Meeting occurrence id"
            }
        },
        "required": [
            "meetingId"
        ]
    },
    "PastMeetings.details": {
        "type": "object",
        "properties": {
            "meetingId": {
                "type": "integer",
                "description": "The meeting ID."
            }
        },
        "required": [
            "meetingId"
        ]
    },
    "PastMeetings.participants": {
        "type": "object",
        "properties": {
            "meetingId": {
                "type": "integer",
                "description": "The meeting ID."
            },
            "page_size": {
                "type": "integer",
                "description": "The number of records returned within a single API call.",
                "default": 0,
                "maximum": 300
            },
            "next_page_token": {
                "type": "string",
                  "description": "The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes."
            }
        },
        "required": [
            "meetingId"
        ]
    },
    "PastMeetings.instances": {
        "type": "object",
        "properties": {
            "meetingId": {
                "type": "integer",
                "description": "The meeting ID."
            }
        },
        "required": [
            "meetingId"
        ]
    }
}
