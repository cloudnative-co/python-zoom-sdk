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
    "Users.get": {
        "type": "object",
        "required": [
            "userId"
        ],
        "properties": {
            "userId": {
                "type": "string",
                "description": "The user ID or email address of the user."
            },
            "login_type": {
                "type": "string",
                "enum": [
                    "0",
                    "1",
                    "99",
                    "100",
                    "101"
                ],
                "description": "`0` - Facebook.<br>`1` - Google.<br>`99` - API.<br>`100` - Zoom.<br>`101` - SSO.",
            }
        }
    },
    "Users.update": {
        "type": "object",
        "description": "The user update object represents a user on Zoom.",
        "required": [
            "userId"
        ],
        "properties": {
            "userId": {
                "type": "string",
                "description": "The user ID or email address of the user."
            },
            "login_type": {
                "type": "string",
                "enum": [
                    "0",
                    "1",
                    "99",
                    "100",
                    "101"
                ],
                "description": "`0` - Facebook.<br>`1` - Google.<br>`99` - API.<br>`100` - Zoom.<br>`101` - SSO."
            },
            "first_name": {
                "type": "string",
                "description": "User's first name. Cannot contain more than 5 Chinese characters.",
                "maxLength": 64
            },
            "last_name": {
                "type": "string",
                "description": "User's last name. Cannot contain more than 5 Chinese characters.",
                "maxLength": 64
            },
            "type": {
                "type": "integer",
                "enum": [
                    1,
                    2,
                    3
                ],
                "x-enum-descriptions": [
                    "Basic",
                    "Licensed",
                    "On-prem"
                ],
                "description": "User types:<br>`1` - Basic.<br>`2` - Licensed.<br>`3` - On-prem."
            },
            "pmi": {
                "type": "integer",
                "description": "Personal meeting ID: length must be 10.",
                "minLength": 10,
                "maxLength": 10
            },
            "use_pmi": {
                "type": "boolean",
                "description": "Use Personal Meeting ID for instant meetings.",
                "default": False
            },
            "timezone": {
                "type": "string",
                "description": "The time zone ID for a user profile. For this parameter value please refer to the ID value in the [timezone](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#timezones) list."
            },
            "language": {
                "type": "string",
                "description": "language"
            },
            "dept": {
                "type": "string",
                "description": "Department for user profile: use for report."
            },
            "vanity_name": {
                "type": "string",
                "description": "Personal meeting room name."
            },
            "host_key": {
                "type": "string",
                "description": "Host key. It should be a 6-10 digit number.",
                "minLength": 6,
                "maxLength": 10
            },
            "cms_user_id": {
                "type": "string",
                "description": "Kaltura user ID."
            },
            "job_title": {
                "type": "string",
                "description": "User's job title.",
                "maxLength": 128
            },
            "company": {
                "type": "string",
                "description": "User's company.",
                "maxLength": 255
            },
            "location": {
                "type": "string",
                "description": "User's location.",
                "maxLength": 256
            },
            "phone_number": {
                "type": "string",
                "description": "Phone number of the user. To update a phone number, you must also provide the `phone_country` field."
            },
            "phone_country": {
                "type": "string",
                "description": "[Country ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries) of the phone number. For example, if the phone number provided in the `phone_number` field is a Brazil based number, the value of the `phone_country` field should be `BR`."
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
