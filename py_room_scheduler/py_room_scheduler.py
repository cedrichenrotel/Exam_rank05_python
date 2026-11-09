from typing import Any


def py_room_scheduler(meetings: list[list[int]]) -> dict[str, Any]:

    rst: dict[str, Any] = {"total_rooms": 0, "schedule": {}}
    if meetings == []:
        return rst

    schedule: list[list[list[int]]] = []
    for meeting in sorted(meetings):
        start_slot = meeting[0]
        for room in schedule:
            end_slot = room[-1][1]
            if end_slot <= start_slot:
                room.append(meeting)
                break
        else:
            schedule.append([meeting])

    rst["total_rooms"] = len(schedule)
    rst["schedule"] = {i: room for i, room in enumerate(schedule, 1)}
    return rst


if __name__ == "__main__":
    result = py_room_scheduler([[0, 30], [5, 10], [15, 20]])
    print(result)
    print({"total_rooms": 2, "schedule": {1: [[0, 30]], 2: [[5, 10], [15, 20]]}})
    print()
    print(py_room_scheduler([]))
    print({"total_rooms": 0, "schedule": {}})
