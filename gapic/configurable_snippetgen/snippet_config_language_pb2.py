# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: snippet_config_language.proto
# type: ignore
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1dsnippet_config_language.proto\x12/google.cloud.tools.snippetgen.configlanguage.v1\x1a google/protobuf/descriptor.proto\"\xcd\x02\n\rSnippetConfig\x12X\n\x08metadata\x18\x01 \x01(\x0b\x32\x46.google.cloud.tools.snippetgen.configlanguage.v1.SnippetConfigMetadata\x12\x41\n\x03rpc\x18\x02 \x01(\x0b\x32\x34.google.cloud.tools.snippetgen.configlanguage.v1.Rpc\x12T\n\tsignature\x18\x03 \x01(\x0b\x32\x41.google.cloud.tools.snippetgen.configlanguage.v1.SnippetSignature\x12I\n\x07snippet\x18\x04 \x01(\x0b\x32\x38.google.cloud.tools.snippetgen.configlanguage.v1.Snippet\"\xd3\x01\n\x15SnippetConfigMetadata\x12\x0f\n\x07skipped\x18\x01 \x01(\x08\x12\x63\n\x11skipped_languages\x18\x02 \x03(\x0e\x32H.google.cloud.tools.snippetgen.configlanguage.v1.GeneratorOutputLanguage\x12\x11\n\tconfig_id\x18\x03 \x01(\t\x12\x14\n\x0csnippet_name\x18\x04 \x01(\t\x12\x1b\n\x13snippet_description\x18\x05 \x01(\t\"Y\n\x03Rpc\x12\x15\n\rproto_package\x18\x01 \x01(\t\x12\x13\n\x0b\x61pi_version\x18\x02 \x03(\t\x12\x14\n\x0cservice_name\x18\x03 \x01(\t\x12\x10\n\x08rpc_name\x18\x04 \x01(\t\"\x99\x03\n\x10SnippetSignature\x12\x1b\n\x13snippet_method_name\x18\x01 \x01(\t\x12J\n\x0breturn_type\x18\x02 \x01(\x0b\x32\x35.google.cloud.tools.snippetgen.configlanguage.v1.Type\x12i\n\x0fsync_preference\x18\x03 \x01(\x0e\x32P.google.cloud.tools.snippetgen.configlanguage.v1.SnippetSignature.SyncPreference\x12Z\n\nparameters\x18\x04 \x03(\x0b\x32\x46.google.cloud.tools.snippetgen.configlanguage.v1.Statement.Declaration\"U\n\x0eSyncPreference\x12\x16\n\x12LANGUAGE_PREFERRED\x10\x00\x12\x10\n\x0cPREFER_ASYNC\x10\x01\x12\x0f\n\x0bPREFER_SYNC\x10\x02\x12\x08\n\x04\x42OTH\x10\x03\"\x91,\n\x07Snippet\x12t\n\x1dservice_client_initialization\x18\x01 \x01(\x0b\x32M.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientInitialization\x12U\n\x08standard\x18\x02 \x01(\x0b\x32\x41.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.StandardH\x00\x12W\n\tpaginated\x18\x03 \x01(\x0b\x32\x42.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.PaginatedH\x00\x12K\n\x03lro\x18\x04 \x01(\x0b\x32<.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.LroH\x00\x12\x64\n\x10\x63lient_streaming\x18\x05 \x01(\x0b\x32H.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientStreamingH\x00\x12\x64\n\x10server_streaming\x18\x06 \x01(\x0b\x32H.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ServerStreamingH\x00\x12`\n\x0e\x62idi_streaming\x18\x07 \x01(\x0b\x32\x46.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.BidiStreamingH\x00\x12T\n\x10\x66inal_statements\x18\x08 \x03(\x0b\x32:.google.cloud.tools.snippetgen.configlanguage.v1.Statement\x1a\xff\x03\n\x14\x43lientInitialization\x12]\n\x19pre_client_initialization\x18\x01 \x03(\x0b\x32:.google.cloud.tools.snippetgen.configlanguage.v1.Statement\x12~\n\x17\x63ustom_service_endpoint\x18\x02 \x01(\x0b\x32].google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientInitialization.ServiceEndpoint\x1a\x87\x02\n\x0fServiceEndpoint\x12\x83\x01\n\x06schema\x18\x01 \x01(\x0e\x32s.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientInitialization.ServiceEndpoint.ServiceEndpointSchema\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\"B\n\x15ServiceEndpointSchema\x12\x14\n\x10LANGUAGE_DEFAULT\x10\x00\x12\t\n\x05HTTPS\x10\x01\x12\x08\n\x04HTTP\x10\x02\x1a\xbf\x02\n\x08Standard\x12t\n\x16request_initialization\x18\x01 \x01(\x0b\x32T.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.SimpleRequestInitialization\x12Q\n\x04\x63\x61ll\x18\x02 \x01(\x0b\x32\x43.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientCall\x12j\n\x11response_handling\x18\x03 \x01(\x0b\x32O.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.SimpleResponseHandling\x1a\xce\x02\n\tPaginated\x12t\n\x16request_initialization\x18\x01 \x01(\x0b\x32T.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.SimpleRequestInitialization\x12[\n\x0epaginated_call\x18\x02 \x01(\x0b\x32\x43.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientCall\x12n\n\x12paginated_handling\x18\x03 \x01(\x0b\x32R.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.PaginatedResponseHandling\x1a\xb2\x02\n\x03Lro\x12t\n\x16request_initialization\x18\x01 \x01(\x0b\x32T.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.SimpleRequestInitialization\x12Q\n\x04\x63\x61ll\x18\x02 \x01(\x0b\x32\x43.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientCall\x12\x62\n\x0clro_handling\x18\x03 \x01(\x0b\x32L.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.LroResponseHandling\x1a\xf4\x02\n\x0f\x43lientStreaming\x12`\n\x13initialization_call\x18\x01 \x01(\x0b\x32\x43.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientCall\x12\x1a\n\x12\x63lient_stream_name\x18\x02 \x01(\t\x12w\n\x16request_initialization\x18\x03 \x01(\x0b\x32W.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.StreamingRequestInitialization\x12j\n\x11response_handling\x18\x04 \x01(\x0b\x32O.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.SimpleResponseHandling\x1a\xf4\x02\n\x0fServerStreaming\x12t\n\x16request_initialization\x18\x01 \x01(\x0b\x32T.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.SimpleRequestInitialization\x12`\n\x13initialization_call\x18\x02 \x01(\x0b\x32\x43.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientCall\x12\x1a\n\x12server_stream_name\x18\x03 \x01(\t\x12m\n\x11response_handling\x18\x04 \x01(\x0b\x32R.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.StreamingResponseHandling\x1a\x91\x03\n\rBidiStreaming\x12`\n\x13initialization_call\x18\x01 \x01(\x0b\x32\x43.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientCall\x12\x1a\n\x12\x63lient_stream_name\x18\x02 \x01(\t\x12w\n\x16request_initialization\x18\x03 \x01(\x0b\x32W.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.StreamingRequestInitialization\x12\x1a\n\x12server_stream_name\x18\x04 \x01(\t\x12m\n\x11response_handling\x18\x05 \x01(\x0b\x32R.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.StreamingResponseHandling\x1aZ\n\nClientCall\x12L\n\x08pre_call\x18\x02 \x03(\x0b\x32:.google.cloud.tools.snippetgen.configlanguage.v1.Statement\x1a\xe7\x01\n\x1bSimpleRequestInitialization\x12^\n\x1apre_request_initialization\x18\x01 \x03(\x0b\x32:.google.cloud.tools.snippetgen.configlanguage.v1.Statement\x12R\n\rrequest_value\x18\x02 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x12\x14\n\x0crequest_name\x18\x03 \x01(\t\x1a\xe1\x02\n\x1eStreamingRequestInitialization\x12u\n\x17\x66irst_streaming_request\x18\x01 \x01(\x0b\x32T.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.SimpleRequestInitialization\x12W\n\titeration\x18\x03 \x01(\x0b\x32\x44.google.cloud.tools.snippetgen.configlanguage.v1.Statement.Iteration\x12o\n\x11streaming_request\x18\x04 \x01(\x0b\x32T.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.SimpleRequestInitialization\x1a/\n\x16SimpleResponseHandling\x12\x15\n\rresponse_name\x18\x01 \x01(\t\x1a\xec\x07\n\x19PaginatedResponseHandling\x12\x15\n\rresponse_name\x18\x01 \x01(\t\x12l\n\x07\x62y_item\x18\x02 \x01(\x0b\x32Y.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.PaginatedResponseHandling.ByItemH\x00\x12l\n\x07\x62y_page\x18\x03 \x01(\x0b\x32Y.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.PaginatedResponseHandling.ByPageH\x00\x12{\n\x0fnext_page_token\x18\x04 \x01(\x0b\x32`.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.PaginatedResponseHandling.NextPageTokenH\x00\x1at\n\x06\x42yItem\x12\x11\n\titem_name\x18\x01 \x01(\t\x12W\n\x13per_item_statements\x18\x02 \x03(\x0b\x32:.google.cloud.tools.snippetgen.configlanguage.v1.Statement\x1a\xe0\x01\n\x06\x42yPage\x12\x11\n\tpage_name\x18\x01 \x01(\t\x12W\n\x13per_page_statements\x18\x02 \x03(\x0b\x32:.google.cloud.tools.snippetgen.configlanguage.v1.Statement\x12j\n\x07\x62y_item\x18\x03 \x01(\x0b\x32Y.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.PaginatedResponseHandling.ByItem\x1a\xf2\x01\n\rNextPageToken\x12\x1c\n\x14next_page_token_name\x18\x01 \x01(\t\x12W\n\x12\x65xplicit_page_size\x18\x02 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x12j\n\x07\x62y_page\x18\x03 \x01(\x0b\x32Y.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.PaginatedResponseHandling.ByPageB\x11\n\x0fpagination_kind\x1a\xcf\x02\n\x13LroResponseHandling\x12\x15\n\rresponse_name\x18\x01 \x01(\t\x12n\n\x0cpolling_type\x18\x02 \x01(\x0e\x32X.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.LroResponseHandling.PollingType\x12\x1d\n\x15polling_response_name\x18\x03 \x01(\t\x12Y\n\x0cpolling_call\x18\x04 \x01(\x0b\x32\x43.google.cloud.tools.snippetgen.configlanguage.v1.Snippet.ClientCall\"7\n\x0bPollingType\x12\x14\n\x10UNTIL_COMPLETION\x10\x00\x12\x08\n\x04ONCE\x10\x01\x12\x08\n\x04NONE\x10\x02\x1a\x9e\x01\n\x19StreamingResponseHandling\x12\x1d\n\x15\x63urrent_response_name\x18\x01 \x01(\t\x12\x62\n\x1eper_stream_response_statements\x18\x02 \x03(\x0b\x32:.google.cloud.tools.snippetgen.configlanguage.v1.StatementB\x06\n\x04\x63\x61ll\"\xc5\x18\n\tStatement\x12]\n\x0b\x64\x65\x63laration\x18\x01 \x01(\x0b\x32\x46.google.cloud.tools.snippetgen.configlanguage.v1.Statement.DeclarationH\x00\x12\x64\n\x0fstandard_output\x18\x02 \x01(\x0b\x32I.google.cloud.tools.snippetgen.configlanguage.v1.Statement.StandardOutputH\x00\x12S\n\x06return\x18\x03 \x01(\x0b\x32\x41.google.cloud.tools.snippetgen.configlanguage.v1.Statement.ReturnH\x00\x12]\n\x0b\x63onditional\x18\x04 \x01(\x0b\x32\x46.google.cloud.tools.snippetgen.configlanguage.v1.Statement.ConditionalH\x00\x12Y\n\titeration\x18\x05 \x01(\x0b\x32\x44.google.cloud.tools.snippetgen.configlanguage.v1.Statement.IterationH\x00\x1a\xc1\x01\n\x0b\x44\x65\x63laration\x12\x43\n\x04type\x18\x01 \x01(\x0b\x32\x35.google.cloud.tools.snippetgen.configlanguage.v1.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12J\n\x05value\x18\x03 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x1a\\\n\x0eStandardOutput\x12J\n\x05value\x18\x02 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x1aU\n\x06Return\x12K\n\x06result\x18\x01 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x1a\xf8\x01\n\x0b\x43onditional\x12N\n\tcondition\x18\x01 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x12K\n\x07on_true\x18\x02 \x03(\x0b\x32:.google.cloud.tools.snippetgen.configlanguage.v1.Statement\x12L\n\x08on_false\x18\x03 \x03(\x0b\x32:.google.cloud.tools.snippetgen.configlanguage.v1.Statement\x1a\xdd\x0f\n\tIteration\x12\x83\x01\n\x1anumeric_sequence_iteration\x18\x01 \x01(\x0b\x32].google.cloud.tools.snippetgen.configlanguage.v1.Statement.Iteration.NumericSequenceIterationH\x00\x12t\n\x12repeated_iteration\x18\x02 \x01(\x0b\x32V.google.cloud.tools.snippetgen.configlanguage.v1.Statement.Iteration.RepeatedIterationH\x00\x12j\n\rmap_iteration\x18\x03 \x01(\x0b\x32Q.google.cloud.tools.snippetgen.configlanguage.v1.Statement.Iteration.MapIterationH\x00\x12n\n\x0f\x62ytes_iteration\x18\x04 \x01(\x0b\x32S.google.cloud.tools.snippetgen.configlanguage.v1.Statement.Iteration.BytesIterationH\x00\x12N\n\nstatements\x18\x05 \x03(\x0b\x32:.google.cloud.tools.snippetgen.configlanguage.v1.Statement\x1a\xdc\x05\n\x18NumericSequenceIteration\x12X\n\x08start_at\x18\x01 \x01(\x0b\x32\x46.google.cloud.tools.snippetgen.configlanguage.v1.Statement.Declaration\x12P\n\tincrement\x18\x03 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionH\x00\x12Q\n\nmultiplier\x18\x04 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionH\x00\x12Y\n\x12less_than_or_equal\x18\x07 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionH\x01\x12P\n\tless_than\x18\x08 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionH\x01\x12\\\n\x15greater_than_or_equal\x18\t \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionH\x01\x12S\n\x0cgreater_than\x18\n \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionH\x01\x12R\n\x0btotal_steps\x18\x0b \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionH\x01\x42\x06\n\x04stepB\x05\n\x03\x65nd\x1a\x8c\x01\n\x11RepeatedIteration\x12\x61\n\x11repeated_elements\x18\x01 \x01(\x0b\x32\x46.google.cloud.tools.snippetgen.configlanguage.v1.Statement.Declaration\x12\x14\n\x0c\x63urrent_name\x18\x02 \x01(\t\x1a\x99\x01\n\x0cMapIteration\x12S\n\x03map\x18\x01 \x01(\x0b\x32\x46.google.cloud.tools.snippetgen.configlanguage.v1.Statement.Declaration\x12\x18\n\x10\x63urrent_key_name\x18\x02 \x01(\t\x12\x1a\n\x12\x63urrent_value_name\x18\x03 \x01(\t\x1a\x8b\x03\n\x0e\x42ytesIteration\x12]\n\rbyte_sequence\x18\x01 \x01(\x0b\x32\x46.google.cloud.tools.snippetgen.configlanguage.v1.Statement.Declaration\x12Q\n\nchunk_size\x18\x02 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionH\x00\x12S\n\x0ctotal_chunks\x18\x03 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionH\x00\x12S\n\nchunk_type\x18\x04 \x01(\x0b\x32?.google.cloud.tools.snippetgen.configlanguage.v1.Type.BytesType\x12\x14\n\x0c\x63urrent_name\x18\x05 \x01(\tB\x07\n\x05\x63hunkB\x10\n\x0eiteration_typeB\x10\n\x0estatement_type\"\xb6\r\n\x04Type\x12W\n\x0bscalar_type\x18\x01 \x01(\x0e\x32@.google.cloud.tools.snippetgen.configlanguage.v1.Type.ScalarTypeH\x00\x12S\n\tenum_type\x18\x02 \x01(\x0b\x32>.google.cloud.tools.snippetgen.configlanguage.v1.Type.EnumTypeH\x00\x12U\n\nbytes_type\x18\x03 \x01(\x0b\x32?.google.cloud.tools.snippetgen.configlanguage.v1.Type.BytesTypeH\x00\x12Y\n\x0cmessage_type\x18\x04 \x01(\x0b\x32\x41.google.cloud.tools.snippetgen.configlanguage.v1.Type.MessageTypeH\x00\x12[\n\rrepeated_type\x18\x05 \x01(\x0b\x32\x42.google.cloud.tools.snippetgen.configlanguage.v1.Type.RepeatedTypeH\x00\x12Q\n\x08map_type\x18\x06 \x01(\x0b\x32=.google.cloud.tools.snippetgen.configlanguage.v1.Type.MapTypeH\x00\x1a\"\n\x08\x45numType\x12\x16\n\x0e\x65num_full_name\x18\x01 \x01(\t\x1a\xce\x01\n\tBytesType\x12o\n\x13language_equivalent\x18\x01 \x01(\x0e\x32R.google.cloud.tools.snippetgen.configlanguage.v1.Type.BytesType.LanguageEquivalent\"P\n\x12LanguageEquivalent\x12\x12\n\x0ePROTOBUF_BYTES\x10\x00\x12\n\n\x06\x42\x41SE64\x10\x01\x12\x0e\n\nBYTE_ARRAY\x10\x02\x12\n\n\x06STREAM\x10\x03\x1a(\n\x0bMessageType\x12\x19\n\x11message_full_name\x18\x01 \x01(\t\x1a\x91\x02\n\x0cRepeatedType\x12K\n\x0c\x65lement_type\x18\x01 \x01(\x0b\x32\x35.google.cloud.tools.snippetgen.configlanguage.v1.Type\x12r\n\x13language_equivalent\x18\x02 \x01(\x0e\x32U.google.cloud.tools.snippetgen.configlanguage.v1.Type.RepeatedType.LanguageEquivalent\"@\n\x12LanguageEquivalent\x12\x15\n\x11PROTOBUF_REPEATED\x10\x00\x12\t\n\x05\x41RRAY\x10\x01\x12\x08\n\x04LIST\x10\x02\x1a\xc4\x02\n\x07MapType\x12G\n\x08key_type\x18\x01 \x01(\x0b\x32\x35.google.cloud.tools.snippetgen.configlanguage.v1.Type\x12I\n\nvalue_type\x18\x02 \x01(\x0b\x32\x35.google.cloud.tools.snippetgen.configlanguage.v1.Type\x12m\n\x13language_equivalent\x18\x03 \x01(\x0e\x32P.google.cloud.tools.snippetgen.configlanguage.v1.Type.MapType.LanguageEquivalent\"6\n\x12LanguageEquivalent\x12\x10\n\x0cPROTOBUF_MAP\x10\x00\x12\x0e\n\nDICTIONARY\x10\x01\"\x96\x02\n\nScalarType\x12\x19\n\x15SCALAR_TYPE_UNDEFINED\x10\x00\x12\x0f\n\x0bTYPE_DOUBLE\x10\x01\x12\x0e\n\nTYPE_FLOAT\x10\x02\x12\x0e\n\nTYPE_INT64\x10\x03\x12\x0f\n\x0bTYPE_UINT64\x10\x04\x12\x0e\n\nTYPE_INT32\x10\x05\x12\x10\n\x0cTYPE_FIXED64\x10\x06\x12\x10\n\x0cTYPE_FIXED32\x10\x07\x12\r\n\tTYPE_BOOL\x10\x08\x12\x0f\n\x0bTYPE_STRING\x10\t\x12\x0f\n\x0bTYPE_UINT32\x10\r\x12\x11\n\rTYPE_SFIXED32\x10\x0f\x12\x11\n\rTYPE_SFIXED64\x10\x10\x12\x0f\n\x0bTYPE_SINT32\x10\x11\x12\x0f\n\x0bTYPE_SINT64\x10\x12\x42\x0b\n\ttype_kind\"\xa8\x10\n\nExpression\x12[\n\nnull_value\x18\x01 \x01(\x0e\x32\x45.google.cloud.tools.snippetgen.configlanguage.v1.Expression.NullValueH\x00\x12\x61\n\rdefault_value\x18\x02 \x01(\x0e\x32H.google.cloud.tools.snippetgen.configlanguage.v1.Expression.DefaultValueH\x00\x12[\n\nname_value\x18\x03 \x01(\x0b\x32\x45.google.cloud.tools.snippetgen.configlanguage.v1.Expression.NameValueH\x00\x12\x16\n\x0cnumber_value\x18\x04 \x01(\x01H\x00\x12\x17\n\rboolean_value\x18\x05 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x00\x12\x14\n\nenum_value\x18\x07 \x01(\tH\x00\x12]\n\x0b\x62ytes_value\x18\x08 \x01(\x0b\x32\x46.google.cloud.tools.snippetgen.configlanguage.v1.Expression.BytesValueH\x00\x12\x61\n\rcomplex_value\x18\t \x01(\x0b\x32H.google.cloud.tools.snippetgen.configlanguage.v1.Expression.ComplexValueH\x00\x12_\n\nlist_value\x18\n \x01(\x0b\x32I.google.cloud.tools.snippetgen.configlanguage.v1.Expression.RepeatedValueH\x00\x12Y\n\tmap_value\x18\x0b \x01(\x0b\x32\x44.google.cloud.tools.snippetgen.configlanguage.v1.Expression.MapValueH\x00\x12l\n\x11\x63onditional_value\x18\x0c \x01(\x0b\x32O.google.cloud.tools.snippetgen.configlanguage.v1.Expression.ConditionalOperatorH\x00\x12\x13\n\x0b\x64\x65scription\x18\r \x01(\t\x1a\'\n\tNameValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x03(\t\x1a\xb3\x02\n\nBytesValue\x12T\n\rbase64_string\x18\x01 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionH\x00\x12h\n\x0b\x66ile_stream\x18\x02 \x01(\x0b\x32Q.google.cloud.tools.snippetgen.configlanguage.v1.Expression.BytesValue.FileStreamH\x00\x1a\\\n\nFileStream\x12N\n\tfile_path\x18\x01 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.ExpressionB\x07\n\x05value\x1a\xec\x01\n\x0c\x43omplexValue\x12l\n\nproperties\x18\x01 \x03(\x0b\x32X.google.cloud.tools.snippetgen.configlanguage.v1.Expression.ComplexValue.PropertiesEntry\x1an\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12J\n\x05value\x18\x02 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression:\x02\x38\x01\x1a\\\n\rRepeatedValue\x12K\n\x06values\x18\x01 \x03(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x1a\xa2\x01\n\x08MapValue\x12I\n\x04keys\x18\x01 \x03(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x12K\n\x06values\x18\x02 \x03(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x1a\x82\x02\n\x13\x43onditionalOperator\x12N\n\tcondition\x18\x01 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x12L\n\x07on_true\x18\x02 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\x12M\n\x08on_false\x18\x03 \x01(\x0b\x32;.google.cloud.tools.snippetgen.configlanguage.v1.Expression\"\x1b\n\tNullValue\x12\x0e\n\nNULL_VALUE\x10\x00\"!\n\x0c\x44\x65\x66\x61ultValue\x12\x11\n\rDEFAULT_VALUE\x10\x00\x42\x07\n\x05value*\xa3\x01\n\x17GeneratorOutputLanguage\x12)\n%GENERATOR_OUTPUT_LANGUAGE_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x43_PLUS_PLUS\x10\x01\x12\x0b\n\x07\x43_SHARP\x10\x02\x12\x06\n\x02GO\x10\x03\x12\x08\n\x04JAVA\x10\x04\x12\x0e\n\nJAVASCRIPT\x10\x05\x12\x07\n\x03PHP\x10\x06\x12\n\n\x06PYTHON\x10\x07\x12\x08\n\x04RUBY\x10\x08\x42\xee\x01\n3com.google.cloud.tools.snippetgen.configlanguage.v1B\x1aSnippetConfigLanguageProtoP\x01\xaa\x02/Google.Cloud.Tools.SnippetGen.ConfigLanguage.V1\xca\x02/Google\\Cloud\\Tools\\SnippetGen\\ConfigLanguage\\V1\xea\x02\x34Google::Cloud::Tools::SnippetGen::ConfigLanguage::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'snippet_config_language_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS is False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n3com.google.cloud.tools.snippetgen.configlanguage.v1B\032SnippetConfigLanguageProtoP\001\252\002/Google.Cloud.Tools.SnippetGen.ConfigLanguage.V1\312\002/Google\\Cloud\\Tools\\SnippetGen\\ConfigLanguage\\V1\352\0024Google::Cloud::Tools::SnippetGen::ConfigLanguage::V1'
    _EXPRESSION_COMPLEXVALUE_PROPERTIESENTRY._options = None
    _EXPRESSION_COMPLEXVALUE_PROPERTIESENTRY._serialized_options = b'8\001'
    _GENERATOROUTPUTLANGUAGE._serialized_start = 13778
    _GENERATOROUTPUTLANGUAGE._serialized_end = 13941
    _SNIPPETCONFIG._serialized_start = 117
    _SNIPPETCONFIG._serialized_end = 450
    _SNIPPETCONFIGMETADATA._serialized_start = 453
    _SNIPPETCONFIGMETADATA._serialized_end = 664
    _RPC._serialized_start = 666
    _RPC._serialized_end = 755
    _SNIPPETSIGNATURE._serialized_start = 758
    _SNIPPETSIGNATURE._serialized_end = 1167
    _SNIPPETSIGNATURE_SYNCPREFERENCE._serialized_start = 1082
    _SNIPPETSIGNATURE_SYNCPREFERENCE._serialized_end = 1167
    _SNIPPET._serialized_start = 1170
    _SNIPPET._serialized_end = 6819
    _SNIPPET_CLIENTINITIALIZATION._serialized_start = 1941
    _SNIPPET_CLIENTINITIALIZATION._serialized_end = 2452
    _SNIPPET_CLIENTINITIALIZATION_SERVICEENDPOINT._serialized_start = 2189
    _SNIPPET_CLIENTINITIALIZATION_SERVICEENDPOINT._serialized_end = 2452
    _SNIPPET_CLIENTINITIALIZATION_SERVICEENDPOINT_SERVICEENDPOINTSCHEMA._serialized_start = 2386
    _SNIPPET_CLIENTINITIALIZATION_SERVICEENDPOINT_SERVICEENDPOINTSCHEMA._serialized_end = 2452
    _SNIPPET_STANDARD._serialized_start = 2455
    _SNIPPET_STANDARD._serialized_end = 2774
    _SNIPPET_PAGINATED._serialized_start = 2777
    _SNIPPET_PAGINATED._serialized_end = 3111
    _SNIPPET_LRO._serialized_start = 3114
    _SNIPPET_LRO._serialized_end = 3420
    _SNIPPET_CLIENTSTREAMING._serialized_start = 3423
    _SNIPPET_CLIENTSTREAMING._serialized_end = 3795
    _SNIPPET_SERVERSTREAMING._serialized_start = 3798
    _SNIPPET_SERVERSTREAMING._serialized_end = 4170
    _SNIPPET_BIDISTREAMING._serialized_start = 4173
    _SNIPPET_BIDISTREAMING._serialized_end = 4574
    _SNIPPET_CLIENTCALL._serialized_start = 4576
    _SNIPPET_CLIENTCALL._serialized_end = 4666
    _SNIPPET_SIMPLEREQUESTINITIALIZATION._serialized_start = 4669
    _SNIPPET_SIMPLEREQUESTINITIALIZATION._serialized_end = 4900
    _SNIPPET_STREAMINGREQUESTINITIALIZATION._serialized_start = 4903
    _SNIPPET_STREAMINGREQUESTINITIALIZATION._serialized_end = 5256
    _SNIPPET_SIMPLERESPONSEHANDLING._serialized_start = 5258
    _SNIPPET_SIMPLERESPONSEHANDLING._serialized_end = 5305
    _SNIPPET_PAGINATEDRESPONSEHANDLING._serialized_start = 5308
    _SNIPPET_PAGINATEDRESPONSEHANDLING._serialized_end = 6312
    _SNIPPET_PAGINATEDRESPONSEHANDLING_BYITEM._serialized_start = 5705
    _SNIPPET_PAGINATEDRESPONSEHANDLING_BYITEM._serialized_end = 5821
    _SNIPPET_PAGINATEDRESPONSEHANDLING_BYPAGE._serialized_start = 5824
    _SNIPPET_PAGINATEDRESPONSEHANDLING_BYPAGE._serialized_end = 6048
    _SNIPPET_PAGINATEDRESPONSEHANDLING_NEXTPAGETOKEN._serialized_start = 6051
    _SNIPPET_PAGINATEDRESPONSEHANDLING_NEXTPAGETOKEN._serialized_end = 6293
    _SNIPPET_LRORESPONSEHANDLING._serialized_start = 6315
    _SNIPPET_LRORESPONSEHANDLING._serialized_end = 6650
    _SNIPPET_LRORESPONSEHANDLING_POLLINGTYPE._serialized_start = 6595
    _SNIPPET_LRORESPONSEHANDLING_POLLINGTYPE._serialized_end = 6650
    _SNIPPET_STREAMINGRESPONSEHANDLING._serialized_start = 6653
    _SNIPPET_STREAMINGRESPONSEHANDLING._serialized_end = 6811
    _STATEMENT._serialized_start = 6822
    _STATEMENT._serialized_end = 9963
    _STATEMENT_DECLARATION._serialized_start = 7304
    _STATEMENT_DECLARATION._serialized_end = 7497
    _STATEMENT_STANDARDOUTPUT._serialized_start = 7499
    _STATEMENT_STANDARDOUTPUT._serialized_end = 7591
    _STATEMENT_RETURN._serialized_start = 7593
    _STATEMENT_RETURN._serialized_end = 7678
    _STATEMENT_CONDITIONAL._serialized_start = 7681
    _STATEMENT_CONDITIONAL._serialized_end = 7929
    _STATEMENT_ITERATION._serialized_start = 7932
    _STATEMENT_ITERATION._serialized_end = 9945
    _STATEMENT_ITERATION_NUMERICSEQUENCEITERATION._serialized_start = 8498
    _STATEMENT_ITERATION_NUMERICSEQUENCEITERATION._serialized_end = 9230
    _STATEMENT_ITERATION_REPEATEDITERATION._serialized_start = 9233
    _STATEMENT_ITERATION_REPEATEDITERATION._serialized_end = 9373
    _STATEMENT_ITERATION_MAPITERATION._serialized_start = 9376
    _STATEMENT_ITERATION_MAPITERATION._serialized_end = 9529
    _STATEMENT_ITERATION_BYTESITERATION._serialized_start = 9532
    _STATEMENT_ITERATION_BYTESITERATION._serialized_end = 9927
    _TYPE._serialized_start = 9966
    _TYPE._serialized_end = 11684
    _TYPE_ENUMTYPE._serialized_start = 10502
    _TYPE_ENUMTYPE._serialized_end = 10536
    _TYPE_BYTESTYPE._serialized_start = 10539
    _TYPE_BYTESTYPE._serialized_end = 10745
    _TYPE_BYTESTYPE_LANGUAGEEQUIVALENT._serialized_start = 10665
    _TYPE_BYTESTYPE_LANGUAGEEQUIVALENT._serialized_end = 10745
    _TYPE_MESSAGETYPE._serialized_start = 10747
    _TYPE_MESSAGETYPE._serialized_end = 10787
    _TYPE_REPEATEDTYPE._serialized_start = 10790
    _TYPE_REPEATEDTYPE._serialized_end = 11063
    _TYPE_REPEATEDTYPE_LANGUAGEEQUIVALENT._serialized_start = 10999
    _TYPE_REPEATEDTYPE_LANGUAGEEQUIVALENT._serialized_end = 11063
    _TYPE_MAPTYPE._serialized_start = 11066
    _TYPE_MAPTYPE._serialized_end = 11390
    _TYPE_MAPTYPE_LANGUAGEEQUIVALENT._serialized_start = 11336
    _TYPE_MAPTYPE_LANGUAGEEQUIVALENT._serialized_end = 11390
    _TYPE_SCALARTYPE._serialized_start = 11393
    _TYPE_SCALARTYPE._serialized_end = 11671
    _EXPRESSION._serialized_start = 11687
    _EXPRESSION._serialized_end = 13775
    _EXPRESSION_NAMEVALUE._serialized_start = 12594
    _EXPRESSION_NAMEVALUE._serialized_end = 12633
    _EXPRESSION_BYTESVALUE._serialized_start = 12636
    _EXPRESSION_BYTESVALUE._serialized_end = 12943
    _EXPRESSION_BYTESVALUE_FILESTREAM._serialized_start = 12842
    _EXPRESSION_BYTESVALUE_FILESTREAM._serialized_end = 12934
    _EXPRESSION_COMPLEXVALUE._serialized_start = 12946
    _EXPRESSION_COMPLEXVALUE._serialized_end = 13182
    _EXPRESSION_COMPLEXVALUE_PROPERTIESENTRY._serialized_start = 13072
    _EXPRESSION_COMPLEXVALUE_PROPERTIESENTRY._serialized_end = 13182
    _EXPRESSION_REPEATEDVALUE._serialized_start = 13184
    _EXPRESSION_REPEATEDVALUE._serialized_end = 13276
    _EXPRESSION_MAPVALUE._serialized_start = 13279
    _EXPRESSION_MAPVALUE._serialized_end = 13441
    _EXPRESSION_CONDITIONALOPERATOR._serialized_start = 13444
    _EXPRESSION_CONDITIONALOPERATOR._serialized_end = 13702
    _EXPRESSION_NULLVALUE._serialized_start = 13704
    _EXPRESSION_NULLVALUE._serialized_end = 13731
    _EXPRESSION_DEFAULTVALUE._serialized_start = 13733
    _EXPRESSION_DEFAULTVALUE._serialized_end = 13766
# @@protoc_insertion_point(module_scope)
