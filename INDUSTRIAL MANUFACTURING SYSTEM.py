# ============================================================
# CATEGORY 8 - KNOWLEDGE BASE
# Problem 3: Industrial Manufacturing
# ============================================================

# ------------------------------------------------------------
# KNOWLEDGE BASE - FACTS
# ------------------------------------------------------------

facts = {
    "machine_running",
    "normal_temperature",
    "normal_vibration",
    "production_active"
}


# ------------------------------------------------------------
# KNOWLEDGE BASE - RULES
# ------------------------------------------------------------

rules = [

    # Machine condition rules
    (
        {"high_temperature"},
        "overheating"
    ),

    (
        {"high_vibration"},
        "mechanical_problem"
    ),

    # Fault detection
    (
        {"high_temperature", "high_vibration"},
        "machine_fault"
    ),

    (
        {"overheating", "machine_running"},
        "temperature_risk"
    ),

    (
        {"mechanical_problem", "machine_running"},
        "maintenance_required"
    ),

    # Safety rules
    (
        {"machine_fault"},
        "stop_machine"
    ),

    (
        {"temperature_risk"},
        "reduce_machine_speed"
    ),

    # Production rules
    (
        {"machine_running", "production_active"},
        "production_in_progress"
    ),

    (
        {"machine_fault", "production_active"},
        "production_stopped"
    ),

    # Maintenance rule
    (
        {"maintenance_required"},
        "schedule_maintenance"
    )
]


# ------------------------------------------------------------
# FORWARD CHAINING
# ------------------------------------------------------------

def forward_chaining(initial_facts, rules):

    known_facts = set(initial_facts)

    print("\n========== FORWARD CHAINING ==========")

    changed = True

    while changed:

        changed = False

        for conditions, conclusion in rules:

            # Check whether all conditions required by
            # the rule are available.
            if conditions.issubset(known_facts):

                # Do not repeatedly add the same fact.
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


# ------------------------------------------------------------
# BACKWARD CHAINING
# ------------------------------------------------------------

def backward_chaining(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    print("Checking goal:", goal)

    # If the goal is directly available as a fact,
    # it is already proven.
    if goal in facts:

        print(
            "  ->",
            goal,
            "is already known."
        )

        return True

    # Avoid infinite recursion.
    if goal in visited:
        return False

    visited.add(goal)

    # Find a rule that can produce our goal.
    for conditions, conclusion in rules:

        if conclusion == goal:

            print(
                "  Trying rule:",
                conditions,
                "->",
                conclusion
            )

            # Assume the rule can prove the goal
            # until one of its conditions fails.
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

                print(
                    "  -> Goal proved:",
                    goal
                )

                return True

    print(
        "  -> Goal could not be proved:",
        goal
    )

    return False


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

print("==========================================")
print("       INDUSTRIAL MANUFACTURING SYSTEM")
print("==========================================")

print("\nInitial Machine Facts:")

for fact in facts:
    print("-", fact)


# ---------- Forward Chaining ----------

derived_facts = forward_chaining(facts, rules)

print("\nFacts after Forward Chaining:")

for fact in sorted(derived_facts):
    print("-", fact)


# ---------- Backward Chaining ----------

print("\n========== BACKWARD CHAINING ==========")

goal = input(
    "\nEnter a machine condition/action to check: "
).strip().lower()

if backward_chaining(goal, facts, rules):

    print("\nRESULT:")
    print(
        "The knowledge base proves that:",
        goal
    )

else:

    print("\nRESULT:")
    print(
        "The knowledge base cannot prove:",
        goal
    )
