# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messaging.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fmessaging.proto\x1a\x1bgoogle/protobuf/empty.proto\"0\n\x0b\x43hatMessage\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2|\n\x0b\x43hatService\x12\x33\n\x0bSendMessage\x12\x0c.ChatMessage\x1a\x16.google.protobuf.Empty\x12\x38\n\x0eReceiveMessage\x12\x16.google.protobuf.Empty\x1a\x0c.ChatMessage0\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messaging_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHATMESSAGE._serialized_start=48
  _CHATMESSAGE._serialized_end=96
  _CHATSERVICE._serialized_start=98
  _CHATSERVICE._serialized_end=222
# @@protoc_insertion_point(module_scope)
