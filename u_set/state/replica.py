import threading
from u_set.state.proto import u_set_pb2


def crdt_add(payload, e):
  new_set = set(payload.set).union(set([e]))
  new_payload = counter_pb2.Payload(set=list([new_set]))
  payload.set.CopyFrom(new_payload.set)

def lub(a, b):
  new_set = set(a.set).union(b.set)
  new_payload = counter_pb2.Payload(set=list([new_set]))
  return new_payload

def value(payload):
  return set(payload.set)


class Replica(object):
  def __init__(self):
    self.payload = counter_pb2.Payload()
    # Lock is for when
    # 1. multiple replicas are merging concurrently
    # 2. local query / mutate concurrency
    self._payload_lock = threading.Lock()

  def mutate_add(self, e):
    with self._payload_lock:
      crdt_add(self.payload, e)

  def query_value(self):
    with self._payload_lock:
      return value(self.payload)

  def merge(self, other):
    with self._payload_lock:
      self.payload = lub(self.payload, other.payload)
