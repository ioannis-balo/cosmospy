# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_send.proto
"""Generated protocol buffer code."""
import cosmospy.interfaces.coin_pb2 as coin__pb2
import cosmospy.interfaces.gogo_pb2 as gogo__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="msg_send.proto",
    package="cosmos.bank.v1beta1",
    syntax="proto3",
    serialized_options=b"Z)github.com/cosmos/cosmos-sdk/x/bank/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0emsg_send.proto\x12\x13\x63osmos.bank.v1beta1\x1a\ngogo.proto\x1a\ncoin.proto"\xca\x01\n\x07MsgSend\x12-\n\x0c\x66rom_address\x18\x01 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"from_address"\x12)\n\nto_address\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"to_address"\x12[\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3',
    dependencies=[
        gogo__pb2.DESCRIPTOR,
        coin__pb2.DESCRIPTOR,
    ],
)


_MSGSEND = _descriptor.Descriptor(
    name="MsgSend",
    full_name="cosmos.bank.v1beta1.MsgSend",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="from_address",
            full_name="cosmos.bank.v1beta1.MsgSend.from_address",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\023yaml:"from_address"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="to_address",
            full_name="cosmos.bank.v1beta1.MsgSend.to_address",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\021yaml:"to_address"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="amount",
            full_name="cosmos.bank.v1beta1.MsgSend.amount",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\350\240\037\000\210\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=64,
    serialized_end=266,
)

_MSGSEND.fields_by_name["amount"].message_type = coin__pb2._COIN
DESCRIPTOR.message_types_by_name["MsgSend"] = _MSGSEND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgSend = _reflection.GeneratedProtocolMessageType(
    "MsgSend",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGSEND,
        "__module__": "msg_send_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.MsgSend)
    },
)
_sym_db.RegisterMessage(MsgSend)


DESCRIPTOR._options = None
_MSGSEND.fields_by_name["from_address"]._options = None
_MSGSEND.fields_by_name["to_address"]._options = None
_MSGSEND.fields_by_name["amount"]._options = None
_MSGSEND._options = None
# @@protoc_insertion_point(module_scope)
