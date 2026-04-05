# Lab 5: Cloud-Edge Collaboration and Event-Driven Prototype

**Related chapters:** Ch. 18 (Computing Gap) · Ch. 19 (Cloud-Edge Collaboration) · Ch. 20 (Spatiotemporal Graph Partitioning)

This lab builds a minimal "device–edge–cloud" layered reasoning prototype, mapping Chapters 18–20 ideas — compute/latency gap, tiered deployment, cloud–edge collaboration, event-driven flow — to an executable pipeline.

## Design

- **Event** — message object carrying telemetry or alerts
- **EdgeNode** — lightweight checks on telemetry (separation threshold, summaries)
- **CloudNode** — aggregate edge outputs and emit policies
- **main()** — telemetry stream → edge → cloud pipeline

## Key concepts

1. Compute gap and tiered deployment
2. Cloud–edge collaboration
3. Event-driven scheduling
4. Closed-loop timely response
5. Risk alerts and policy downlink
6. Light rule reasoning vs. centralized decisions

## How to run

```bash
python lab5_edge_cloud_pipeline.py
```

## Source code

```python
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Event:
    event_type: str
    payload: Dict[str, object]


class EdgeNode:
    def __init__(self, node_id: str):
        self.node_id = node_id

    def process(self, event: Event) -> List[Event]:
        forwarded: List[Event] = []
        if event.event_type != "telemetry":
            return forwarded

        altitude = float(event.payload["altitude"])
        speed = float(event.payload["speed"])
        distance = float(event.payload["nearest_distance"])
        uav_id = str(event.payload["uav_id"])

        if distance < 100:
            forwarded.append(
                Event(
                    "edge_alert",
                    {
                        "uav_id": uav_id,
                        "level": "high",
                        "reason": f"nearest_distance={distance}",
                        "source": self.node_id,
                    },
                )
            )

        forwarded.append(
            Event(
                "edge_summary",
                {
                    "uav_id": uav_id,
                    "altitude": altitude,
                    "speed": speed,
                    "nearest_distance": distance,
                    "source": self.node_id,
                },
            )
        )
        return forwarded


class CloudNode:
    def process(self, events: List[Event]) -> List[str]:
        decisions = []
        for event in events:
            if event.event_type == "edge_alert":
                decisions.append(
                    f"[Cloud policy] {event.payload['uav_id']}: high-risk alert — execute conservative avoidance immediately"
                )
            elif event.event_type == "edge_summary":
                if float(event.payload["speed"]) > 22:
                    decisions.append(
                        f"[Cloud policy] {event.payload['uav_id']}: speed high — reduce cruise speed and await new route assignment"
                    )
        return decisions


def main() -> None:
    telemetry_stream = [
        Event("telemetry", {"uav_id": "UAV-01", "altitude": 120, "speed": 24, "nearest_distance": 82}),
        Event("telemetry", {"uav_id": "UAV-02", "altitude": 135, "speed": 16, "nearest_distance": 210}),
    ]

    edge = EdgeNode("edge-node-beijing-01")
    cloud = CloudNode()

    print("=== Cloud-edge reasoning prototype ===")
    forwarded_events: List[Event] = []
    for event in telemetry_stream:
        print(f"[Edge ingest] {event.payload}")
        results = edge.process(event)
        forwarded_events.extend(results)
        for result in results:
            print(f"[Edge emit] {result.event_type}: {result.payload}")

    print("\n=== Cloud aggregation ===")
    for decision in cloud.process(forwarded_events):
        print(decision)


if __name__ == "__main__":
    main()
```
