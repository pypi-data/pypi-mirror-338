# -*- coding: utf-8 -*-

"""
Setup automation for Cloudflare.
"""

import typing as T
import os
import subprocess
import dataclasses
from functools import cached_property

try:
    import boto3
    import botocore.exceptions
except ImportError:  # pragma: no cover
    pass

from .vendor.emoji import Emoji
from .vendor.better_pathlib import temp_cwd

from .logger import logger
from .runtime import IS_CI
from .helpers import print_command

if T.TYPE_CHECKING:  # pragma: no cover
    from .define import PyWf
    from boto3 import Session
    from mypy_boto3_codeartifact.client import CodeArtifactClient


@dataclasses.dataclass
class PyWfCloudflare:  # pragma: no cover
    """
    Namespace class for Cloudflare setup automation.
    """

    @cached_property
    def cloudflare_token(self: "PyWf") -> str:
        if self.path_cloudflare_token_file.exists():
            return self.path_cloudflare_token_file.read_text(encoding="utf-8").strip()
        else:  # pragma: no cover
            message = (
                f"{Emoji.error} Cannot find Cloudflare token file at "
                f"{self.path_cloudflare_token_file}!\n"
                f"{self.__class__.path_cloudflare_token_file.__doc__}"
            )
            raise FileNotFoundError(message)

    @logger.emoji_block(
        msg="Create Cloudflare Pages project",
        emoji=Emoji.doc,
    )
    def create_cloudflare_pages_project(
        self: "PyWf",
        real_run: bool = True,
        verbose: bool = False,
    ):
        os.environ["CLOUDFLARE_API_TOKEN"] = self.cloudflare_token
        args = [
            f"{self.path_bin_wrangler}",
            "pages",
            "project",
            "create",
            self.package_name_slug,
            "--production-branch",
            "main",
        ]
        if real_run:
            with temp_cwd(self.dir_project_root):
                subprocess.run(args, check=True)

    @logger.emoji_block(
        msg="Create Cloudflare Pages project",
        emoji=Emoji.doc,
    )
    def deploy_cloudflare_pages(
        self: "PyWf",
        real_run: bool = True,
        verbose: bool = False,
    ):
        os.environ["CLOUDFLARE_API_TOKEN"] = self.cloudflare_token
        args = [
            f"{self.path_bin_wrangler}",
            "pages",
            "deploy",
            f"{self.dir_sphinx_doc_build_html}",
            f"--project-name={self.package_name_slug}",
        ]
        if real_run:
            with temp_cwd(self.dir_project_root):
                subprocess.run(args, check=True)
