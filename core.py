import json


def new_game():
    return {'events': {1: (5, 6), 2: (1, 2)}, 'items': [], 'cap': 2, 'count': 0, 'closed': False, 'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}, 'src': 10, 'dst': 0, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_17(state):
    return state["value"] < 0

def bug_24(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def bug_1(state):
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True

def bug_8(state):
    state["count"] = 0
    return True

def bug_15(state):
    return not state["closed"]

def bug_22(state):
    return True

def bug_29(state):
    state["nodes"].pop(1, None)
    state["edges"] = {
        edge: weight
        for edge, weight in state["edges"].items()
        if 1 not in edge
    }
    return True

def bug_6(state):
    return len(state["items"])

def bug_13(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def bug_20(state):
    state["events"].pop(1, None)
    return True

def bug_30(state):
    if any(result == "failed" for _, result in state["log"]):
        state["value"] = state["snapshot"]
    return True

def bug_31(state):
    return not state["settled"]

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
