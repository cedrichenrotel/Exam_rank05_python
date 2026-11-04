from typing import Any


def py_room_scheduler(meetings: list[list[int]]) -> dict[str, Any]:

    rst: dict[str, Any] = {
        "total_rooms": 0,
        "schedule": []
    }
    if meetings == []:
        return rst

    meetings = sorted(meetings)
    scheduler: list[list[list[int]]] = []

    for meeting in meetings:
        start = meeting[0]

        for salle in scheduler:
            end = salle[-1][1]
            if end <= start:
                scheduler.append(meeting)
                break
        else:
            scheduler.append([meeting])
    rst["total_rooms"] = len(scheduler)
    rst["scheduler"] = scheduler
    return rst


if __name__ == "__main__":

    print(py_room_scheduler([[0, 30], [5, 10], [15, 20]]))
