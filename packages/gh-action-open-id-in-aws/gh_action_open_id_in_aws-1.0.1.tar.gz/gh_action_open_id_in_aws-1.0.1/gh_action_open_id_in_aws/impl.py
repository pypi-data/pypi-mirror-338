# -*- coding: utf-8 -*-

"""
This module automates the setup of GitHub Actions OpenID Connect (OIDC) integration with AWS.
It creates the necessary AWS resources to enable secure authentication between GitHub Actions
workflows and AWS services without storing long-term credentials.
"""

import typing as T

from boto_session_manager import BotoSesManager
import aws_cloudformation.api as aws_cf
from aws_cloudformation.deploy import DeployStackResponse

from .paths import path_cft


def setup_github_action_open_id_connection_in_aws(
    aws_profile: str,
    stack_name: str,
    github_repo_patterns: list[str],
    role_name: str = "",
    oidc_provider_arn: str = "",
    oidc_audience: str = "sts.amazonaws.com",
    tags: T.Optional[T.Dict[str, str]] = None,
    skip_prompt: bool = True,
    verbose: bool = True,
) -> DeployStackResponse:
    """
    The OpenID Connect (OIDC) identity provider that allows the GitHub Actions
    to assume the role in the target account.

    :param aws_profile: AWS profile name to use for deployment. This profile should have
        sufficient permissions to create IAM roles and OIDC providers.
    :param stack_name: Name for the CloudFormation stack that will be created.
    :param github_repo_patterns: List of GitHub repository patterns to allow access.
        Each pattern should be in the format: ``repo:${github_org}/${github_repo_name}:*``
        or ``repo:${github_org}/${github_repo_name_prefix}*:*``
        Example: ``["repo:MyOrg/my-repo:*", "repo:MyOrg/prefix*:*", "repo:MyOrg/another-repo:ref:refs/heads/main"]``
    :param role_name: Name of the IAM role to be created and assumed by GitHub Actions.
        If empty, the stack will only create the OIDC provider without an IAM role.
    :param oidc_provider_arn: ARN of an existing GitHub OIDC provider in your AWS account.
        If provided, the function will reuse this provider instead of creating a new one.
        If empty, a new OIDC provider will be created.
        Format: "arn:aws:iam::{aws_account_id}:oidc-provider/token.actions.githubusercontent.com"
    :param oidc_audience: Audience value for the OIDC provider, typically "sts.amazonaws.com".
    :param tags: Optional dictionary of tags to apply to AWS resources created by the stack.
    :param skip_prompt: default False; if False, you have to enter "Yes"
        in prompt to do deployment; if True, then execute the deployment directly.
    :param verbose: whether you want to log information to console

    Notes:

    - The IAM role created will not have any permissions by default. You need to
      attach appropriate policies after creation.
    - When reusing an existing OIDC provider (oidc_provider_arn is provided) and
      not creating a role (role_name is empty), no deployment will happen.
    - The stack adds standard technical tags to all resources for tracking purposes.

    :returns: ``DeployStackResponse`` Object containing information about the deployment result.
    """
    # Skip deployment if we're just reusing an OIDC provider without creating a role
    if (bool(oidc_provider_arn) is True) and (bool(role_name) is False):
        return DeployStackResponse(
            is_deploy_happened=False,
        )

    bsm = BotoSesManager(profile_name=aws_profile)

    # Set up default resource tags for tracking and management
    final_tags = {
        "tech:cloudformation_stack": f"arn:aws:cloudformation:{bsm.aws_region}:{bsm.aws_account_id}:stack/{stack_name}",
        "tech:human_creator": bsm.sts_client.get_caller_identity()["Arn"],
        "tech:machine_creator": "gh_action_open_id_in_aws Python library",
    }
    if tags is not None:
        final_tags.update(tags)

    # Deploy the CloudFormation stack using the template from the package
    deploy_stack_response = aws_cf.deploy_stack(
        bsm=bsm,
        stack_name=stack_name,
        template=path_cft.read_text(),
        parameters=[
            aws_cf.Parameter(
                key="GithubRepoPatterns", value=",".join(github_repo_patterns)
            ),
            aws_cf.Parameter(key="RoleName", value=role_name),
            aws_cf.Parameter(key="OIDCProviderArn", value=oidc_provider_arn),
            aws_cf.Parameter(key="OIDCAudience", value=oidc_audience),
        ],
        skip_prompt=skip_prompt,
        include_named_iam=True,
        tags=final_tags,
        verbose=verbose,
    )

    return deploy_stack_response
