# src/wiz_mcp/server.py
import asyncio
import os
from typing import Any
import aiohttp
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server with dependencies
dep = ["aiohttp","asyncio"]
mcp = FastMCP("wiz-mcp", dependencies=dep)

# Environment variables
USER = os.environ.get('KS_USER', 'admin')
BASE_URL = os.environ.get('KS_APISERVER_ENDPOINT', 'http://172.31.17.47:30881')
TOKEN = os.environ.get('KS_TOKEN', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwOi8va3MtY29uc29sZS5rdWJlc3BoZXJlLXN5c3RlbS5zdmM6MzA4ODAiLCJzdWIiOiJhZG1pbiIsImV4cCI6MTc0MzU4NzExNywiaWF0IjoxNzQzNTc5OTE3LCJ0b2tlbl90eXBlIjoiYWNjZXNzX3Rva2VuIiwidXNlcm5hbWUiOiJhZG1pbiJ9.JWhquqO5b0gPRiToOVhZIHsKYUyrsURLa5PiDVLEOu0')

HEADERS = {
    "Accept": "application/json",
    "X-Remote-User": USER,
    "Authorization": f"Bearer {TOKEN}"
}

async def fetch_json(session: aiohttp.ClientSession, url: str) -> Any:
    async with session.get(url, headers=HEADERS) as response:
        return await response.json()

@mcp.tool()
async def get_logging(cluster: str, pod: str) -> Any:
    """Get logs and events
    Args:
        cluster: Cluster name
        pod: Pod name
    """
    url = f"{BASE_URL}/kapis/logging.kubesphere.io/v1alpha2/logs?cluster={cluster}&pods={pod}&size=30"
    async with aiohttp.ClientSession() as session:
        return await fetch_json(session, url)

@mcp.tool()
async def get_events(cluster: str, pod: str) -> Any:
    """Get logs and events
    Args:
        cluster: Cluster name
        pod: Pod name
    """
    url = f"{BASE_URL}/kapis/logging.kubesphere.io/v1alpha2/events?cluster={cluster}&involved_object_name_filter={pod}&size=30"
    async with aiohttp.ClientSession() as session:
        return await fetch_json(session, url)

@mcp.tool()
async def list_all_clusters() -> Any:
    """Get all clusters"""
    url = f"{BASE_URL}/kapis/tenant.kubesphere.io/v1beta1/clusters"
    async with aiohttp.ClientSession() as session:
        resp = await fetch_json(session, url)
        return [cluster['metadata']['name'] for cluster in resp['items']]

@mcp.tool()
async def list_cluster_resources(cluster: list[str],resourceType: str) -> Any:
    """ Get the specified resource for the specified cluster list
    Args:
        cluster: cluster name list
        resourceType: K8s Resource type (e.g., pods, deployments,configmaps,secrets,namespaces, etc.)
    """
    urls = [f"{BASE_URL}/clusters/{c}/kapis/resources.kubesphere.io/v1alpha3/{resourceType}" for c in cluster]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_json(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for i, resp in enumerate(responses):
            responses[i] = [
                {
                    "cluster": cluster[i],
                    "name": item['metadata']['name'],
                    "namespace": item['metadata'].get('namespace', 'N/A')
                }
                for item in resp['items']
            ]
        return responses

# 获取指定资源的全部信息
@mcp.tool()
async def get_namespace_resource_info(cluster: str, resourceType: str,namespace: str, name: str) -> Any:
    """Get the specified namespace level resource from the specified cluster
    Args:
        cluster: Cluster name
        resourceType: K8s Resource type (e.g., pods, deployments,configmaps,secrets, etc.)
        namespace: Namespace name
        name: Resource name
    """
    url = f"{BASE_URL}/clusters/{cluster}/kapis/resources.kubesphere.io/v1alpha3/namespaces/{namespace}/{resourceType}"
    async with aiohttp.ClientSession() as session:
        resp = await fetch_json(session, url)
        for item in resp['items']:
            if item['metadata']['name'] == name:
                return item
    return None

@mcp.tool()
async def get_cluster_resource_info(cluster: str, resourceType: str, name: str) -> Any:
    """Get the specified cluster level resource from the specified cluster
    Args:
        cluster: Cluster name
        resourceType: K8s Resource type (e.g. clusters,namespaces etc.)
        name: Resource name
    """
    url = f"{BASE_URL}/clusters/{cluster}/kapis/resources.kubesphere.io/v1alpha3/{resourceType}"
    async with aiohttp.ClientSession() as session:
        resp = await fetch_json(session, url)
        for item in resp['items']:
            if item['metadata']['name'] == name:
                return item
    return None


@mcp.prompt()
def analyse_special_cluster(cluster: str) -> str:
    """Analyse all clusters and provide report
    Args:
        cluster: Cluster name
    """
    return f"Please analyse the cluster {cluster} status and give me a report."

@mcp.prompt()
def analyse_all_cluster() -> Any:
    """Analyze all clusters and provide a summary report
    """
    return "Please analyse all cluster status and give me a report"

def start_server() -> None:
    """Initialize and run the server"""
    mcp.run(transport="stdio")

if __name__ == "__main__":
    start_server()