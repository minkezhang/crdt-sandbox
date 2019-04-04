import unittest

from counter.state import replica


class ReplicaTestCase(unittest.TestCase):
  def testConvergence(self):
    replica_1 = replica.Replica(0)
    replica_2 = replica.Replica(1)
    replica_3 = replica.Replica(2)

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

    self.assertEqual(replica_1.value(), replica_2.value())
    self.assertEqual(replica_2.value(), replica_3.value())
    self.assertEqual(replica_3.value(), 4)


if __name__ == '__main__':
  unittest.main()
