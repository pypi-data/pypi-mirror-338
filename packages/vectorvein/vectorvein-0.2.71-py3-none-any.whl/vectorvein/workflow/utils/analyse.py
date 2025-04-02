import json
from typing import TypedDict, Any


class PortRecord(TypedDict):
    """
    端口记录
    """

    name: str
    type: str
    show: bool
    value: Any
    connected: bool


class NodeRecord(TypedDict):
    """
    节点记录
    """

    id: str
    name: str
    type: str
    category: str
    ports: list[PortRecord]


class AnalyseResult(TypedDict):
    """
    分析结果
    """

    nodes: list[NodeRecord]


def analyse_workflow_record(
    json_str: str, connected_only: bool = False, reserver_programming_function_ports: bool = False
) -> AnalyseResult:
    """
    分析工作流JSON字符串，提取节点和端口信息

    Args:
        json_str: 工作流JSON字符串

    Returns:
        分析结果
    """
    # 解析JSON
    workflow_data = json.loads(json_str)

    # 收集所有连接的端口
    connected_ports = set()
    for edge in workflow_data["edges"]:
        source_id = edge["source"]
        target_id = edge["target"]
        source_handle = edge["sourceHandle"]
        target_handle = edge["targetHandle"]
        connected_ports.add((source_id, source_handle))
        connected_ports.add((target_id, target_handle))

    # 分析节点
    nodes_records = []

    for node in workflow_data["nodes"]:
        node_id = node["id"]
        node_type = node["type"]
        category = node["category"]

        # 跳过辅助节点
        if category == "assistedNodes":
            continue

        # 获取任务名称
        task_name = node["data"]["task_name"].split(".")[-1] if "task_name" in node["data"] else ""

        # 收集端口信息
        ports_records = []

        if "template" in node["data"]:
            for port_name, port in node["data"]["template"].items():
                if "name" not in port:
                    continue

                port_is_connected = (node_id, port["name"]) in connected_ports

                if node_type != "ProgrammingFunction" or not reserver_programming_function_ports:
                    if connected_only and not port_is_connected:
                        continue

                port_record: PortRecord = {
                    "name": port["name"],
                    "type": port.get("field_type", port.get("type", "")),
                    "show": port.get("show", False),
                    "value": port.get("value", None),
                    "connected": port_is_connected,
                }

                ports_records.append(port_record)

        # 创建节点记录
        node_record: NodeRecord = {
            "id": node_id,
            "name": task_name,
            "type": node_type,
            "category": category,
            "ports": ports_records,
        }

        nodes_records.append(node_record)

    # 返回分析结果
    result: AnalyseResult = {"nodes": nodes_records}

    return result
