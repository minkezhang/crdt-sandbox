import threading
import counter_pb2

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


if __name__ == '__main__':
  replica_1 = Replica(0)
  replica_2 = Replica(1)
  replica_3 = Replica(2)

  replica_1.increment()
  replica_1.increment()

  replica_2.increment()
  replica_3.increment()

  replica_1.merge(replica_2.payload)
  replica_1.merge(replica_3.payload)

  replica_2.merge(replica_1.payload)
  replica_2.merge(replica_3.payload)

  replica_3.merge(replica_1.payload)
  replica_3.merge(replica_2.payload)

  assert replica_1.value() == replica_2.value() == replica_3.value() == 4
