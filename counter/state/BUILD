load(
  "@io_bazel_rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test",
)

load("@virtualenv//:requirements.bzl", "requirement")

py_binary(
  name = "counter",
  srcs = ["counter.py"],
  deps = [
    "//counter/state:counter_pb",
  ],
)

py_library(
  name = "counter_pb",
  srcs = ["counter_pb2.py"],
  deps = [
    requirement("protobuf"),
    requirement("six"),
  ],
)

py_binary(
  name = "test",
  srcs = ["test.py"],
)
