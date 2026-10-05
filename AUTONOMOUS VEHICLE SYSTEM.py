# CATEGORY 8 - KNOWLEDGE BASE
# Problem 2: Autonomous Vehicle
# KNOWLEDGE BASE - FACTS
facts = {
    "road_clear",
    "green_light",
    "vehicle_moving"
}

# KNOWLEDGE BASE - RULES

rules = [

    # Traffic rules
    ({"red_light"}, "stop"),
    ({"yellow_light"}, "slow_down"),
    ({"green_light", "road_clear"}, "move_forward"),

    # Safety rules
    ({"obstacle_ahead"}, "slow_down"),
    ({"obstacle_ahead", "vehicle_moving"}, "apply_brakes"),

    # Pedestrian safety
    ({"pedestrian_crossing"}, "stop"),
    ({"pedestrian_nearby"}, "slow_down"),

    # Emergency situations
    ({"accident_ahead"}, "stop"),
    ({"bad_weather"}, "reduce_speed"),

    # Lane-related decisions
    ({"road_clear", "green_light"}, "safe_to_continue")
]

# FORWARD CHAINING

def forward_chaining(initial_facts, rules):

    known_facts = set(initial_facts)

    print("\n========== FORWARD CHAINING ==========")

    changed = True

    while changed:

        changed = False

        for conditions, conclusion in rules:

            if conditions.issubset(known_facts):

                if conclusion not in known_facts:

                    print(
                        "Rule fired:",
                        conditions,
                        "->",
                        conclusion
                    )

                    known_facts.add(conclusion)

                    changed = True

    return known_facts

# BACKWARD CHAINING

def backward_chaining(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    print("Checking:", goal)

    if goal in facts:
        print("  ->", goal, "is a known fact.")
        return True

    if goal in visited:
        return False

    visited.add(goal)
    for conditions, conclusion in rules:

        if conclusion == goal:

            print(
                "  Trying rule:",
                conditions,
                "->",
                conclusion
            )

            possible = True

            for condition in conditions:

                if not backward_chaining(
                    condition,
                    facts,
                    rules,
                    visited
                ):
                    possible = False
                    break

            if possible:
                print("  -> Goal proved:", goal)
                return True

    print("  -> Goal cannot be proved:", goal)

    return False

# MAIN PROGRAM

print("==========================================")
print("        AUTONOMOUS VEHICLE SYSTEM")
print("==========================================")

print("\nCurrent Vehicle Environment:")

for fact in facts:
    print("-", fact)


# ---------- Forward Chaining ----------

derived_facts = forward_chaining(facts, rules)

print("\nKnowledge after Forward Chaining:")

for fact in sorted(derived_facts):
    print("-", fact)


# ---------- Backward Chaining ----------

print("\n========== BACKWARD CHAINING ==========")

goal = input(
    "\nEnter an action to check: "
).strip().lower()

if backward_chaining(goal, facts, rules):

    print("\nRESULT:")
    print(
        "The vehicle can derive that it should:",
        goal
    )

else:

    print("\nRESULT:")
    print(
        "The vehicle cannot derive the action:",
        goal
    )
