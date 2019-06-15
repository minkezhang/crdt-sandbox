load(
    "@io_bazel_rules_python//python:python.bzl",
    "py_binary",
    "py_library",
    "py_test",
)   

py_library(
    name = "replica",
    srcs = ["replica.py"],
    deps = [
        "//counter/op/proto:op_g_counter_proto_py",
    ],
)
