syntax = "proto3";

package crdt.counter.state;

message Payload {
  repeated int32 counter = 1;
}
