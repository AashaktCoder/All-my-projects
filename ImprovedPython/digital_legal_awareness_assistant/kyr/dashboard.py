CATEGORIES = [
    "rights",
    "duties",
    "restrictions",
    "procedures",
    "remedies"
]


def build_kyr(
    rules
):

    result = {
        category: []
        for category in CATEGORIES
    }

    for rule in rules:

        category = rule["category"]

        if category not in result:

            category = "procedures"

        result[category].append(
            rule
        )

    return result