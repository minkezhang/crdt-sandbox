load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "9bc2cd89f4d342c6dae2ee6fae4861ebbae69f85",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_import", "pip_repositories")
pip_repositories()
pip_import(
   name = "virtualenv",
   requirements = "//:requirements.txt",
)

load("@virtualenv//:requirements.bzl", "pip_install")
pip_install()
