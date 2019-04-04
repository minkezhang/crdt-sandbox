import unittest

from counter.state import replica


class ReplicaTestCase(unittest.TestCase):
  def testConvergence(self):
    n_increments = [2, 1, 1]
    replicas = [replica.Replica(i, len(n_increments)) for i in range(len(n_increments))]

    for (replica_index, increments) in enumerate(n_increments):
      replicas[i].mutate_increment(increments)

    for r in replicas:
      replicas[0].merge(r)

    self.assertEqual(replicas[0].query_value(), 4)

  def testIdempotency(self):
    r_1 = replica.Replica(0, 2)
    r_2 = replica.Replica(1, 2)

    r_1.mutate_increment(2)
    r_2.mutate_increment(5)

    r_1.merge(r_2)
    self.assertEqual(r_1.query_value(), 7)

    r_1.merge(r_2)
    self.assertEqual(r_1.query_value(), 7)


if __name__ == '__main__':
  unittest.main()
