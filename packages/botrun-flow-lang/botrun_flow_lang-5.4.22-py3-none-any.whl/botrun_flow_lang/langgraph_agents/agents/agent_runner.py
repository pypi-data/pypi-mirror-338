import logging
from typing import AsyncGenerator, Dict, List, Optional, Union
from langgraph.graph.state import CompiledStateGraph
from pydantic import BaseModel
from botrun_flow_lang.utils.botrun_logger import default_logger


class StepsUpdateEvent(BaseModel):
    """
    for step in steps:
        print("Description:", step.get("description", ""))
        print("Status:", step.get("status", ""))
        print("Updates:", step.get("updates", ""))
    """

    steps: List = []


class OnNodeStreamEvent(BaseModel):
    chunk: str


async def langgraph_runner(
    thread_id: str,
    init_state: dict,
    graph: CompiledStateGraph,
    need_resume: bool = False,
) -> AsyncGenerator:
    invoke_state = init_state
    config = {"configurable": {"thread_id": thread_id}}
    if need_resume:
        state_history = []
        async for state in graph.aget_state_history(config):
            state_history.append(state)
        checkpoint_id = ""
        if len(state_history) > 0:
            # 最新的會在 state_history[0]
            checkpoint_id = (
                state_history[0].config.get("configurable", {}).get("checkpoint_id", "")
            )
        if checkpoint_id:
            config["configurable"]["checkpoint_id"] = checkpoint_id
            invoke_state = None
    # todo 要怎麼重新開始，而不是再遇到 recursion limit
    async for event in graph.astream_events(
        invoke_state,
        config,
        version="v2",
    ):
        state = await graph.aget_state(config)
        # print(state.config)

        yield event


async def agent_runner(
    thread_id: str,
    init_state: dict,
    graph: CompiledStateGraph,
    need_resume: bool = False,
    logger: logging.Logger = default_logger,
) -> AsyncGenerator[Union[StepsUpdateEvent, OnNodeStreamEvent], None]:
    invoke_state = init_state
    config = {"configurable": {"thread_id": thread_id}}
    if need_resume:
        state_history = []
        async for state in graph.aget_state_history(config):
            state_history.append(state)
        checkpoint_id = ""
        if len(state_history) > 0:
            # 最新的會在 state_history[0]
            checkpoint_id = (
                state_history[0].config.get("configurable", {}).get("checkpoint_id", "")
            )
        if checkpoint_id:
            config["configurable"]["checkpoint_id"] = checkpoint_id
            invoke_state = None
    async for event in graph.astream_events(
        invoke_state,
        config,
        version="v2",
    ):
        if event["event"] == "on_chain_end":
            pass
            # print(event)
        if event["event"] == "on_chat_model_end":
            pass
            # for step_event in handle_copilotkit_intermediate_state(event):
            #     yield step_event
        if event["event"] == "on_chat_model_stream":
            data = event["data"]
            if (
                data["chunk"].content
                and isinstance(data["chunk"].content[0], dict)
                and data["chunk"].content[0].get("text", "")
            ):
                yield OnNodeStreamEvent(chunk=data["chunk"].content[0].get("text", ""))
            elif data["chunk"].content and isinstance(data["chunk"].content, str):
                yield OnNodeStreamEvent(chunk=data["chunk"].content)


# def handle_copilotkit_intermediate_state(event: dict):
#     print("Handling copilotkit intermediate state")
#     copilotkit_intermediate_state = event["metadata"].get(
#         "copilotkit:emit-intermediate-state"
#     )
#     print(f"Intermediate state: {copilotkit_intermediate_state}")
#     if copilotkit_intermediate_state:
#         for intermediate_state in copilotkit_intermediate_state:
#             if intermediate_state.get("state_key", "") == "steps":
#                 for tool_call in event["data"]["output"].tool_calls:
#                     if tool_call.get("name", "") == intermediate_state.get("tool", ""):
#                         steps = tool_call["args"].get(
#                             intermediate_state.get("tool_argument")
#                         )
#                         print(f"Yielding steps: {steps}")
#                         yield StepsUpdateEvent(steps=steps)
#     print("--------------------------------")
