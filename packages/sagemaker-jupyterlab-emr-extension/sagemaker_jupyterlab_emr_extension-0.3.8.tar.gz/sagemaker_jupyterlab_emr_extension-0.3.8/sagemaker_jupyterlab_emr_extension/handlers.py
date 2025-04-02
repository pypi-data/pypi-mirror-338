import json
import os
import traceback

import botocore
import botocore.credentials
import jsonschema
from jsonschema.exceptions import ValidationError
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.utils import url_path_join
from sagemaker_jupyterlab_extension_common.clients import get_domain_id, get_space_name
from sagemaker_jupyterlab_extension_common.logging.logging_utils import HandlerLogMixin
from sagemaker_jupyterlab_extension_common.util.app_metadata import (
    get_aws_account_id,
    get_domain_id,
    get_space_name,
    get_user_profile_name,
)
from tornado import web

from sagemaker_jupyterlab_emr_extension.clients import (
    get_emr_client,
    get_emrprivate_client,
    get_sagemaker_client,
)
from sagemaker_jupyterlab_emr_extension.converters import (
    convertDescribeClusterResponse,
    convertDescribeDomainResponse,
    convertDescribeUserProfileResponse,
    convertInstanceGroupsResponse,
    convertListClustersResponse,
    convertPersistentAppUIResponse,
)
from sagemaker_jupyterlab_emr_extension.handler.emr_serverless_handlers import (
    GetServerlessApplicationHandler,
    ListServerlessApplicationsHandler,
)
from sagemaker_jupyterlab_emr_extension.schema.api_schema import (
    create_presistent_app_ui_schema,
    describe_cluster_request_schema,
    describe_persistent_app_ui_schema,
    get_on_cluster_app_ui_presigned_url_schema,
    get_persistent_app_ui_presigned_url_schema,
    list_cluster_request_schema,
    list_instance_groups_schema,
)
from sagemaker_jupyterlab_emr_extension.utils.logging_utils import EmrErrorHandler

from ._version import __version__ as ext_version

EXTENSION_NAME = "sagemaker_jupyterlab_emr_extension"
EXTENSION_VERSION = ext_version

from sagemaker_jupyterlab_extension_common.logging.logging_utils import HandlerLogMixin


class DescribeClusterHandler(HandlerLogMixin, JupyterHandler):
    # Do not rename or change the variable names, these are used by
    # loggers in common package.
    jl_extension_name = EXTENSION_NAME
    jl_extension_version = EXTENSION_VERSION

    """
    Response schema
    {
        cluster: Cluster
        errorMessage: String
    }
    """

    @web.authenticated
    async def post(self):
        self.set_header("Content-Type", "application/json")
        try:
            body = self.get_json_body()
            jsonschema.validate(body, describe_cluster_request_schema)
            cluster_id = body["ClusterId"]
            role_arn = body.pop("RoleArn", None)
            self.log.info(
                f"Describe cluster request {cluster_id}",
                extra={"Component": "DescribeCluster"},
            )
            response = await get_emr_client(roleArn=role_arn).describe_cluster(**body)
            self.log.info(
                f"Successfuly described cluster for id {cluster_id}",
                extra={"Component": "DescribeCluster"},
            )
            converted_resp = convertDescribeClusterResponse(response)
            self.set_status(200)
            self.finish(json.dumps(converted_resp))
        except web.HTTPError as e:
            message = e.log_message
            self.log.error(message)
            self.set_status(e.status_code)
            if e.status_code == 400:
                reply = dict(message="Invalid JSON in request", reason=e.reason)
                self.finish(json.dumps(reply))
            else:
                reply = dict(message=message, reason=e.reason)
                self.finish(json.dumps(reply))
        except (
            botocore.exceptions.ParamValidationError,
            ValidationError,
        ) as error:
            self.log.error(
                "Invalid request {} {}".format(body, traceback.format_exc()),
                extra={"Component": "DescribeCluster"},
            )
            self.set_status(400)
            self.finish(
                json.dumps({"errorMessage": "Invalid request missing or wrong input"})
            )
        except botocore.exceptions.ClientError as error:
            self.log.error(
                "SdkClientError {}".format(traceback.format_exc()),
                extra={"Component": "DescribeCluster"},
            )
            msg = EmrErrorHandler.get_boto_error(error)
            self.set_status(msg.get("http_code"))
            self.finish(json.dumps(msg.get("message")))
        except Exception as error:
            self.log.error(
                "Internal Service Error: {}".format(traceback.format_exc()),
                extra={"Component": "DescribeCluster"},
            )
            self.set_status(500)
            self.finish(json.dumps({"errorMessage": str(error)}))


class ListClustersHandler(HandlerLogMixin, JupyterHandler):
    # Do not rename or change the variable names, these are used by
    # loggers in common package.
    jl_extension_name = EXTENSION_NAME
    jl_extension_version = EXTENSION_VERSION

    """
    Response schema
    {
        clusters: [ClusterSummary]!
        errorMessage: String
    }
    """

    @web.authenticated
    async def post(self):
        self.set_header("Content-Type", "application/json")
        try:
            body = self.get_json_body()
            jsonschema.validate(body, list_cluster_request_schema)
            self.log.info(
                f"List clusters request {body}", extra={"Component": "ListClusters"}
            )
            roleArn = body.pop("RoleArn", None)
            response = await get_emr_client(roleArn=roleArn).list_clusters(**body)
            converted_resp = convertListClustersResponse(response)
            self.set_status(200)
            self.finish(json.dumps(converted_resp))
        except web.HTTPError as e:
            message = e.log_message
            self.log.error(message)
            self.set_status(e.status_code)
            if e.status_code == 400:
                reply = dict(message="Invalid JSON in request", reason=e.reason)
                self.finish(json.dumps(reply))
            else:
                reply = dict(message=message, reason=e.reason)
                self.finish(json.dumps(reply))
        except (
            botocore.exceptions.ParamValidationError,
            jsonschema.exceptions.ValidationError,
        ) as error:
            self.log.error(
                "Invalid request {} {}".format(body, traceback.format_exc()),
                extra={"Component": "ListClusters"},
            )
            self.set_status(400)
            self.finish(
                json.dumps({"ErrorMessage": "Invalid request missing or wrong input"})
            )
        except botocore.exceptions.ClientError as error:
            self.log.error(
                "SdkClientError {}".format(traceback.format_exc()),
                extra={"Component": "ListClusters"},
            )
            msg = EmrErrorHandler.get_boto_error(error)
            self.set_status(msg.get("http_code"))
            self.finish(json.dumps(msg.get("message")))
        except Exception as error:
            self.log.error(
                "Internal Service Error: {}".format(traceback.format_exc()),
                extra={"Component": "ListClusters"},
            )
            self.set_status(500)
            self.finish(json.dumps({"error": str(error)}))


class ListInstanceGroupsHandler(HandlerLogMixin, JupyterHandler):
    # Do not rename or change the variable names, these are used by
    # loggers in common package.
    jl_extension_name = EXTENSION_NAME
    jl_extension_version = EXTENSION_VERSION

    """
    Response schema

    InstanceGroup = {
        id: String;
        instanceGroupType: String;
        instanceType: String;
        name: String;
        requestedInstanceCount: Int;
        runningInstanceCount: Int;
    }

    {
        instanceGroups: InstanceGroup
    }
    """

    @web.authenticated
    async def post(self):
        self.set_header("Content-Type", "application/json")
        try:
            body = self.get_json_body()
            jsonschema.validate(body, list_instance_groups_schema)
            cluster_id = body["ClusterId"]
            role_arn = body.pop("RoleArn", None)
            self.log.info(
                f"ListInstanceGroups for cluster {cluster_id}",
                extra={"Component": "ListInstanceGroups"},
            )
            response = await get_emr_client(roleArn=role_arn).list_instance_groups(
                **body
            )
            self.log.info(
                f"Successfuly listed instance groups for cluster {cluster_id}",
                extra={"Component": "ListInstanceGroups"},
            )
            converted_resp = convertInstanceGroupsResponse(response)
            self.set_status(200)
            self.finish(json.dumps(converted_resp))
        except web.HTTPError as e:
            message = e.log_message
            self.log.error(message)
            self.set_status(e.status_code)
            if e.status_code == 400:
                reply = dict(message="Invalid JSON in request", reason=e.reason)
                self.finish(json.dumps(reply))
            else:
                reply = dict(message=message, reason=e.reason)
                self.finish(json.dumps(reply))
        except (
            botocore.exceptions.ParamValidationError,
            ValidationError,
        ) as error:
            self.log.error(
                "Invalid request {} {}".format(body, traceback.format_exc()),
                extra={"Component": "ListInstanceGroups"},
            )
            self.set_status(400)
            self.finish(
                json.dumps({"errorMessage": "Invalid request missing or wrong input"})
            )
        except botocore.exceptions.ClientError as error:
            self.log.error(
                "SdkClientError {}".format(traceback.format_exc()),
                extra={"Component": "ListInstanceGroups"},
            )
            msg = EmrErrorHandler.get_boto_error(error)
            self.set_status(msg.get("http_code"))
            self.finish(json.dumps(msg.get("message")))
        except Exception as error:
            self.log.error(
                "Internal Service Error: {}".format(traceback.format_exc()),
                extra={"Component": "ListInstanceGroups"},
            )
            self.set_status(500)
            self.finish(json.dumps({"errorMessage": str(error)}))


class CreatePersistentAppUiHandler(HandlerLogMixin, JupyterHandler):
    # Do not rename or change the variable names, these are used by
    # loggers in common package.
    jl_extension_name = EXTENSION_NAME
    jl_extension_version = EXTENSION_VERSION

    """
    Response schema
    {
        persistentAppUIId: String
    }
    """

    @web.authenticated
    async def post(self):
        self.set_header("Content-Type", "application/json")
        try:
            body = self.get_json_body()
            jsonschema.validate(body, create_presistent_app_ui_schema)
            target_resource_arn = body.get("TargetResourceArn")
            role_arn = body.pop("RoleArn", None)
            self.log.info(
                f"Create Persistent App UI for Arn {target_resource_arn}",
                extra={"Component": "CreatePersistentAppUI"},
            )
            response = await get_emrprivate_client(
                roleArn=role_arn
            ).create_persistent_app_ui(**body)
            persistent_app_ui_id = response.get("PersistentAppUIId")
            self.log.info(
                f"Successfully cretaed Persistent App UI withId {persistent_app_ui_id}",
                extra={"Component": "CreatePersistentAppUI"},
            )
            converted_resp = {
                "persistentAppUIId": persistent_app_ui_id,
                "roleArn": role_arn,
            }
            self.set_status(200)
            self.finish(json.dumps(converted_resp))
        except web.HTTPError as e:
            message = e.log_message
            self.log.error(message)
            self.set_status(e.status_code)
            if e.status_code == 400:
                reply = dict(message="Invalid JSON in request", reason=e.reason)
                self.finish(json.dumps(reply))
            else:
                reply = dict(message=message, reason=e.reason)
                self.finish(json.dumps(reply))
        except (
            botocore.exceptions.ParamValidationError,
            jsonschema.exceptions.ValidationError,
        ) as error:
            self.log.error(
                "Invalid request {} {}".format(body, traceback.format_exc()),
                extra={"Component": "CreatePersistentAppUI"},
            )
            self.set_status(400)
            self.finish(
                json.dumps({"ErrorMessage": "Invalid request missing or wrong input"})
            )
        except botocore.exceptions.ClientError as error:
            self.log.error(
                "SdkClientError {}".format(traceback.format_exc()),
                extra={"Component": "CreatePersistentAppUI"},
            )
            msg = EmrErrorHandler.get_boto_error(error)
            self.set_status(msg.get("http_code"))
            self.finish(json.dumps(msg.get("message")))
        except Exception as error:
            self.log.error(
                "Internal Service Error: {}".format(traceback.format_exc()),
                extra={"Component": "CreatePersistentAppUI"},
            )
            self.set_status(500)
            self.finish(json.dumps({"error": str(error)}))


class DescribePersistentAppUiHandler(HandlerLogMixin, JupyterHandler):
    # Do not rename or change the variable names, these are used by
    # loggers in common package.
    jl_extension_name = EXTENSION_NAME
    jl_extension_version = EXTENSION_VERSION

    """
    Response schema
    {
        persistentAppUI: PersistentAppUI
        errorMessage: String
    }
    """

    @web.authenticated
    async def post(self):
        self.set_header("Content-Type", "application/json")
        try:
            body = self.get_json_body()
            jsonschema.validate(body, describe_persistent_app_ui_schema)
            persistent_app_ui_id = body.get("PersistentAppUIId")
            role_arn = body.pop("RoleArn", None)
            self.log.info(
                f"DescribePersistentAppUi for Id {persistent_app_ui_id}",
                extra={"Component": "DescribePersistentAppUI"},
            )
            response = await get_emrprivate_client(
                roleArn=role_arn
            ).describe_persistent_app_ui(**body)
            converted_resp = convertPersistentAppUIResponse(response)
            converted_resp["roleArn"] = role_arn
            self.set_status(200)
            self.finish(json.dumps(converted_resp))
        except web.HTTPError as e:
            message = e.log_message
            self.log.error(message)
            self.set_status(e.status_code)
            if e.status_code == 400:
                reply = dict(message="Invalid JSON in request", reason=e.reason)
                self.finish(json.dumps(reply))
            else:
                reply = dict(message=message, reason=e.reason)
                self.finish(json.dumps(reply))
        except (
            botocore.exceptions.ParamValidationError,
            jsonschema.exceptions.ValidationError,
        ) as error:
            self.log.error(
                "Invalid request {} {}".format(body, traceback.format_exc()),
                extra={"Component": "DescribePersistentAppUI"},
            )
            self.set_status(400)
            self.finish(
                json.dumps({"errorMessage": "Invalid request missing or wrong input"})
            )
        except botocore.exceptions.ClientError as error:
            self.log.error(
                "SdkClientError {}".format(traceback.format_exc()),
                extra={"Component": "DescribePersistentAppUI"},
            )
            msg = EmrErrorHandler.get_boto_error(error)
            self.set_status(msg.get("http_code"))
            self.finish(json.dumps(msg.get("message")))
        except Exception as error:
            self.log.error(
                "Internal Service Error: {}".format(traceback.format_exc()),
                extra={"Component": "DescribePersistentAppUI"},
            )
            self.set_status(500)
            self.finish(json.dumps({"error": str(error)}))


class GetPersistentAppUiPresignedUrlHandler(HandlerLogMixin, JupyterHandler):
    # Do not rename or change the variable names, these are used by
    # loggers in common package.
    jl_extension_name = EXTENSION_NAME
    jl_extension_version = EXTENSION_VERSION

    """
    Response schema
    {
        presignedURLReady: Boolean
        presignedURL: String
    }
    """

    @web.authenticated
    async def post(self):
        self.set_header("Content-Type", "application/json")
        try:
            body = self.get_json_body()
            jsonschema.validate(body, get_persistent_app_ui_presigned_url_schema)
            role_arn = body.pop("RoleArn", None)
            persistent_app_ui_id = body["PersistentAppUIId"]
            self.log.info(
                f"Get Persistent App UI for {persistent_app_ui_id}",
                extra={"Component": "GetPersistentAppUiPresignedUrl"},
            )
            response = await get_emrprivate_client(
                roleArn=role_arn
            ).get_persistent_app_ui_presigned_url(**body)
            converted_resp = {
                "presignedURLReady": response.get("PresignedURLReady"),
                "presignedURL": response.get("PresignedURL"),
            }
            self.set_status(200)
            self.finish(json.dumps(converted_resp))
        except web.HTTPError as e:
            message = e.log_message
            self.log.error(message)
            self.set_status(e.status_code)
            if e.status_code == 400:
                reply = dict(message="Invalid JSON in request", reason=e.reason)
                self.finish(json.dumps(reply))
            else:
                reply = dict(message=message, reason=e.reason)
                self.finish(json.dumps(reply))
        except (
            botocore.exceptions.ParamValidationError,
            jsonschema.exceptions.ValidationError,
        ) as error:
            self.log.error(
                "Invalid request {} {}".format(body, traceback.format_exc()),
                extra={"Component": "GetPersistentAppUiPresignedUrl"},
            )
            self.set_status(400)
            self.finish(
                json.dumps({"errorMessage": "Invalid request missing or wrong input"})
            )
        except botocore.exceptions.ClientError as error:
            self.log.error(
                "SdkClientError {}".format(traceback.format_exc()),
                extra={"Component": "GetPersistentAppUiPresignedUrl"},
            )
            msg = EmrErrorHandler.get_boto_error(error)
            self.set_status(msg.get("http_code"))
            self.finish(json.dumps(msg.get("message")))
        except Exception as error:
            self.log.error(
                "Internal Service Error: {}".format(traceback.format_exc()),
                extra={"Component": "GetPersistentAppUiPresignedUrl"},
            )
            self.set_status(500)
            self.finish(json.dumps({"error": str(error)}))


class GetOnClustersAppUiPresignedUrlHandler(HandlerLogMixin, JupyterHandler):
    # Do not rename or change the variable names, these are used by
    # loggers in common package.
    jl_extension_name = EXTENSION_NAME
    jl_extension_version = EXTENSION_VERSION

    """
    Response schema
    {
        presignedURLReady: Boolean
        presignedURL: String
    }
    """

    @web.authenticated
    async def post(self):
        self.set_header("Content-Type", "application/json")
        try:
            body = self.get_json_body()
            jsonschema.validate(body, get_on_cluster_app_ui_presigned_url_schema)
            cluster_id = body["ClusterId"]
            role_arn = body.get("RoleArn", None)
            self.log.info(
                f"GetOnClusterAppUiPresignedUrl for cluster id {cluster_id}",
                extra={"Component": "GetOnClustersAppUiPresignedUrl"},
            )
            response = await get_emrprivate_client(
                roleArn=role_arn
            ).get_on_cluster_app_ui_presigned_url(**body)
            converted_resp = {
                "presignedURLReady": response.get("PresignedURLReady"),
                "presignedURL": response.get("PresignedURL"),
            }
            self.set_status(200)
            self.finish(json.dumps(converted_resp))
        except web.HTTPError as e:
            message = e.log_message
            self.log.error(message)
            self.set_status(e.status_code)
            if e.status_code == 400:
                reply = dict(message="Invalid JSON in request", reason=e.reason)
                self.finish(json.dumps(reply))
            else:
                reply = dict(message=message, reason=e.reason)
                self.finish(json.dumps(reply))
        except (
            botocore.exceptions.ParamValidationError,
            jsonschema.exceptions.ValidationError,
        ) as error:
            self.log.error(
                "Invalid request {} {}".format(body, traceback.format_exc()),
                extra={"Component": "GetOnClustersAppUiPresignedUrl"},
            )
            self.set_status(400)
            self.finish(
                json.dumps({"errorMessage": "Invalid request missing or wrong input"})
            )
        except botocore.exceptions.ClientError as error:
            self.log.error(
                "SdkClientError {}".format(traceback.format_exc()),
                extra={"Component": "GetOnClustersAppUiPresignedUrl"},
            )
            msg = EmrErrorHandler.get_boto_error(error)
            self.set_status(msg.get("http_code"))
            self.finish(json.dumps(msg.get("message")))
        except Exception as error:
            self.log.error(
                "Internal Service Error: {}".format(traceback.format_exc()),
                extra={"Component": "GetOnClustersAppUiPresignedUrl"},
            )
            self.set_status(500)
            self.finish(json.dumps({"error": str(error)}))


# This is a custom handler calling multiple APIs to fetch EMR assumable
# and execution roles
class FetchEMRRolesHandler(HandlerLogMixin, JupyterHandler):
    # Do not rename or change the variable names, these are used by
    # loggers in common package.
    jl_extension_name = EXTENSION_NAME
    jl_extension_version = EXTENSION_VERSION

    """
    Response schema
    {
        EmrAssumableRoleArns: [roleArn]!
        EmrExecutionRoleArns: [roleArn]!
        CallerAccountId: String
        ErrorMessage: String
    }
    """

    @web.authenticated
    async def post(self):
        self.set_header("Content-Type", "application/json")
        try:
            client = get_sagemaker_client()
            domain_id = get_domain_id()
            space_name = get_space_name()
            space_details = await client.describe_space(
                DomainId=domain_id, SpaceName=space_name
            )
            space_type = space_details.get("SpaceSharingSettings", {}).get(
                "SharingType"
            )
            # Since there is no easy way to get user name directly, we get it from space owner name. If the
            # space is a shared space, we would use the EmrSettings under domain instead.
            if space_type == "Private":
                user_profile_name = space_details.get("OwnershipSettings", {}).get(
                    "OwnerUserProfileName", None
                )
                describe_user_profile_response = await client.describe_user_profile(
                    DomainId=domain_id, UserProfileName=user_profile_name
                )
                converted_response = convertDescribeUserProfileResponse(
                    response=describe_user_profile_response
                )

                # if both role arn lists under user are empty, use domain level EMR roles
                if (not converted_response.get("EmrAssumableRoleArns")) and (
                    not converted_response.get("EmrExecutionRoleArns")
                ):
                    describe_domain_response = await client.describe_domain(
                        DomainId=domain_id
                    )
                    converted_response = convertDescribeDomainResponse(
                        response=describe_domain_response
                    )
            else:
                describe_domain_response = await client.describe_domain(
                    DomainId=domain_id
                )
                converted_response = convertDescribeDomainResponse(
                    response=describe_domain_response
                )

            # add more keys to response
            converted_response.update({"CallerAccountId": get_aws_account_id()})
            self.set_status(200)
            self.finish(json.dumps(converted_response))
        except web.HTTPError as e:
            message = e.log_message
            self.log.error(message)
            self.set_status(e.status_code)
            if e.status_code == 400:
                reply = dict(message="Invalid JSON in request", reason=e.reason)
                self.finish(json.dumps(reply))
            else:
                reply = dict(message=message, reason=e.reason)
                self.finish(json.dumps(reply))
        except (
            botocore.exceptions.ParamValidationError,
            jsonschema.exceptions.ValidationError,
        ) as error:
            self.log.error(
                "Invalid request {}".format(traceback.format_exc()),
                extra={"Component": "FetchEMRRoles"},
            )
            self.set_status(400)
            self.finish(
                json.dumps({"ErrorMessage": "Invalid request missing or wrong input"})
            )
        except botocore.exceptions.ClientError as error:
            self.log.error(
                "SdkClientError {}".format(traceback.format_exc()),
                extra={"Component": "FetchEMRRoles"},
            )
            msg = EmrErrorHandler.get_boto_error(error)
            self.set_status(msg.get("http_code"))
            self.finish(json.dumps({"ErrorMessage": msg.get("message")}))
        except Exception as e:
            self.log.error(
                "Internal Service Error: {}".format(traceback.format_exc()),
                extra={"Component": "FetchEMRRoles"},
            )
            self.set_status(500)
            self.finish(json.dumps({"ErrorMessage": str(e)}))


def build_url(web_app, endpoint):
    base_url = web_app.settings["base_url"]
    return url_path_join(base_url, endpoint)


def register_handlers(nbapp):
    web_app = nbapp.web_app
    host_pattern = ".*$"
    handlers = [
        (
            build_url(web_app, r"/aws/sagemaker/api/emr/describe-cluster"),
            DescribeClusterHandler,
        ),
        (
            build_url(web_app, r"/aws/sagemaker/api/emr/list-clusters"),
            ListClustersHandler,
        ),
        (
            build_url(web_app, r"/aws/sagemaker/api/emr/create-persistent-app-ui"),
            CreatePersistentAppUiHandler,
        ),
        (
            build_url(web_app, r"/aws/sagemaker/api/emr/describe-persistent-app-ui"),
            DescribePersistentAppUiHandler,
        ),
        (
            build_url(
                web_app, r"/aws/sagemaker/api/emr/get-persistent-app-ui-presigned-url"
            ),
            GetPersistentAppUiPresignedUrlHandler,
        ),
        (
            build_url(
                web_app, r"/aws/sagemaker/api/emr/get-on-cluster-app-ui-presigned-url"
            ),
            GetOnClustersAppUiPresignedUrlHandler,
        ),
        (
            build_url(web_app, r"/aws/sagemaker/api/emr/list-instance-groups"),
            ListInstanceGroupsHandler,
        ),
        (
            build_url(web_app, r"/aws/sagemaker/api/sagemaker/fetch-emr-roles"),
            FetchEMRRolesHandler,
        ),
        (
            build_url(web_app, r"/aws/sagemaker/api/emr-serverless/list-applications"),
            ListServerlessApplicationsHandler,
        ),
        (
            build_url(web_app, r"/aws/sagemaker/api/emr-serverless/get-application"),
            GetServerlessApplicationHandler,
        ),
    ]
    web_app.add_handlers(host_pattern, handlers)
