import threading
from counter.state.proto import counter_pb2

class Replica(object):
  def __init__(self, id):
    self.id = id
    self.payload = [0, 0, 0]
    self._payload_lock = threading.Lock()

  def increment(self):
    with self._payload_lock:
      self.payload[self.id] += 1

  def value(self):
    with self._payload_lock:
      return sum(self.payload)

  def merge(self, other_payload):
    with self._payload_lock:
      self.payload = [
        max(self.payload[i], other_payload[i]) for i in range(len(self.payload))]
