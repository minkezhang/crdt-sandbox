load(
  "@io_bazel_rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test",
)

load("@virtualenv//:requirements.bzl", "requirement")

py_library(
  name = "replica",
  srcs = ["replica.py"],
  deps = [
    "//counter/state/proto:counter_proto_py",
  ],
)

py_test(
  name = "replica_test",
  srcs = ["replica_test.py"],
  deps = [
    ":replica",
  ],
)

py_binary(
  name = "test",
  srcs = ["test.py"],
)
