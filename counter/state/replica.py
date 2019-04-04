import threading
from counter.state.proto import counter_pb2


class _Payload(object):
  def __init__(self, n=0, repr=None):
    if repr is None:
      self._repr = [0] * n
    else:
      self._repr = list(repr)

  def increment(self, i, n):
    self._repr[i] += n

  def lub(self, other):
    return _Payload(
        repr=[
            max(self._repr[i], other._repr[i]) for i in range(len(self._repr))])

  def value(self):
    return sum(self._repr)


class Replica(object):
  def __init__(self, id, n):
    self.id = id
    self.payload = _Payload(n)
    self._payload_lock = threading.Lock()

  def mutate_increment(self, n):
    with self._payload_lock:
      self.payload.increment(self.id, n)

  def query_value(self):
    with self._payload_lock:
      return self.payload.value()

  def merge(self, other):
    with self._payload_lock:
      self.payload = self.payload.lub(other.payload)
