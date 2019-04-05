load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# proto_library
git_repository(
    name = "com_google_protobuf",
    commit = "b829ff2a4614ff25048944b2cdc8e43b6488fda0",  # v3.6.1.2
    remote = "https://github.com/protocolbuffers/protobuf.git",
)

git_repository(
    name = "io_bazel_rules_python",
    branch = "master",  # HEAD
    remote = "https://github.com/bazelbuild/rules_python.git",
)

git_repository(
    name = "io_bazel_rules_go",
    branch = "master",
    remote = "https://github.com/bazelbuild/rules_go.git",
)

git_repository(
    name = "com_github_bazelbuild_buildtools",
    branch = "master",
    remote = "https://github.com/bazelbuild/buildtools.git",
)

# Need to symlink the six repo expected in the protobuf repo.
# This is necessary when loading the py_proto_library rule.
# The version is directly lifted from the protobuf repo WORKSPACE
# at the protobuf repo version listed above.
http_archive(
    name = "six_archive",
    build_file = "@com_google_protobuf//:six.BUILD",
    sha256 = "105f8d68616f8248e24bf0e9372ef04d3cc10104f1980f54d57b2ce73a5ad56a",
    urls = ["https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz#md5=34eed507548117b2ab523ab14b2f8b55"],
)

bind(
    name = "six",
    actual = "@six_archive//:six",
)

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")
load("@com_github_bazelbuild_buildtools//buildifier:deps.bzl", "buildifier_dependencies")
load("@io_bazel_rules_python//python:pip.bzl", "pip_import", "pip_repositories")

go_rules_dependencies()

go_register_toolchains()

buildifier_dependencies()

pip_repositories()

pip_import(
    name = "virtualenv",
    requirements = "//:requirements.txt",
)

load("@virtualenv//:requirements.bzl", "pip_install")

pip_install()
