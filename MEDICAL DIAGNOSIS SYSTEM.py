# CATEGORY 8 - KNOWLEDGE BASE
# Problem 1: Medical Diagnosis

# KNOWLEDGE BASE

# Facts represent information already known about the patient.
facts = {
    "fever",
    "cough",
    "body_pain",
    "tiredness"
}


rules = [
    ({"fever", "cough", "body_pain"}, "flu"),
    ({"fever", "sore_throat"}, "throat_infection"),
    ({"sneezing", "runny_nose"}, "common_cold"),
    ({"fever", "cough"}, "respiratory_infection"),
    ({"flu", "tiredness"}, "needs_rest"),
    ({"common_cold", "tiredness"}, "needs_rest"),
    ({"fever", "body_pain"}, "possible_viral_infection")
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

    print("Checking goal:", goal)
    if goal in facts:
        print("  ->", goal, "is already a known fact.")
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

            all_conditions_true = True
            for condition in conditions:

                if not backward_chaining(
                    condition,
                    facts,
                    rules,
                    visited
                ):
                    all_conditions_true = False
                    break

            if all_conditions_true:
                print("  -> Goal proved:", goal)
                return True

    print("  -> Could not prove:", goal)

    return False


# MAIN PROGRAM

print("==========================================")
print("       MEDICAL DIAGNOSIS SYSTEM")
print("==========================================")

print("\nInitial Patient Symptoms:")
for fact in facts:
    print("-", fact)


# ---------- Forward Chaining ----------

all_derived_facts = forward_chaining(facts, rules)

print("\nAll facts after Forward Chaining:")
for fact in sorted(all_derived_facts):
    print("-", fact)


# ---------- Backward Chaining ----------

print("\n========== BACKWARD CHAINING ==========")

goal = input(
    "\nEnter a diagnosis/conclusion to check: "
).strip().lower()

if backward_chaining(goal, facts, rules):
    print("\nRESULT:")
    print(goal, "can be proved from the knowledge base.")
else:
    print("\nRESULT:")
    print(goal, "cannot be proved from the knowledge base.")
