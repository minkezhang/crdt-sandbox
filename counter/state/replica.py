import threading
from counter.state.proto import counter_pb2


def increment(payload, i, n):
  payload.increments[i] += n

def lub(a, b):
  return counter_pb2.Payload(
    increments=[
        max(
            a.increments[i],
            b.increments[i]) for i in range(len(a.increments))]
  )

def value(payload):
  return sum(payload.increments)


class Replica(object):
  def __init__(self, id, n):
    self.id = id
    self.payload = counter_pb2.Payload(increments=[0] * n)
    self._payload_lock = threading.Lock()

  def mutate_increment(self, n):
    with self._payload_lock:
      increment(self.payload, self.id, n)

  def query_value(self):
    with self._payload_lock:
      return value(self.payload)

  def merge(self, other):
    with self._payload_lock:
      self.payload = lub(self.payload, other.payload)
