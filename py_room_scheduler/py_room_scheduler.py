from typing import Any


def py_room_scheduler(meetings: list[list[int]]) -> dict[str, Any]:
    """repartitions des salles par rapport au horraires avec condition:
    - ne peux pas avoir 2 reumions dans la meme salle si les horaire ce
    chevauche
    - crer le moins de salle possible

    Args:
        meetings (list[list[int]]): liste des heures de reunions_

    Returns:
        dict[str, Any]: retourne le nombre total de salle creee et
        le descriptif
    """
    rst: dict[str, Any] = {"total_rooms": 0, "schedule": []}
    if meetings == []:
        return rst

    meetings = sorted(meetings)
    schedule: list[list[list[int]]] = []
    for meeting in meetings:
        debut = meeting[0]

        for salle in schedule:
            fin = salle[-1][1]

            if fin <= debut:
                salle.append(meeting)
                break
        else:
            schedule.append([meeting])
    rst["total_rooms"] = len(schedule)
    rst["schedule"] = schedule
    return rst


if __name__ == "__main__":
    print(py_room_scheduler([[0, 30], [5, 10], [15, 20]]))
    print()
    print(py_room_scheduler([]))
