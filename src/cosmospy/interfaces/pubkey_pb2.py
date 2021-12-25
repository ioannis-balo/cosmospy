# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pubkey.proto
"""Generated protocol buffer code."""
import cosmospy.interfaces.gogo_pb2 as gogo__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="pubkey.proto",
    package="cosmos.crypto.secp256k1",
    syntax="proto3",
    serialized_options=b"Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256k1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0cpubkey.proto\x12\x17\x63osmos.crypto.secp256k1\x1a\ngogo.proto"\x1b\n\x06PubKey\x12\x0b\n\x03key\x18\x01 \x01(\x0c:\x04\x98\xa0\x1f\x00\x42\x34Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256k1b\x06proto3',
    dependencies=[
        gogo__pb2.DESCRIPTOR,
    ],
)


_PUBKEY = _descriptor.Descriptor(
    name="PubKey",
    full_name="cosmos.crypto.secp256k1.PubKey",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="cosmos.crypto.secp256k1.PubKey.key",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\230\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=53,
    serialized_end=80,
)

DESCRIPTOR.message_types_by_name["PubKey"] = _PUBKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PubKey = _reflection.GeneratedProtocolMessageType(
    "PubKey",
    (_message.Message,),
    {
        "DESCRIPTOR": _PUBKEY,
        "__module__": "pubkey_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.crypto.secp256k1.PubKey)
    },
)
_sym_db.RegisterMessage(PubKey)


DESCRIPTOR._options = None
_PUBKEY._options = None
# @@protoc_insertion_point(module_scope)
