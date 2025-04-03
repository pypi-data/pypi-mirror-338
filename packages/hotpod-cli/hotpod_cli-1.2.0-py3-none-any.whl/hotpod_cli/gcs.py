"""HotPod CLI GCS API 客户端"""

import os
import click
import click_spinner
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTPS
from jdcloud_sdk.services.gcs.client.GcsClient import GcsClient
from jdcloud_sdk.services.gcs.apis.DescribeInstancesRequest import DescribeInstancesRequest
from jdcloud_sdk.services.gcs.apis.DescribeInstanceRequest import DescribeInstanceRequest
from jdcloud_sdk.services.gcs.apis.CreateInstancesRequest import CreateInstancesRequest
from jdcloud_sdk.services.gcs.apis.DeleteInstanceRequest import DeleteInstanceRequest
from jdcloud_sdk.core.logger import Logger

# 创建日志记录器
logger = Logger(0)


class GCS:
    """京东云 GCS API 客户端
    
    用于与京东云GCS API进行交互的客户端类，提供创建、删除、列出和获取实例详情等功能。
    使用环境变量JDCLOUD_AK和JDCLOUD_SK进行身份验证。
    """
    
    def __init__(self):
        """初始化GCS客户端
        
        从环境变量加载凭证并设置GCS客户端配置
        """
        self.access_key = os.environ.get('JDCLOUD_AK')
        self.secret_key = os.environ.get('JDCLOUD_SK')
        self.credentials = Credential(self.access_key, self.secret_key)
        self.config = Config(
            scheme=SCHEME_HTTPS,
            timeout=60
        )
        self.client = GcsClient(self.credentials, self.config, logger=logger)
        self.region_id = 'cn-central-xy1'
        self.az = 'cn-central-xy1a'
        

    def create_instance(self, num=1, image_id=None, sku_id=None):
        """创建GCS实例
        
        Args:
            num: 要创建的实例数量
            image_id: 镜像ID，如果未指定则使用默认值
            sku_id: SKU ID，如果未指定则使用默认值
            
        Returns:
            实例ID列表，如果创建失败则返回None
        """
        try:
            # 临时禁用调试输出
            os.environ['JDCLOUD_SDK_DEBUG'] = 'false'
            parameters = {
                'regionId': self.region_id,
                'instanceSpec': {
                    'az': self.az,
                    'count': num,
                    'charge': {
                        "chargeMode": "postpaid_by_duration",
                    },
                    'skuId': sku_id or 'gcssku-dkdueldlsid',
                    'imageId': image_id or 'i-de9b194080374b52a00089b143be',
                }
            }
            request = CreateInstancesRequest(parameters, header={'X-JDCLOUD-PROFILE': 'PROFILE_INNER_CUSTOM'})
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return None
            else:
                return resp.result.get('instanceIds', [])
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return None

    def delete_instance(self, instance_id):
        """删除GCS实例
        
        Args:
            instance_id: 要删除的实例ID
            
        Returns:
            删除是否成功
        """
        try:
            parameters = {
                'regionId': self.region_id,
                'instanceId': instance_id
            }
            request = DeleteInstanceRequest(parameters)
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return False
            else:
                return True
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return False

    def list_instances(self):
        """列出所有GCS实例
        
        Returns:
            实例列表，如果获取失败则返回None
        """
        try:
            parameters = {
                'regionId': self.region_id,
                'az': self.az,
                'pageNumber': 1,
                'pageSize': 100
            }
            request = DescribeInstancesRequest(parameters)
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return None
            else:
                return resp.result.get('list', [])
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return None

    def get_instance(self, instance_id):
        """获取GCS实例详情
        
        Args:
            instance_id: 实例ID
            
        Returns:
            实例详情，如果获取失败则返回None
        """
        try:
            parameters = {
                'regionId': self.region_id,
                'instanceId': instance_id
            }
            request = DescribeInstanceRequest(parameters)
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return None
            else:
                return resp.result
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return None

    def create_cluster(self, cluster_name):
        """创建集群
        
        Args:
            cluster_name: 集群名称，必须唯一
            
        Returns:
            创建成功返回集群信息字典，失败返回None
        """
        try:
            parameters = {
                'regionId': self.region_id,
                'clusterSpec': {
                    'name': cluster_name,
                    'description': f'Cluster created by HotPod CLI: {cluster_name}'
                }
            }
            # 这里需要根据实际API调整
            from jdcloud_sdk.services.gcs.apis.CreateClusterRequest import CreateClusterRequest
            request = CreateClusterRequest(parameters)
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return None
            else:
                return resp.result
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return None
            
    def add_instances_to_cluster(self, cluster_name, instance_ids):
        """向集群中添加实例
        
        Args:
            cluster_name: 集群名称
            instance_ids: 实例ID列表
            
        Returns:
            添加成功返回True，失败返回False
        """
        try:
            parameters = {
                'regionId': self.region_id,
                'clusterName': cluster_name,
                'instanceIds': instance_ids
            }
            # 这里需要根据实际API调整
            from jdcloud_sdk.services.gcs.apis.AddInstancesToClusterRequest import AddInstancesToClusterRequest
            request = AddInstancesToClusterRequest(parameters)
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return False
            else:
                return True
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return False
            
    def list_clusters(self):
        """列出所有集群
        
        Returns:
            集群列表，如果获取失败则返回None
        """
        try:
            parameters = {
                'regionId': self.region_id,
                'pageNumber': 1,
                'pageSize': 100
            }
            # 这里需要根据实际API调整
            from jdcloud_sdk.services.gcs.apis.DescribeClustersRequest import DescribeClustersRequest
            request = DescribeClustersRequest(parameters)
            resp = self.client.send(request)
            if resp.error is not None:
                click.secho(f"Error: {resp.error.code} - {resp.error.message}", fg='red')
                return None
            else:
                return resp.result.get('list', [])
        except Exception as e:
            click.secho(f"Error occurred: {str(e)}", fg='red')
            return None 