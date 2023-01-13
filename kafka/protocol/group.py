from __future__ import absolute_import

from kafka.protocol.api import Request, Response
from kafka.protocol.struct import Struct
from kafka.protocol.types import Array, Bytes, Int16, Int32, Schema, String


class JoinGroupResponse_v0(Response):
    API_KEY = 11
    API_VERSION = 0
    SCHEMA = Schema(
        ('error_code', Int16),
        ('generation_id', Int32),
        ('group_protocol', String('utf-8')),
        ('leader_id', String('utf-8')),
        ('member_id', String('utf-8')),
        ('members', Array(
            ('member_id', String('utf-8')),
            ('member_metadata', Bytes)))
    )


class JoinGroupResponse_v1(Response):
    API_KEY = 11
    API_VERSION = 1
    SCHEMA = JoinGroupResponse_v0.SCHEMA


class JoinGroupResponse_v2(Response):
    API_KEY = 11
    API_VERSION = 2
    SCHEMA = Schema(
        ('throttle_time_ms', Int32),
        ('error_code', Int16),
        ('generation_id', Int32),
        ('group_protocol', String('utf-8')),
        ('leader_id', String('utf-8')),
        ('member_id', String('utf-8')),
        ('members', Array(
            ('member_id', String('utf-8')),
            ('member_metadata', Bytes)))
    )

class JoinGroupResponse_v5(Response):
    API_KEY = 11
    API_VERSION = 5
    SCHEMA = Schema(
        ('throttle_time_ms', Int32),
        ('error_code', Int16),
        ('generation_id', Int32),
        ('group_protocol', String('utf-8')),
        ('leader_id', String('utf-8')),
        ('member_id', String('utf-8')),
        ('members', Array(
            ('member_id', String('utf-8')),
            ('group_instance_id', String('utf-8')),
            ('member_metadata', Bytes))),
    )

class JoinGroupRequest_v0(Request):
    API_KEY = 11
    API_VERSION = 0
    RESPONSE_TYPE = JoinGroupResponse_v0
    SCHEMA = Schema(
        ('group', String('utf-8')),
        ('session_timeout', Int32),
        ('member_id', String('utf-8')),
        ('protocol_type', String('utf-8')),
        ('group_protocols', Array(
            ('protocol_name', String('utf-8')),
            ('protocol_metadata', Bytes)))
    )
    UNKNOWN_MEMBER_ID = ''


class JoinGroupRequest_v1(Request):
    API_KEY = 11
    API_VERSION = 1
    RESPONSE_TYPE = JoinGroupResponse_v1
    SCHEMA = Schema(
        ('group', String('utf-8')),
        ('session_timeout', Int32),
        ('rebalance_timeout', Int32),
        ('member_id', String('utf-8')),
        ('protocol_type', String('utf-8')),
        ('group_protocols', Array(
            ('protocol_name', String('utf-8')),
            ('protocol_metadata', Bytes)))
    )
    UNKNOWN_MEMBER_ID = ''


class JoinGroupRequest_v2(Request):
    API_KEY = 11
    API_VERSION = 2
    RESPONSE_TYPE = JoinGroupResponse_v2
    SCHEMA = JoinGroupRequest_v1.SCHEMA
    UNKNOWN_MEMBER_ID = ''

class JoinGroupRequest_v5(Request):
    API_KEY = 11
    API_VERSION = 5
    RESPONSE_TYPE = JoinGroupResponse_v5
    SCHEMA = Schema(
        ('group', String('utf-8')),
        ('session_timeout', Int32),
        ('rebalance_timeout', Int32),
        ('member_id', String('utf-8')),
        ('group_instance_id', String('utf-8')),
        ('protocol_type', String('utf-8')),
        ('group_protocols', Array(
            ('protocol_name', String('utf-8')),
            ('protocol_metadata', Bytes))),
    )
    UNKNOWN_MEMBER_ID = ''



JoinGroupRequest = [
    JoinGroupRequest_v0, JoinGroupRequest_v1, JoinGroupRequest_v2, None, None, JoinGroupRequest_v5,
]
JoinGroupResponse = [
    JoinGroupResponse_v0, JoinGroupResponse_v1, JoinGroupResponse_v2, None, None, JoinGroupResponse_v5,
]


class ProtocolMetadata(Struct):
    SCHEMA = Schema(
        ('version', Int16),
        ('subscription', Array(String('utf-8'))), # topics list
        ('user_data', Bytes)
    )


class SyncGroupResponse_v0(Response):
    API_KEY = 14
    API_VERSION = 0
    SCHEMA = Schema(
        ('error_code', Int16),
        ('member_assignment', Bytes)
    )


class SyncGroupResponse_v1(Response):
    API_KEY = 14
    API_VERSION = 1
    SCHEMA = Schema(
        ('throttle_time_ms', Int32),
        ('error_code', Int16),
        ('member_assignment', Bytes)
    )

class SyncGroupResponse_v3(Response):
    API_KEY = 14
    API_VERSION = 3
    SCHEMA = Schema(
        ('throttle_time_ms', Int32),
        ('error_code', Int16),
        ('member_assignment', Bytes)
    )

class SyncGroupRequest_v0(Request):
    API_KEY = 14
    API_VERSION = 0
    RESPONSE_TYPE = SyncGroupResponse_v0
    SCHEMA = Schema(
        ('group', String('utf-8')),
        ('generation_id', Int32),
        ('member_id', String('utf-8')),
        ('group_assignment', Array(
            ('member_id', String('utf-8')),
            ('member_metadata', Bytes)))
    )


class SyncGroupRequest_v1(Request):
    API_KEY = 14
    API_VERSION = 1
    RESPONSE_TYPE = SyncGroupResponse_v1
    SCHEMA = SyncGroupRequest_v0.SCHEMA
class SyncGroupRequest_v3(Request):
    API_KEY = 14
    API_VERSION = 3
    RESPONSE_TYPE = SyncGroupResponse_v3
    SCHEMA = Schema(
        ('group', String('utf-8')),
        ('generation_id', Int32),
        ('member_id', String('utf-8')),
        ('group_instance_id', String('utf-8')),
        ('group_assignment', Array(
            ('member_id', String('utf-8')),
            ('member_metadata', Bytes))),
    )


SyncGroupRequest = [SyncGroupRequest_v0, SyncGroupRequest_v1, None, SyncGroupRequest_v3]
SyncGroupResponse = [SyncGroupResponse_v0, SyncGroupResponse_v1, None, SyncGroupResponse_v3]


class MemberAssignment(Struct):
    SCHEMA = Schema(
        ('version', Int16),
        ('assignment', Array(
            ('topic', String('utf-8')),
            ('partitions', Array(Int32)))),
        ('user_data', Bytes)
    )


class HeartbeatResponse_v0(Response):
    API_KEY = 12
    API_VERSION = 0
    SCHEMA = Schema(
        ('error_code', Int16)
    )


class HeartbeatResponse_v1(Response):
    API_KEY = 12
    API_VERSION = 1
    SCHEMA = Schema(
        ('throttle_time_ms', Int32),
        ('error_code', Int16)
    )


class HeartbeatRequest_v0(Request):
    API_KEY = 12
    API_VERSION = 0
    RESPONSE_TYPE = HeartbeatResponse_v0
    SCHEMA = Schema(
        ('group', String('utf-8')),
        ('generation_id', Int32),
        ('member_id', String('utf-8'))
    )


class HeartbeatResponse_v2(Response):
    API_KEY = 12
    API_VERSION = 2
    SCHEMA = Schema(
        ('throttle_time_ms', Int32),
        ('error_code', Int16)
    )


class HeartbeatRequest_v2(Request):
    API_KEY = 12
    API_VERSION = 2
    RESPONSE_TYPE = HeartbeatResponse_v2
    SCHEMA = Schema(
        ('group', String('utf-8')),
        ('generation_id', Int32),
        ('member_id', String('utf-8')),
        ('group_instance_id', String('utf-8')),
    )


HeartbeatRequest = [HeartbeatRequest_v0, HeartbeatRequest_v1, HeartbeatRequest_v2]
HeartbeatResponse = [HeartbeatResponse_v0, HeartbeatResponse_v1, HeartbeatResponse_v2]



class LeaveGroupResponse_v0(Response):
    API_KEY = 13
    API_VERSION = 0
    SCHEMA = Schema(
        ('error_code', Int16)
    )

    
class LeaveGroupResponse_v1(Response):
    API_KEY = 13
    API_VERSION = 1
    SCHEMA = Schema(
        ('throttle_time_ms', Int32),
        ('error_code', Int16)
    )


class LeaveGroupRequest_v0(Request):
    API_KEY = 13
    API_VERSION = 0
    RESPONSE_TYPE = LeaveGroupResponse_v0
    SCHEMA = Schema(
        ('group', String('utf-8')),
        ('member_id', String('utf-8'))
    )


class LeaveGroupRequest_v1(Request):
    API_KEY = 13
    API_VERSION = 1
    RESPONSE_TYPE = LeaveGroupResponse_v1
    SCHEMA = LeaveGroupRequest_v0.SCHEMA


LeaveGroupRequest = [LeaveGroupRequest_v0, LeaveGroupRequest_v1]
LeaveGroupResponse = [LeaveGroupResponse_v0, LeaveGroupResponse_v1]
