import struct
import uuid
import json
from attrs import define, field, asdict
from typing import Dict


VERSION = 2
RESERVED = 0
OP_CONTROL = 2
OP_DATA = 1


@define(slots=True, kw_only=True)
class JRPC:

    jrpc: str = field(default='2.0')
    id: str = field(factory=lambda: str(uuid.uuid4()).split('-')[-1])
    params: dict = field(factory=dict)
    result: dict = field(factory=dict)
    error: dict = field(factory=dict)

    def to_frame(self):
        return _jrpc_to_frame(self)

    def to_frame_bytes(self):
        return _jrpc_to_bytes(self)


@define(slots=True, kw_only=True)
class Hello(JRPC):

    method: str = field(default='agent-hello')


@define(slots=True, kw_only=True)
class EchoRequest(JRPC):

    method: str = field(default='echo-request')


@define(slots=True, kw_only=True)
class JRPCResponse(JRPC):

    method: str = field(default=None)
    error: Dict = field(default=None)

    @classmethod
    def of(cls, id, method: str = None, error: Dict = None):
        r = cls()
        r.id = id
        r.method = method
        r.error = error
        return r


@define(slots=True, kw_only=True)
class SessionTrafficControl(JRPC):

    method: str = field(default='session-suspend')

    @classmethod
    def suspend(cls, session_id):
        r = cls()
        r.params['session-id'] = session_id
        return r

    @classmethod
    def resume(cls, session_id):
        r = cls()
        r.method = 'session-resume'
        r.params['session-id'] = session_id
        return r


@define(slots=True, kw_only=True)
class TerminationRequest(JRPC):

    method: str = field(default='termination-request')

    @classmethod
    def of(cls, session_id):
        r = cls()
        r.params['session-id'] = session_id
        return r


@define(slots=True, kw_only=True)
class SessionRequest(JRPC):

    method: str = field(default='session-request')

    @classmethod
    def of(cls, ip, port):
        r = cls()
        r.params['ip'] = ip
        r.params['port'] = port
        r.params['protocol'] = 'TCP'
        return r

    @classmethod
    def socks5(cls):
        r = cls()
        r.params['socks5'] = True
        return r


@define(slots=True, kw_only=True)
class Frame:

    version: int = field(default=VERSION)
    op_type: int = field(default=OP_CONTROL)
    session_id: int = field(default=0)
    payload: bytes = field(default=None)

    def to_bytes(self):
        return frame_to_bytes(self)


def bytes_to_frame(data: bytes) -> Frame:
    format = '>BBHH'
    size = struct.calcsize(format)
    version_op_type, _, session_id, payload_length = struct.unpack(format, data[:6])
    payload = data[size:size + payload_length]

    version = version_op_type >> 4
    op_type = version_op_type & 0x0F
    return Frame(
        version=version,
        op_type=op_type,
        session_id=session_id,
        payload=payload
    )


def frame_to_bytes(frame: Frame) -> bytes:
    payload_length = len(frame.payload)
    frame_format = '>BBHH{}s'.format(payload_length)

    frame_data = struct.pack(
        frame_format,
        frame.version << 4 | frame.op_type,  # B
        0,                          # B
        frame.session_id,           # H
        payload_length,             # H
        frame.payload
    )
    return frame_data


def _jrpc_to_frame(jrpc_obj: JRPC) -> Frame:
    payload = json.dumps(asdict(jrpc_obj)).encode('utf-8')
    frame = Frame(
        payload=payload
    )
    return frame


def _jrpc_to_bytes(jrpc_obj: JRPC) -> bytes:
    return frame_to_bytes(_jrpc_to_frame(jrpc_obj))


def hello(jrpc_obj=None) -> bytes:
    if jrpc_obj is None:
        jrpc_obj = Hello()
    else:
        assert jrpc_obj.method == 'agent-hello'

    return jrpc_obj.to_frame_bytes()
